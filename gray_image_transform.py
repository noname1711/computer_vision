from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


my_path = 'C:/computer_vision/img/hust.jpg'
im = Image.open(my_path)
#chuyển đổi sang ảnh xám
image_array = np.array(im.convert('L'))

#thử biến đổi ảnh xám 
inverted_image = 255 - image_array     #đảo chiều màu (đen -> trắng, trắng -> đen)
squared_image = image_array **2  #bình phương giá trị của pixel
clampes_image = np.clip(image_array, 100, 200)   #giới hạn giá trị pixel trong khoảng 100-200, < 100 thì thành 100, >200 thì thành 200

#hiển thị ảnh gốc và hình ảnh đã biến đổi với khoảng trắng (4 ảnh)
fig, axs = plt.subplots(2,2, figsize =(10,10))  # tạo khung ảnh chiều ngang là 2, dọc là 2 và kích thước là 10x10
fig.subplots_adjust(wspace =0.2, hspace= 0.2)

axs[0,0].imshow(image_array,cmap="gray")
axs[0,0].set_title('Ảnh gốc')

axs[0,1].imshow(inverted_image,cmap ="gray")
axs[0,1].set_title('Ảnh đã biến đổi')

axs[1,0].imshow(squared_image,cmap ="gray")
axs[1,0].set_title('Ảnh đã biến đổi')

axs[1,1].imshow(clampes_image,cmap ="gray")
axs[1,1].set_title('Ảnh đã biến đổi')

plt.show()