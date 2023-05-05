{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMM/y8Gpm29cGMZi17mRmkL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Patric-Ramz/CapeTownFireDashboard/blob/main/CapeTownFire.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CsV2HmSk2J6m",
        "outputId": "cfda0471-6c29-4048-85f4-20259b859651"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "# MOUNT Google Drive\n",
        "from google.colab import drive\n",
        "drive.mount('/content/drive')\n",
        "import pandas as pd \n",
        "\n",
        "q1 = pd.read_csv('/content/drive/My Drive/Cape_Town_Fire_Data/data.csv', sep = ',')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Exploring the dataset\n",
        "print(q1.head(5))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yGxp2V_h4PaT",
        "outputId": "e407ad8a-5db1-4bf0-c554-25cad5790dbe"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Month  Day  Suburb  107 - INFORMATION CALL  ACCIDENT - PEDESTRIAN  \\\n",
            "0      7    4     460                     1.0                    NaN   \n",
            "1      9    5     661                     1.0                    NaN   \n",
            "2      1    1     205                     NaN                    1.0   \n",
            "3      1    1     426                     NaN                    1.0   \n",
            "4      1    1     465                     NaN                    1.0   \n",
            "\n",
            "   ACCIDENT - VECHILE  ALERT - CONTROLLED BURN  \\\n",
            "0                 NaN                      NaN   \n",
            "1                 NaN                      NaN   \n",
            "2                 NaN                      NaN   \n",
            "3                 NaN                      NaN   \n",
            "4                 NaN                      NaN   \n",
            "\n",
            "   ALERT - PROTEST ACTION / PUBLIC VIOLENCE  ALERT - WATER INTERUPTION  \\\n",
            "0                                       NaN                        NaN   \n",
            "1                                       NaN                        NaN   \n",
            "2                                       NaN                        NaN   \n",
            "3                                       NaN                        NaN   \n",
            "4                                       NaN                        NaN   \n",
            "\n",
            "   AVIATION INCIDENT - COMMERCIAL / LARGE AIRCRAFT AC  ...  \\\n",
            "0                                                NaN   ...   \n",
            "1                                                NaN   ...   \n",
            "2                                                NaN   ...   \n",
            "3                                                NaN   ...   \n",
            "4                                                NaN   ...   \n",
            "\n",
            "   TRAUMA - ENVIRONMENTAL - HEAT EXPOSURE  TRAUMA - NEAR DROWNING  \\\n",
            "0                                     NaN                     NaN   \n",
            "1                                     NaN                     NaN   \n",
            "2                                     NaN                     NaN   \n",
            "3                                     NaN                     NaN   \n",
            "4                                     NaN                     NaN   \n",
            "\n",
            "   TRAUMA - SELF HARM - OTHER  TRAUMA - SELF HARM - POISONING  \\\n",
            "0                         NaN                             NaN   \n",
            "1                         NaN                             NaN   \n",
            "2                         NaN                             NaN   \n",
            "3                         NaN                             NaN   \n",
            "4                         NaN                             NaN   \n",
            "\n",
            "   TRAUMA - SELF HARM - WEAPON (GUNSHOT)  TRAUMA - SELF HARM - WEAPON (OTHER)  \\\n",
            "0                                    NaN                                  NaN   \n",
            "1                                    NaN                                  NaN   \n",
            "2                                    NaN                                  NaN   \n",
            "3                                    NaN                                  NaN   \n",
            "4                                    NaN                                  NaN   \n",
            "\n",
            "   VCP  VEHICLE MOVEMENT  VEHICLE REFUELING  NA  \n",
            "0  NaN               NaN                NaN NaN  \n",
            "1  NaN               NaN                NaN NaN  \n",
            "2  NaN               NaN                NaN NaN  \n",
            "3  NaN               NaN                NaN NaN  \n",
            "4  NaN               NaN                NaN NaN  \n",
            "\n",
            "[5 rows x 167 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "q2 = q1.melt(id_vars=[\"Month\", \"Day\", \"Suburb\"], \n",
        "             var_name=\"Sub Category\", \n",
        "             value_name=\"Count\")"
      ],
      "metadata": {
        "id": "Nt5b0C1I4uqQ"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(q2.head(5))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ml7i2JbX6CrA",
        "outputId": "96ddc8f8-6d8e-43e6-e817-49647b778dff"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Month  Day  Suburb            Sub Category  Count\n",
            "0      7    4     460  107 - INFORMATION CALL    1.0\n",
            "1      9    5     661  107 - INFORMATION CALL    1.0\n",
            "2      1    1     205  107 - INFORMATION CALL    NaN\n",
            "3      1    1     426  107 - INFORMATION CALL    NaN\n",
            "4      1    1     465  107 - INFORMATION CALL    NaN\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "q3 = q2.dropna(subset=['Count'])"
      ],
      "metadata": {
        "id": "SPkOwRTN6QUU"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(q3.head(5))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aZvHRvNC6wTQ",
        "outputId": "6cfe9779-8c6c-4296-e96c-ad071d7a924a"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "       Month  Day  Suburb            Sub Category  Count\n",
            "0          7    4     460  107 - INFORMATION CALL    1.0\n",
            "1          9    5     661  107 - INFORMATION CALL    1.0\n",
            "18982      1    1     205   ACCIDENT - PEDESTRIAN    1.0\n",
            "18983      1    1     426   ACCIDENT - PEDESTRIAN    1.0\n",
            "18984      1    1     465   ACCIDENT - PEDESTRIAN    1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "# spliting the values in the column `Sub Category` into the columns `Category` and `Sub Category`\n",
        "q4 = q3.copy()\n",
        "q4['Category'] = q4['Sub Category'].str.extract(r'^([^ -]+)')\n",
        "q4['Sub Category'] = q4['Sub Category'].str.replace(r'^[^-]+-(.*)', r'\\1')\n",
        "q4 = q4[['Month', 'Day', 'Suburb', 'Category', 'Sub Category', 'Count']]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xHoo2lqY66qH",
        "outputId": "4e3b426d-4fbf-464f-c0d8-c3f827413ccf"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-8-0e22284511b6>:5: FutureWarning: The default value of regex will change from True to False in a future version.\n",
            "  q4['Sub Category'] = q4['Sub Category'].str.replace(r'^[^-]+-(.*)', r'\\1')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(q4.head(5))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BmUcFQBl71mh",
        "outputId": "0f21094b-e4ac-43b6-fe05-10dd907851a8"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "       Month  Day  Suburb  Category       Sub Category  Count\n",
            "0          7    4     460       107   INFORMATION CALL    1.0\n",
            "1          9    5     661       107   INFORMATION CALL    1.0\n",
            "18982      1    1     205  ACCIDENT         PEDESTRIAN    1.0\n",
            "18983      1    1     426  ACCIDENT         PEDESTRIAN    1.0\n",
            "18984      1    1     465  ACCIDENT         PEDESTRIAN    1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Removing rows where the total count per `Sub Category` per year was less than or equal to 10\n",
        "\n",
        "q5 = q4.groupby('Sub Category').agg(Count=('Count', 'sum')).reset_index()\n",
        "q5 = q5[q5['Count'] > 10]\n",
        "q5 = q4.merge(q5[['Sub Category']], on='Sub Category', how='inner')"
      ],
      "metadata": {
        "id": "nYoKCdSz9FNH"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(q5.head(5))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dhp00OMU9Xad",
        "outputId": "0fdd374a-d98d-4393-da62-afee61231f91"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Month  Day  Suburb  Category Sub Category  Count\n",
            "0      1    1     205  ACCIDENT   PEDESTRIAN    1.0\n",
            "1      1    1     426  ACCIDENT   PEDESTRIAN    1.0\n",
            "2      1    1     465  ACCIDENT   PEDESTRIAN    1.0\n",
            "3      1    1     517  ACCIDENT   PEDESTRIAN    1.0\n",
            "4      1    1     570  ACCIDENT   PEDESTRIAN    1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit\n",
        "\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import altair as alt\n",
        "\n",
        "# Create the visualization using Altair\n",
        "chart = alt.Chart(q5).mark_bar().encode(\n",
        "    x=alt.X('Count:Q', title='Number of Incidents'),\n",
        "    y=alt.Y('Category:N', title='Category'),\n",
        "    tooltip=[alt.Tooltip('Count:Q', title='Number of Incidents')]\n",
        ").properties(\n",
        "    title='Number of Incidents Reported per Category'\n",
        ")\n",
        "\n",
        "# Display the visualization in Streamlit\n",
        "st.altair_chart(chart, use_container_width=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mrlfuatN9dgY",
        "outputId": "ef9d2764-a1ad-464c-a01f-0381caa7a674"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.22.0-py2.py3-none-any.whl (8.9 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.9/8.9 MB\u001b[0m \u001b[31m71.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tenacity<9,>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.2.2)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.27.1)\n",
            "Collecting watchdog\n",
            "  Downloading watchdog-3.0.0-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.1/82.1 kB\u001b[0m \u001b[31m9.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tornado>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.2)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.22.4)\n",
            "Collecting pympler>=0.9\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m164.8/164.8 kB\u001b[0m \u001b[31m16.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.5.0)\n",
            "Collecting importlib-metadata>=1.4\n",
            "  Downloading importlib_metadata-6.6.0-py3-none-any.whl (22 kB)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (23.1)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: altair<5,>=3.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Collecting validators>=0.2\n",
            "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pandas<3,>=0.25 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.5.3)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.3)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.3.4)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.3)\n",
            "Collecting pydeck>=0.1.dev5\n",
            "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m125.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.4.0)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.3.0)\n",
            "Collecting blinker>=1.0.0\n",
            "  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)\n",
            "Collecting gitpython!=3.1.19\n",
            "  Downloading GitPython-3.1.31-py3-none-any.whl (184 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m184.3/184.3 kB\u001b[0m \u001b[31m23.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (0.12.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (3.1.2)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (4.3.3)\n",
            "Collecting gitdb<5,>=4.0.1\n",
            "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m7.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata>=1.4->streamlit) (3.15.0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=0.25->streamlit) (2022.7.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil->streamlit) (1.16.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (3.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (2.0.12)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (1.26.15)\n",
            "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit) (2.2.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit) (2.14.0)\n",
            "Requirement already satisfied: pytz-deprecation-shim in /usr/local/lib/python3.10/dist-packages (from tzlocal>=1.1->streamlit) (0.1.0.post0)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
            "Collecting smmap<6,>=3.0.1\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<5,>=3.2.0->streamlit) (2.1.2)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (23.1.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (0.19.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.11.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: tzdata in /usr/local/lib/python3.10/dist-packages (from pytz-deprecation-shim->tzlocal>=1.1->streamlit) (2023.3)\n",
            "Building wheels for collected packages: validators\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19579 sha256=0e1d07e903f31e5d8cd225067b70b2229fe393fb6eb066287c6942afafe32ac7\n",
            "  Stored in directory: /root/.cache/pip/wheels/f2/ed/dd/d3a556ad245ef9dc570c6bcd2f22886d17b0b408dd3bbb9ac3\n",
            "Successfully built validators\n",
            "Installing collected packages: watchdog, validators, smmap, pympler, importlib-metadata, blinker, pydeck, gitdb, gitpython, streamlit\n",
            "Successfully installed blinker-1.6.2 gitdb-4.0.10 gitpython-3.1.31 importlib-metadata-6.6.0 pydeck-0.8.1b0 pympler-1.0.1 smmap-5.0.0 streamlit-1.22.0 validators-0.20.0 watchdog-3.0.0\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2023-05-04 22:58:40.182 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pickle\n",
        "import hashlib\n",
        "from types import FunctionType as function\n",
        "\n",
        "def hash_func(func):\n",
        "    # Serialize the object using pickle\n",
        "    obj_str = pickle.dumps(func)\n",
        "    \n",
        "    # Hash the serialized object using SHA256\n",
        "    h = hashlib.sha256()\n",
        "    h.update(obj_str)\n",
        "    return h.digest()"
      ],
      "metadata": {
        "id": "gQ8VBgtuAqgA"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Define the plot\n",
        "@st.cache(hash_funcs={function: hash_func})\n",
        "def generate_plot():\n",
        "    # Filter the data\n",
        "    my_summary = q5.groupby('Category').agg(Count=('Count', 'sum')).reset_index().sort_values('Count', ascending=False)\n",
        "    selected_categories = my_summary['Category'].head(num_categories)\n",
        "    other_count = q5[~q5['Category'].isin(selected_categories)]['Count'].sum()\n",
        "    selected_data = q5[q5['Category'].isin(selected_categories)]\n",
        "    \n",
        "    # Create the plot using Altair\n",
        "    chart = alt.Chart(selected_data).mark_bar().encode(\n",
        "        x=alt.X('Count:Q', title='Count'),\n",
        "        y=alt.Y('Category:N', sort='-x', title='Category'),\n",
        "        tooltip=[alt.Tooltip('Count:Q', title='Count')]\n",
        "    ).properties(\n",
        "        title='Number of Fires per Category'\n",
        "    )\n",
        "\n",
        "    return chart"
      ],
      "metadata": {
        "id": "TKBNNJQBEcKW"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "q6 = q5.copy()\n",
        "q6['Year'] = 2018\n",
        "q6['Date'] = pd.to_datetime(q6[['Year', 'Month', 'Day']])\n",
        "q6 = q6[['Date', 'Suburb', 'Category', 'Sub Category', 'Count']]\n",
        "q6['Weekday'] = q6['Date'].dt.day_name().astype(pd.CategoricalDtype(categories=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']))"
      ],
      "metadata": {
        "id": "CDDSs13BFtKF"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a new dataframe with the desired columns and filters\n",
        "q9 = (q6.assign(Months=pd.Categorical(pd.to_datetime(q6['Date']).dt.strftime('%b'),\n",
        "                                       categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']))\n",
        "      .query('Category == \"RESIDENTIAL FIRE \"')\n",
        "      .groupby(['Months', 'Sub Category'])\n",
        "      .agg(count=('Count', 'sum'))\n",
        "      .reset_index())\n",
        "\n",
        "# Create the visualization using Altair\n",
        "def generate_plot():\n",
        "    bars = alt.Chart(q9).mark_bar().encode(\n",
        "        x='Months:O',\n",
        "        y='count:Q',\n",
        "        color=alt.Color('Sub Category:N', legend=alt.Legend(title='Sub Category'))\n",
        "    )\n",
        "\n",
        "    chart = (bars\n",
        "             .properties(width=500, height=300)\n",
        "             .configure_axis(labelFontSize=14, titleFontSize=16)\n",
        "             .configure_legend(labelFontSize=14, titleFontSize=16))\n",
        "\n",
        "    return chart\n",
        "\n",
        "st.altair_chart(generate_plot(), use_container_width=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SqgtU9CtGAZO",
        "outputId": "fdbcf1f1-4f68-4bc7-d500-90196451b575"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install geopandas\n",
        "\n",
        "import geopandas as gpd\n",
        "\n",
        "# Load the GeoJSON file\n",
        "map = gpd.read_file('/content/drive/My Drive/Cape_Town_Fire_Data/CapeTownMap.geojson')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WzftRhUgGvsv",
        "outputId": "5e482a68-94f5-49ff-814b-c4704b4ca901"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting geopandas\n",
            "  Downloading geopandas-0.12.2-py3-none-any.whl (1.1 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.1/1.1 MB\u001b[0m \u001b[31m47.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pyproj>=2.6.1.post1\n",
            "  Downloading pyproj-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (7.7 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m7.7/7.7 MB\u001b[0m \u001b[31m113.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: shapely>=1.7 in /usr/local/lib/python3.10/dist-packages (from geopandas) (2.0.1)\n",
            "Collecting fiona>=1.8\n",
            "  Downloading Fiona-1.9.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.0 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m16.0/16.0 MB\u001b[0m \u001b[31m77.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from geopandas) (23.1)\n",
            "Requirement already satisfied: pandas>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from geopandas) (1.5.3)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from fiona>=1.8->geopandas) (2022.12.7)\n",
            "Requirement already satisfied: attrs>=19.2.0 in /usr/local/lib/python3.10/dist-packages (from fiona>=1.8->geopandas) (23.1.0)\n",
            "Collecting cligj>=0.5\n",
            "  Downloading cligj-0.7.2-py3-none-any.whl (7.1 kB)\n",
            "Collecting munch>=2.3.2\n",
            "  Downloading munch-2.5.0-py2.py3-none-any.whl (10 kB)\n",
            "Collecting click-plugins>=1.0\n",
            "  Downloading click_plugins-1.1.1-py2.py3-none-any.whl (7.5 kB)\n",
            "Requirement already satisfied: click~=8.0 in /usr/local/lib/python3.10/dist-packages (from fiona>=1.8->geopandas) (8.1.3)\n",
            "Requirement already satisfied: numpy>=1.21.0 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.0.0->geopandas) (1.22.4)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.0.0->geopandas) (2022.7.1)\n",
            "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.0.0->geopandas) (2.8.2)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from munch>=2.3.2->fiona>=1.8->geopandas) (1.16.0)\n",
            "Installing collected packages: pyproj, munch, cligj, click-plugins, fiona, geopandas\n",
            "Successfully installed click-plugins-1.1.1 cligj-0.7.2 fiona-1.9.3 geopandas-0.12.2 munch-2.5.0 pyproj-3.5.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(map.crs)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "caP2tn5MILf5",
        "outputId": "05e255d3-2ef3-47e2-ebed-7b5be4bbfc83"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "EPSG:4326\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "map = map.to_crs('epsg:4326')\n",
        "\n",
        "# Tidy the GeoDataFrame\n",
        "map = map.dropna()"
      ],
      "metadata": {
        "id": "ugcpkBgjIYGt"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.write(map)"
      ],
      "metadata": {
        "id": "zWKfxLKxIxTu"
      },
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "lookup = pd.read_csv('/content/drive/My Drive/Cape_Town_Fire_Data/lookup.csv', sep = ',')"
      ],
      "metadata": {
        "id": "0WsqI4dFKWp_"
      },
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(lookup.head(5))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ukwNEPDiLNTs",
        "outputId": "e806004d-696b-490a-ffd4-414135b76698"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    ID                    Suburb\n",
            "0  774  AAN DE WIJNLANDEN ESTATE\n",
            "1  591               ACACIA PARK\n",
            "2  586             ADMIRALS PARK\n",
            "3  500                 ADRIAANSE\n",
            "4  233                   AIRPORT\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(map.head(5))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "usF-NRAhLmnX",
        "outputId": "a6e4ad1b-a6d2-48da-f725-7e64e64f3159"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   OBJECTID       OFC_SBRB_NAME  SHAPE_STArea__  SHAPE_STLength__  \\\n",
            "0         1           HYDE PARK               0                 0   \n",
            "1         2         SPRINGFIELD               0                 0   \n",
            "2         3  NIEUW MAASTRECHT-2               0                 0   \n",
            "3         4        CHARLESVILLE               0                 0   \n",
            "4         5            WILDWOOD               0                 0   \n",
            "\n",
            "     SHAPESTArea  SHAPESTLength  \\\n",
            "0   73482.984467    1248.309489   \n",
            "1  563248.378242    4122.216062   \n",
            "2  577520.411263    3125.364759   \n",
            "3  290334.013199    2303.999697   \n",
            "4  134618.519958    1629.455806   \n",
            "\n",
            "                                            geometry  \n",
            "0  POLYGON ((18.58526 -34.03099, 18.58526 -34.030...  \n",
            "1  POLYGON ((18.60537 -33.83933, 18.60536 -33.839...  \n",
            "2  POLYGON ((18.59845 -33.85189, 18.59868 -33.851...  \n",
            "3  POLYGON ((18.56878 -33.96377, 18.56878 -33.963...  \n",
            "4  POLYGON ((18.58097 -34.03246, 18.58101 -34.032...  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Perform data wrangling\n",
        "s3 = q5.groupby(\"Suburb\").sum().reset_index().rename(columns={\"Suburb\": \"ID\", \"Count\": \"count\"})\n",
        "S3_lookup = pd.merge(lookup, s3, how=\"left\", on=\"ID\").rename(columns={\"ID\": \"id\"})\n",
        "map = map.assign(id=pd.to_numeric(map[\"OBJECTID\"])).drop(columns=[\"geometry\"])\n",
        "s3_map = pd.merge(map, S3_lookup, how=\"left\", on=\"id\")\n",
        "\n",
        "# Create the visualization\n",
        "chart = (\n",
        "    alt.Chart(s3_map)\n",
        "    .mark_geoshape(stroke=\"black\", strokeWidth=0.2)\n",
        "    .encode(color=alt.Color(\"count:Q\", title=\"Number of Fires Reported\"))\n",
        "    .properties(width=800, height=600)\n",
        ")\n",
        "st.altair_chart(chart)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jBEws7WwKmSu",
        "outputId": "4c0ab9f0-acab-43f5-fd61-5275a640f3b5"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-48-c5f0e5d5db85>:2: FutureWarning: The default value of numeric_only in DataFrameGroupBy.sum is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.\n",
            "  s3 = q5.groupby(\"Suburb\").sum().reset_index().rename(columns={\"Suburb\": \"ID\", \"Count\": \"count\"})\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(s3_map.head(5))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PYn9zq6bQwL2",
        "outputId": "f1817b1d-c1de-4146-a20f-a5e716cb112b"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   OBJECTID       OFC_SBRB_NAME  SHAPE_STArea__  SHAPE_STLength__  \\\n",
            "0         1           HYDE PARK               0                 0   \n",
            "1         2         SPRINGFIELD               0                 0   \n",
            "2         3  NIEUW MAASTRECHT-2               0                 0   \n",
            "3         4        CHARLESVILLE               0                 0   \n",
            "4         5            WILDWOOD               0                 0   \n",
            "\n",
            "     SHAPESTArea  SHAPESTLength  id_x  id_y              Suburb  count  \n",
            "0   73482.984467    1248.309489     1     1           HYDE PARK    2.0  \n",
            "1  563248.378242    4122.216062     2     2         SPRINGFIELD    1.0  \n",
            "2  577520.411263    3125.364759     3     3  NIEUW MAASTRECHT-2    0.0  \n",
            "3  290334.013199    2303.999697     4     4        CHARLESVILLE    1.0  \n",
            "4  134618.519958    1629.455806     5     5            WILDWOOD   29.0  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Group by suburb and get the sum of counts\n",
        "s3 = q5.groupby('Suburb').sum('Count').reset_index().rename(columns={'Suburb': 'ID', 'Count': 'count'})\n",
        "\n",
        "# Merge the dataframes\n",
        "s3_lookup = pd.merge(lookup, s3, how='left', left_on='ID', right_on='ID').rename(columns={'ID': 'id'})\n",
        "s3_map = pd.merge(map, s3_lookup, how='left', left_on='id', right_on='id')\n",
        "s3_map['count'] = s3_map['count'].fillna(0)\n",
        "\n",
        "# Create the visualization\n",
        "chart = alt.Chart(s3_map).mark_geoshape(\n",
        "    stroke='white'\n",
        ").encode(\n",
        "    color=alt.Color('count:Q', scale=alt.Scale(domain=[0, 1], range=['red', 'white']), title='Fire Reports',\n",
        "                    legend=alt.Legend(orient='bottom', title=None, labelFontSize=12, labelFont='Helvetica Neue')),\n",
        "    tooltip=['Suburb', 'count:Q']\n",
        ").properties(\n",
        "    width=700,\n",
        "    height=500\n",
        ").project(\n",
        "    type='mercator'\n",
        ")\n",
        "\n",
        "# Show the visualization\n",
        "st.altair_chart(chart)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2fo7MrblQafD",
        "outputId": "899ede87-fc6d-46be-e356-956906b87d8d"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 51
        }
      ]
    }
  ]
}