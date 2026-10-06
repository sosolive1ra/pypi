import streamlit as st

st.title("Meu primeiro site com Streamlit")

st.write("Olá! Esse é meu primeiro projeto usando Streamlit.")

nome = st.text_input("Digite seu nome:")

if st.button("Enviar"):
    st.success(f"Olá, {nome}! Seja bem-vindo(a)!")