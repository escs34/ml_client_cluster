import numpy as np
from PIL import Image

import os

directory = 'images'
if not os.path.exists(directory):
    os.mkdir(directory)

img_number = 1000
for i in range(1, img_number+1):
    im = (np.random.rand(32,32,3)*100).astype('uint8')
    img = Image.fromarray(im)
    img.save('./images/pic_'+str(i) + '.jpeg')


