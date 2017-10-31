from tensorflow_vgg import utils
import os
import matplotlib.pyplot as plt
import pylab
from scipy.ndimage import imread

# 图片裁剪工具包，以H为基准，裁剪图片中部，压缩至指定像素

test_img_path = 'flower_photos/roses/10894627425_ec76bbc757_n.jpg'
# test_img = imread(test_img_path)
# test_img.reshape(1, 224, 224, 3)
# plt.imshow(test_img)
# pylab.show()


img = utils.load_image(test_img_path)

plt.imshow(img)
pylab.show()



