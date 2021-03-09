import streamlit as st
import streamlit.components.v1 as stc

stc.html("<h1 style='text-align: center'>Gluon Style Transfer</h1>")

col_img= st.beta_columns(3)

selected_original_image = ''

with col_img[0]:
    st.header("original image")
    original_image = st.empty()
    selected_original_image = st.file_uploader('select original image', type='jpg')

with col_img[1]:
    st.header("style image")
    style_image = st.empty()
    selected_style_image = st.file_uploader('select style image', type='jpg')
    
with col_img[2]:
    st.header("result")
    result_image = st.empty()

if selected_original_image != None:
    original_image.image(selected_original_image)

if selected_style_image != None:
    style_image.image(selected_style_image)