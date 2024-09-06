from PIL import Image
from IPython.display import display  #thư viện IPython để dùng display
#import imgtools.py vừa code và lấy mọi phương thức = *
from imgtools import *

my_path = 'C:/computer_vision/img/hust.jpg'
img = load_image(my_path)
#img.show()

#xoay ảnh dựa trên 1 trục ảnh
rotate_image = img.rotate(90)  #xoay ảnh 90 độ, lưu ý ngược chiều kim đồng hồ
#lưu ý do kích thước ko đổi nên khi xoay ảnh có thể bị mất đi 1 vài phần
#như vậy trước khi xoay ảnh nên resize ảnh về ảnh vuông
rotate_image.show()

#đảo chiều ảnh
transposed_image = img.transpose(Image.Transpose.ROTATE_90)
transposed_image.show()
#khi transpose thì ảnh sẽ ko bị mất pixel nào mà chỉ đơn giản là đảo chiều 
#nôm na là chiều rộng thành chiều cao và ngược lại
