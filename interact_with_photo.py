from PIL import Image
import matplotlib.pyplot as plt

my_path = 'C:/computer_vision/img/hust.jpg'
im = Image.open(my_path)

#plt.switch_backend('tkagg')   chuyển đổi môi trường nếu đang sử dụng jupiter notebook, còn VSC và pycharm thì ko cần
plt.imshow(im)
plt.title('Click on the image to select points')

#sử dụng hàm ginput để chọn điểm trên ảnh
points = plt.ginput(5)   #được chọn 5 điểm
print(points)          #in ra tọa độ 5 điểm mình đã chọn

#hiển thị
plt.show()

#vẽ lại các điểm đã chọn bằng dấu * màu đỏ
plt.close()
plt.imshow(im)
for point in points:
    x, y = point
    plt.plot(x, y, 'r*')
plt.show()
