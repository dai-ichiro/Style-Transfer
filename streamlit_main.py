import streamlit as st
import streamlit.components.v1 as stc

import mxnet as mx

import net 
import utils

### setting ###
ctx = mx.cpu()
content_size = 512
### setting ###

def load_model():
    model = net.Net(ngf=128)
    model.load_parameters('./models/21styles.params', ctx=ctx)
    return model

stc.html("<h1 style='text-align: center'>Gluon Style Transfer</h1>")

col_img= st.beta_columns(3)

selected_original_image = ''
selected_style_image = ''

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
    original_image.image(selected_original_image, use_column_width=True)

if selected_style_image != None:
    style_image.image(selected_style_image, use_column_width=True)

if (selected_original_image != None) & (selected_style_image != None):

    model = load_model()
    content_image = utils.tensor_load_rgbimage(selected_original_image, ctx, size=content_size, keep_asp=True)
    style_image = utils.tensor_load_rgbimage(selected_style_image, ctx, size=512)
    style_image = utils.preprocess_batch(style_image)

    model.set_target(style_image)
    output = model(content_image)
    output = output[0].asnumpy().clip(0, 255).astype('uint8')

    output = output.transpose(1, 2, 0)
    output = output[:,:,[2,1,0]]    

    result_image.image(output, use_column_width=True)

