import streamlit as st
from PIL import Image
st.title("Mi primera app")
st.header("Esta es mi página de presentación")
image= Imagen.open("Flores.webp")
st.image(image, caption="Esta es mi imagen")
