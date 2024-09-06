from PIL import Image

from IPython.display import display  #thư viện IPython để dùng display

#import imgtools.py vừa code và lấy mọi phương thức = *
from imgtools import *

my_path = 'C:/computer_vision/img/hust.jpg'

img = load_image(my_path)

display(img)


#in kích thước ban đầu:
print(img.size)

#thay đổi kích thước
new_image = img.resize((100, 100))
display(new_image)
new_image.show()     #show ra kích thước đã thay đổi


new_image_2= img.thumbnail(50,50)     #thumbnail cũng có tác dụng như resize
#tuy nhiên có sự khác biệt giữa resize (thay đổi kích thước và tạo ra ảnh mới, ảnh cũ vẫn nguyên) còn thumbnail thì thay đổi kích thước ảnh gốc luôn
new_image_2.show()

