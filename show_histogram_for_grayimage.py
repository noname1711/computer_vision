from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#đọc ảnh gốc
my_path = 'C:/computer_vision/img/hust.jpg'
im= Image.open(my_path)
plt.imshow(im)
#im.show()

#chuyển sang ảnh xám
im_gray = im.convert('L')
plt.imshow(im_gray, cmap='gray')
#im_gray.show()

#vẽ đồ thị histogram của ảnh xám
#biến toàn bộ ảnh thành mảng
im_array = np.array(im_gray)
print(im_array)
#từ mảng có thể hiển thị ra histogram
plt.figure()    #hiển thị dưới dạng mới
plt.hist(im_array.flatten(), bins = 128)
#flatten() biến mảng 2 chiều -> 1 chiều , bins là số lượng ngăn
plt.title('Biểu đồ histogram của ảnh')
plt.xlabel('Giá trị của pixel')
plt.ylabel('Số lượng pixel')
plt.show()