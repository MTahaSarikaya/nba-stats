import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NBA Oyuncu Istatistikleri')

st.markdown("""
Bu site basitleştirilmiş NBA oyuncu istatistik verilerini sunar.
* **Bu projede kullanılan python kütüphaneleri:** base64, pandas, streamlit
* **Veri kaynağı:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

st.sidebar.header('Kullanıcı Girişi Özellikleri')
selected_year = st.sidebar.selectbox('Yıl', list(reversed(range(1975,2023))))

# Web scraping of NBA player stats
@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(selected_year)

# Sidebar - Team selection
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Takım', sorted_unique_team, sorted_unique_team)

# Sidebar - Position selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Pozisyon', unique_pos, unique_pos)

# Filtering data
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Seçilen Takım(lar)ın Oyuncu İstatistiklerini Görüntüle')
st.write('Veri Boyutu: ' + str(df_selected_team.shape[0]) + ' sıra and ' + str(df_selected_team.shape[1]) + ' sütun.')
st.dataframe(df_selected_team)

# Download NBA player stats data
#https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806



st.write("1975-2022 yılları arasındaki basitleştirilmiş NBA oyuncu istatistikleri gözlemlerini sunduğum bu proje aşağıdaki YouTube Videosu yardımıyla yapılmıştır.")
st.write("https://youtu.be/JwSS70SZdyM")
st.write("Copyright © 2023 Tüm Hakları Saklıdır.")
st.write("Muhammed Taha SARIKAYA")

