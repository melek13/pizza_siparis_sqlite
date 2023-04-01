import streamlit as st
import sqlite3
import pandas as pd


st.header("Hayal Pizza")

veri_tabani = sqlite3.connect("pizzadb.sqlite3")
db=veri_tabani.cursor()

db.execute("SELECT * FROM siparisler")
siparisler = db.fetchall()

df=pd.DataFrame(siparisler)

df.columns = ["alici_isim", "alici_adres", "pizza_sec", "pizza_boy", "icecek_sec", "toplam_fiyat"]

st.table(df)