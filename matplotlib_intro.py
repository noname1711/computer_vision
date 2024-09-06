import matplotlib as mpl
import matplotlib.pyplot as plt

from PIL import Image
my_path = 'C:/computer_vision/img/hust.jpg'

#đọc ảnh và hiển thị
img = Image.open(my_path)
plt.imshow(img)   #hiển thị bằng imshow thì sẽ hiển thị ảnh kèm theo cả tọa độ 
#plt.axis('off')  # Tắt hiển thị trục tọa độ (nếu bạn không muốn thấy trục)
plt.show()     #hiển thị ảnh kèm đồ thị


#vẽ đồ thị cơ bản
x=[1,2,3,4,5]
y=[10,16,20,30,25]
plt.plot(x,y, color='red')   #vẽ từng cặp x,y và đường bằng màu đỏ
plt.title('Ví dụ về biểu đồ')  #tiêu đề
plt.show()


#vẽ đồ thị trên ảnh
im = Image.open(my_path)
x=[100, 100, 400, 400]
y=[200, 300, 200,300]
plt.imshow(im)  #hiển thị hình ảnh
#plt.plot(x,y, 'r*')  #đánh dấu các điểm bằng dấu sao màu đỏ
#plt.plot(x,y, 'ks:')  #đánh dấu các điểm bằng ô vuông và nối với nhau bằng nét đứt (đều màu đen)
#plt.plot(x,y, color='red')     #đánh dấu các điểm và nối chúng với nhau bằng màu đỏ
plt.plot(x,y, 'bo--')   #hiển thị chấm blue tròn nối với nhau bằng nét đứt --
plt.show()