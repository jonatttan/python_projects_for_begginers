import streamlit as st
import pandas as pd
import plotly.express as px

st.write("# Vendas sys")
salesTable = pd.read_csv("sales.csv")

data = st.date_input("Data")
vendedor = st.selectbox("Vendedor", ["Beatriz", "Debora", "Cleiton"])
produto = st.selectbox("Produto", ["Geladeira", "Microondas", "Fogão"])
quantidade = st.number_input("Quantidade", step=1)
valor = st.number_input("Valor")
botao = st.button("Vendiii!")

st.write("## Vendas cadastradas")
st.dataframe(salesTable)