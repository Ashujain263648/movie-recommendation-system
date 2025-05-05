{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNo4LPhpkis65vHtTrIzWEr",
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
        "<a href=\"https://colab.research.google.com/github/Ashujain263648/movie-recommendation-system/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit pyngrok\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZpSKVorCVh55",
        "outputId": "7a440539-a09d-4351-c8a4-9cc0919be6c8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.45.0-py3-none-any.whl.metadata (8.9 kB)\n",
            "Collecting pyngrok\n",
            "  Downloading pyngrok-7.2.5-py3-none-any.whl.metadata (8.9 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.2.1)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.29.4)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.1.2)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.13.2)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.11/dist-packages (from pyngrok) (6.0.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.37.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.4.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.4.26)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2025.4.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.24.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.45.0-py3-none-any.whl (9.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.9/9.9 MB\u001b[0m \u001b[31m62.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pyngrok-7.2.5-py3-none-any.whl (23 kB)\n",
            "Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m108.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m6.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pyngrok, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 pyngrok-7.2.5 streamlit-1.45.0 watchdog-6.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "import pickle\n",
        "import pandas as pd\n",
        "import requests\n",
        "\n",
        "def fetch_poster(movie_id):\n",
        "  response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0cf9c62ee26e0f1c96e49692d07ef3c8&language=en-US'.format(movie_id))\n",
        "  data=response.json()\n",
        "  print(data)\n",
        "  return \"https://image.tmdb.org/t/p/w500\"+data['poster_path']\n",
        "\n",
        "def recommend(movie):\n",
        "    movie_index = movies[movies['title'] == movie].index[0]\n",
        "    distances = similarity[movie_index]\n",
        "    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]\n",
        "\n",
        "    recommended_movies = []\n",
        "    recommended_movie_posters = []\n",
        "    for i in movies_list:\n",
        "        movie_id = movies.iloc[i[0]].movie_id\n",
        "        recommended_movies.append(movies.iloc[i[0]].title)\n",
        "        recommended_movie_posters.append(fetch_poster(movie_id))\n",
        "\n",
        "    return recommended_movies, recommended_movie_posters  # Return both lists\n",
        "\n",
        "# Load the movie data inside app.py\n",
        "movies_dict = pickle.load(open('movies_dict.pkl','rb'))\n",
        "movies = pd.DataFrame(movies_dict)\n",
        "similarity=pickle.load(open('similarity.pkl','rb'))\n",
        "\n",
        "st.title(\"Movie Recommender System\")\n",
        "\n",
        "st.text_input(\"What's your name?\", key=\"name\")\n",
        "selected_movie_name = st.selectbox(\n",
        "    'How would you like to be contacted?',\n",
        "    (movies['title'].values)\n",
        ")\n",
        "if st.button('Recommend'):\n",
        "  names, posters=recommend(selected_movie_name)\n",
        "  col1, col2, col3, col4, col5 = st.columns(5)\n",
        "  with col1:\n",
        "    st.text(names[0])\n",
        "    st.image(posters[0])\n",
        "  with col2:\n",
        "    st.text(names[1])\n",
        "    st.image(posters[1])\n",
        "  with col3:\n",
        "    st.text(names[2])\n",
        "    st.image(posters[2])\n",
        "  with col4:\n",
        "    st.text(names[3])\n",
        "    st.image(posters[3])\n",
        "  with col5:\n",
        "    st.text(names[4])\n",
        "    st.image(posters[4])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s4MMSpNabdLT",
        "outputId": "ae0fea00-89e6-4301-832a-0d6fb18d4939"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#!ngrok config add-authtoken 2wRBRvEJu5YuQMx2VHce0jZNez0_7Me7NTxH8KvC2GKN8JJxo\n",
        "\n",
        "import subprocess\n",
        "\n",
        "# Use subprocess to run shell commands\n",
        "subprocess.run(['ngrok', 'config', 'add-authtoken', '2wRBRvEJu5YuQMx2VHce0jZNez0_7Me7NTxH8KvC2GKN8JJxo'])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kcOoTLTYZCmL",
        "outputId": "e35d7b60-7f2d-4e37-e765-8dce265d6602"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "CompletedProcess(args=['ngrok', 'config', 'add-authtoken', '2wRBRvEJu5YuQMx2VHce0jZNez0_7Me7NTxH8KvC2GKN8JJxo'], returncode=0)"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pyngrok import ngrok\n",
        "import threading\n",
        "import os\n",
        "\n",
        "# Kill previous tunnels\n",
        "ngrok.kill()\n",
        "\n",
        "# Start tunnel to port 8501\n",
        "public_url = ngrok.connect(8501)\n",
        "print(f\"✅ Public URL: {public_url}\")\n",
        "\n",
        "# Start Streamlit in background\n",
        "def run():\n",
        "    os.system('streamlit run app.py')\n",
        "\n",
        "threading.Thread(target=run).start()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_rHwNfmJZPD7",
        "outputId": "dc36c519-f444-4652-e70d-fa459eaaf388"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ Public URL: NgrokTunnel: \"https://31b1-34-80-179-198.ngrok-free.app\" -> \"http://localhost:8501\"\n"
          ]
        }
      ]
    }
  ]
}