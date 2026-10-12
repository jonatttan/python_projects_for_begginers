import streamlit as st
import pandas as pd
import plotly.express as px

st.write("# Vendas sys")
sales_table = pd.read_csv("sales.csv")
st.sidebar.write("## Cadastrar venda")

data = st.sidebar.date_input("Data")
seller = st.sidebar.selectbox("Vendedor", ["Beatriz", "Debora", "Cleiton"])
product = st.sidebar.selectbox("Produto", ["Geladeira", "Microondas", "Fogão"])
quantity = st.sidebar.number_input("Quantidade", step=1)
value = st.sidebar.number_input("Valor")
send_button = st.sidebar.button("Vendiii!")

if send_button:
    new_sale = [data, seller, product, quantity, value]
    sales_table.loc[len(sales_table)] = new_sale
    sales_table.to_csv("sales.csv", index=False)
    st.success("Venda cadastrada!")

st.write("## Vendas cadastradas")
st.dataframe(sales_table)