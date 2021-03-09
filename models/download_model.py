import os
import zipfile
import shutil
from mxnet import gluon

url = 'https://apache-mxnet.s3-accelerate.amazonaws.com/gluon/models/msgnet_21styles-2cb88353.zip'
filename = gluon.utils.download(url)

with zipfile.ZipFile(filename) as f:
        f.extractall()

os.remove(filename)

shutil.move('msgnet_21styles-2cb88353.params', 'models/21styles.params')
