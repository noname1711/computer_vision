from PIL import Image
import matplotlib.pyplot as plt

#đọc ảnh gốc
my_path = 'C:/computer_vision/img/hust.jpg'
im= Image.open(my_path).convert("L")
plt.imshow(im)    #hiển thị ảnh dưới dạng trục tọa độ

plt.figure()    #tạo hình vẽ mới
plt.gray()      #đặt màu sắc là xám
plt.contour(im, origin="image")    #vẽ biểu đồ đường biên sử dụng contour
plt.axis('equal')   #đảm bảo tỉ lệ trục x và y trên biểu đồ là bằng nhau
plt.show()


