import streamlit as st
from PIL import Image
import requests 
from streamlit_lottie import st_lottie

st.set_page_config(page_title="PaginaPython", page_icon="👩‍💻", layout="wide")
email_contact = "sofialaballeja21@gmail.com"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}<style>", unsafe_allow_html=True)
css_load("C:/Users/Usuario/Desktop/PaginaWeb/Style/main.css")

url = "https://lottie.host/544d9730-6c60-4b85-82f8-8507f96687cb/AFsK078hKS.json"

def load_lottie(url):
    r = requests.get(url)
    if r.status_code  != 200:
        return None
    return r.json()

lottie = load_lottie(url)
#INTRO

with st.container():
    st.header("Hola, bienvenido a mi Portfolio")
    st.title("Sofia Laballeja")
    st.write("Estudiante de Lic. en sistemas de información")
    st.write("Si quieres saber mas sobre mi has clik [AQUI >] (www.linkedin.com/in/sofia-laballeja-a31111248)")

#SOBRE NOSOTROS
with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre mi 👩‍🎓 ")
        st.write("Hola soy Sofia, tengo 22 años y estoy finalizandoel segundo año de mi carrera")
        st.write("[Contactarme >] sofialabellaja21@gmail.com")
    with animation_column:
        st_lottie(lottie, height=400)

#SERVICIOS
with st.container():
    st.write("---")
    st.header("Servicios")
    st.write("##")
    image_column, text_column = st.columns ((1,2))
    with image_column:
        image = Image.open("C:/Users/Usuario/Desktop/PaginaWeb/Imagenes/web-design-3411373_1280.jpg")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Diseño de aplicación")
        st.write(
            """"""
        )
        st.write("[Ver servicios >](www.linkedin.com/in/sofia-laballeja-a31111248)")

#CONTACTO

with st.container():
    st.write("---")
    st.header("Contacta con nosotros")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_contact}" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "Tu nombre" required>
     <input type="email" name="email" placeholder= "Tu email" required></textarea>
     <textarea type="Mensaje" name="mensaje" placeholder= "Tu mensaje aquí" required></textarea>
     <button type="submit">Enviar</button></form>"""
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()