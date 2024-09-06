from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

image_path = 'C:/computer_vision/img/hust.jpg'
image = Image.open(image_path)
gray_image = image.convert('L')   # Chuyển ảnh sang ảnh xám để dễ quan sát độ mờ
image_a = np.array(gray_image)     # Chuyển ảnh xám thành mảng

#Bộ lọc sobel
#tính gradient theo hướng x
gradient_x = ndimage.sobel(image_a, axis= 0, mode ='constant')
#tính gradient theo hướng y
gradient_y = ndimage.sobel(image_a, axis= 1, mode ='constant')
#hiển thị ảnh
fig, axs = plt.subplots(2,2,figsize=(10,8))
axs[0,0].imshow(image, cmap='gray')
axs[0,0].set_title('Ảnh gốc')
axs[0,1].imshow(gray_image, cmap='gray')
axs[0,1].set_title('ảnh xám')
axs[1,0].imshow(gradient_x, cmap='gray')
axs[1,0].set_title('Gradient theo hướng x')
axs[1,1].imshow(gradient_y, cmap='gray')
axs[1,1].set_title('Gradient theo hướng y')
plt.show()


#bộ lọc prewitt
#các ma trận này là công thức của bộ lọc prewitt
#tính gradient theo hướng x(đạo hàm riêng theo x)
gradient_x = ndimage.convolve(image_a, np.array([[-1,0,1],[-1, 0,1],[-1,0,1]]))
#tính gradient theo hướng y(đạo hàm riêng theo y)
gradient_y = ndimage.convolve(image_a, np.array([[-1,-1,-1],[0,0,0],[1,1,1]]))
#tính biên độ gradient
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
#hiển thị ảnh
fig, axs = plt.subplots(2,1,figsize=(10,8))
axs[0].imshow(gray_image, cmap='gray')
axs[0].set_title('ảnh xám')
axs[1].imshow(gradient_magnitude, cmap='gray')
axs[1].set_title('Lọc prewitt theo biên gradient')
plt.show()

