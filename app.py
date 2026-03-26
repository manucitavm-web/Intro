import streamlit as st
from PIL import Image
st.title("Mi Primera App")
st.header("Bienvenido, esta es mi página de presentación!!!")
image= Image.open("Pocoyonina.jpg")
st.image(image, caption="Esta es mi imagen")
texto= st.text_input ("Ingresa texto", "Texto inicial")
st.write("El texto que escribiste es",texto)
if st.button("Presiona el botón"):
   st.write("Has presionado el botón")
