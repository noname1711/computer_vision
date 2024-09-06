from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


my_path = 'C:/computer_vision/img/hust.jpg'
im = Image.open(my_path)

#chuyển ảnh về array
im_array = np.array(im)
#kiểm tra kích thước ảnh
print(im_array.shape)           #(1053, 699, 3)  ảnh màu nên kq là mảng 3 chiều
print(im_array.dtype)           #uint8

#chuyển đổi sang ảnh xám
im_array_2 = np.array(im.convert('L'))
print(im_array_2.shape)           #(1053, 699)    ảnh xám nên kq là mảng 2 chiều
print(im_array_2.dtype)             #uint8