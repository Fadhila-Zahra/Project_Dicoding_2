import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Read dataset
df = pd.read_csv("day.csv")

# Mengubah tipe data menjadi kategorikal
cate_cols = ["dteday", "season", "yr", "mnth", "holiday", "weekday", "workingday", "weathersit"]
for col in cate_cols:
    df[col] = df[col].astype('category')

# Mengubah nama kolom
df = df.rename(columns= {'dteday':'date', 'yr':'year', 'mnth':'month', 'weathersit': 'weather', 'hum':'humidity', 'cnt':'count'})

# Melakukan analisi pada seasson
st.header('Musim dengan Jumlah Terbanyak')
st.write(f"Pada musim 3(musim gugur) memiliki jumlah hitungan terbanyak dan paling sedikit adalah musim 1")
fig = px.box(df, x="season", y="count", color="season", width=1000, height=600)
def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
        fig.data[i].name = new_name
custom_legend_name(['season 1','season 2','season 3','season 4' ])
st.plotly_chart(fig)

fig = px.bar(df, x='season', y='count', color="season")
st.plotly_chart(fig)

# melihat informasi dari beberapa fitur
st.header('Pengaruh Cuaca, Musim, Hari Libur, dan Hari Kerja')
st.write(f"weather vs Count = Saat cuaca 1 (Cerah, Sebagian berawan) maka jumlah tertinggi.")
st.write(f"season vs Count = Pada musim 3 (musim gugur) kami memiliki jumlah hitungan tertinggi & paling sedikit di musim 1 (musim semi).")
st.write(f"holiday vs Count = Pada hari libur (1) kita memiliki jumlah hitungan paling sedikit.")
st.write(f"workingday vs Count = Pada hari kerja (hari libur / akhir pekan) kita memiliki jumlah hitungan tertinggi.")
fig, ax = plt.subplots(2,2, figsize = (14,8))
sns.barplot(x = 'weather', y = 'count', data = df, saturation=0.90, ax = ax[0][0])
sns.barplot(x = 'season', y = 'count', data = df,  saturation=0.90, ax = ax[0][1])
sns.barplot(x = 'holiday', y = 'count', data = df, saturation=0.90, ax = ax[1][0])
sns.barplot(x = 'workingday', y = 'count', data = df,  saturation=0.90, ax = ax[1][1])
st.pyplot(fig)

# Seasson
st.header('Pengaruh Musm Terhadap Jumlah')
st.write(f"Pada musim 1 (musim semi) ketika suhu berkisar antara 0,25 hingga 0,29 maka kita memiliki jumlah hitungan tertinggi.")
st.write(f"Pada musim 2 (musim panas) ketika suhu berkisar antara 0,6 hingga 0,64 maka kita memiliki jumlah hitungan tertinggi.")
st.write(f"Pada musim 3 (musim gugur) ketika suhu berkisar antara 0,7 hingga 0,74 maka kita memiliki jumlah hitungan tertinggi.")
st.write(f"Pada musim 4 (musim dingin) ketika suhu berkisar antara 0,3 hingga 0,34 maka kita memiliki jumlah hitungan tertinggi.")
fig = px.histogram (df, x = "temp",  facet_row = "season",  template = 'plotly_dark')
st.plotly_chart(fig)

# Worikingday
st.header('Saat Hari Kerja')
st.write(f"Pada hari kerja 1 ketika temp berkisar antara 0.7 hingga 0.74 maka kita memiliki jumlah hitungan tertinggi.")
st.write(f"Pada hari kerja 0 ketika temp berkisar antara 0.65 sampai 0.69 dan 0.34 sampai 0.39 maka kita memiliki jumlah hitungan tertinggi.")
fig = px.histogram (df, x = "temp",  facet_row = "workingday",  template = 'plotly_dark')
st.plotly_chart(fig)

# Cuaca
st.header('Pengaruh Cuaca')
st.write(f"Dari cuaca 1 memiliki jumlah hitungan tertinggi.")
st.write(f"Dari cuaca 3 memiliki jumlah hitungan paling sedikit.")
fig =  px.pie (df, names = "workingday", hole = 0.4, template = "gridon")
st.plotly_chart(fig)

fig =  px.pie (df, names = "weather", hole = 0.4, template = "plotly_dark")
st.plotly_chart(fig)

fig =  px.pie (df, names = "season", hole = 0.4, template = "plotly_dark")
st.plotly_chart(fig)