from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from uuid import uuid4
import os
import mxnet as mx 

import net
import utils

app = Flask(__name__)

ctx = mx.cpu()
content_size = 512
set_cuda = 0

style_model = net.Net(ngf=128)
style_model.load_parameters('./models/21styles.params', ctx=ctx)

original_image = ''
style_image = ''
result_image = ''

@app.route('/')
def index():
    return render_template('index.html', img1=original_image, img2=style_image, img3=result_image)

@app.post('/upload/<int:id>')
def file_upload(id):
    global original_image
    global style_image

    select_file = request.files['upload_file']
    filename = secure_filename(select_file.filename)
    select_file.save(os.path.join('static', filename))
    if id == 1:
        original_image = filename
    else:
        style_image = filename
    return redirect('/')

@app.route('/transfer')
def transfer():
    global result_image

    if (original_image != '') and (style_image != ''):
        input_file = os.path.join('static', original_image)
        style_file = os.path.join('static', style_image)

        content_image = utils.tensor_load_rgbimage(input_file, ctx, size=content_size, keep_asp=True)
        style_img = utils.tensor_load_rgbimage(style_file, ctx, size=512)
        style_img = utils.preprocess_batch(style_img)

        output_filename = f"{uuid4()}.jpg"
        save_dir = os.path.join('static', output_filename)
        result_image = output_filename

        style_model.set_target(style_img)
        output = style_model(content_image)
        utils.tensor_save_bgrimage(output[0], save_dir, set_cuda)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
