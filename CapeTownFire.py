import pandas as pd 

q1 = pd.read_csv('Data/data.csv', sep = ',')


q2 = q1.melt(id_vars=["Month", "Day", "Suburb"], 
             var_name="Sub Category", 
             value_name="Count")

q3 = q2.dropna(subset=['Count'])

import re
# spliting the values in the column `Sub Category` into the columns `Category` and `Sub Category`
q4 = q3.copy()
q4['Category'] = q4['Sub Category'].str.extract(r'^([^ -]+)')
q4['Sub Category'] = q4['Sub Category'].str.replace(r'^[^-]+-(.*)', r'\1')
q4 = q4[['Month', 'Day', 'Suburb', 'Category', 'Sub Category', 'Count']]


# Removing rows where the total count per `Sub Category` per year was less than or equal to 10

q5 = q4.groupby('Sub Category').agg(Count=('Count', 'sum')).reset_index()
q5 = q5[q5['Count'] > 10]
q5 = q4.merge(q5[['Sub Category']], on='Sub Category', how='inner')


!pip install streamlit

import streamlit as st
import pandas as pd
import altair as alt

# Create the visualization using Altair
chart = alt.Chart(q5).mark_bar().encode(
    x=alt.X('Count:Q', title='Number of Incidents'),
    y=alt.Y('Category:N', title='Category'),
    tooltip=[alt.Tooltip('Count:Q', title='Number of Incidents')]
).properties(
    title='Number of Incidents Reported per Category'
)

# Display the visualization in Streamlit
st.altair_chart(chart, use_container_width=True)

import pickle
import hashlib
from types import FunctionType as function

def hash_func(func):
    # Serialize the object using pickle
    obj_str = pickle.dumps(func)
    
    # Hash the serialized object using SHA256
    h = hashlib.sha256()
    h.update(obj_str)
    return h.digest()

# Define the plot
@st.cache(hash_funcs={function: hash_func})
def generate_plot():
    # Filter the data
    my_summary = q5.groupby('Category').agg(Count=('Count', 'sum')).reset_index().sort_values('Count', ascending=False)
    selected_categories = my_summary['Category'].head(num_categories)
    other_count = q5[~q5['Category'].isin(selected_categories)]['Count'].sum()
    selected_data = q5[q5['Category'].isin(selected_categories)]
    
    # Create the plot using Altair
    chart = alt.Chart(selected_data).mark_bar().encode(
        x=alt.X('Count:Q', title='Count'),
        y=alt.Y('Category:N', sort='-x', title='Category'),
        tooltip=[alt.Tooltip('Count:Q', title='Count')]
    ).properties(
        title='Number of Fires per Category'
    )

    return chart

q6 = q5.copy()
q6['Year'] = 2018
q6['Date'] = pd.to_datetime(q6[['Year', 'Month', 'Day']])
q6 = q6[['Date', 'Suburb', 'Category', 'Sub Category', 'Count']]
q6['Weekday'] = q6['Date'].dt.day_name().astype(pd.CategoricalDtype(categories=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']))

# Create a new dataframe with the desired columns and filters
q9 = (q6.assign(Months=pd.Categorical(pd.to_datetime(q6['Date']).dt.strftime('%b'),
                                       categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']))
      .query('Category == "RESIDENTIAL FIRE "')
      .groupby(['Months', 'Sub Category'])
      .agg(count=('Count', 'sum'))
      .reset_index())

# Create the visualization using Altair
def generate_plot():
    bars = alt.Chart(q9).mark_bar().encode(
        x='Months:O',
        y='count:Q',
        color=alt.Color('Sub Category:N', legend=alt.Legend(title='Sub Category'))
    )

    chart = (bars
             .properties(width=500, height=300)
             .configure_axis(labelFontSize=14, titleFontSize=16)
             .configure_legend(labelFontSize=14, titleFontSize=16))

    return chart

st.altair_chart(generate_plot(), use_container_width=True)

!pip install geopandas

import geopandas as gpd

# Load the GeoJSON file
map = gpd.read_file('Data/CapeTownMap.geojson')

map = map.to_crs('epsg:4326')

# Tidy the GeoDataFrame
map = map.dropna()

st.write(map)

lookup = pd.read_csv('Data/lookup.csv', sep = ',')

# Perform data wrangling
s3 = q5.groupby("Suburb").sum().reset_index().rename(columns={"Suburb": "ID", "Count": "count"})
S3_lookup = pd.merge(lookup, s3, how="left", on="ID").rename(columns={"ID": "id"})
map = map.assign(id=pd.to_numeric(map["OBJECTID"])).drop(columns=["geometry"])
s3_map = pd.merge(map, S3_lookup, how="left", on="id")

# Create the visualization
chart = (
    alt.Chart(s3_map)
    .mark_geoshape(stroke="black", strokeWidth=0.2)
    .encode(color=alt.Color("count:Q", title="Number of Fires Reported"))
    .properties(width=800, height=600)
)
st.altair_chart(chart)

# Group by suburb and get the sum of counts
s3 = q5.groupby('Suburb').sum('Count').reset_index().rename(columns={'Suburb': 'ID', 'Count': 'count'})

# Merge the dataframes
s3_lookup = pd.merge(lookup, s3, how='left', left_on='ID', right_on='ID').rename(columns={'ID': 'id'})
s3_map = pd.merge(map, s3_lookup, how='left', left_on='id', right_on='id')
s3_map['count'] = s3_map['count'].fillna(0)

# Create the visualization
chart = alt.Chart(s3_map).mark_geoshape(
    stroke='white'
).encode(
    color=alt.Color('count:Q', scale=alt.Scale(domain=[0, 1], range=['red', 'white']), title='Fire Reports',
                    legend=alt.Legend(orient='bottom', title=None, labelFontSize=12, labelFont='Helvetica Neue')),
    tooltip=['Suburb', 'count:Q']
).properties(
    width=700,
    height=500
).project(
    type='mercator'
)

# Show the visualization
st.altair_chart(chart)

