from PIL import Image

from IPython.display import display  #thư viện IPython để dùng display

#import imgtools.py vừa code và lấy mọi phương thức = *
from imgtools import *

#thư mục chứa hình ảnh
my_dir = 'C:/computer_vision/img'

#đọc nhiều ảnh
imgs = get_image_list(my_dir)

"""
#đường dẫn đến hình ảnh
#image_path = dir + '/hust.JPG'  #nếu ảnh ko tồn tại thì sẽ lỗi nhg do try except lên vẫn thực thi dù có lỗi
#vậy nếu đường dẫn có tồn tại nhưng lại dẫn đến 1 file không phải ảnh thì sao
#giả sử có file a.txt
#image_path= dir + '/a.txt'   #thì bị lỗi khi đọc hình ảnh cannot identify image file file ko đúng loại
#viết thêm hàm kiểm tra xem có đúng là hình ảnh hay ko ở imgtools.py

print(image_path)   

#đọc đường dẫn từ phương thức vừa viết ra thì phải import vào
#dọc ảnh từ function

img01 = load_image(image_path)

#hiển thị hình ảnh
img01.show()

#in 1 số thông tin
#in định dạng ảnh
print("định dạng ảnh: " , img01.format)
#in ra size
print("kích thước ảnh: ", img01.size)

#lưu ảnh bằng tên mới và chuyển đổi định dạng ảnh
new_img_01_path =  dir + '/new.JPG'  #đổi tên
new_img_png_01_path= dir + '/new_01.PNG'  #đổi tên và định dạng
#lưu 2 ảnh mới
img01.save(new_img_01_path)
img01.save(new_img_png_01_path)

#đóng tệp tin sau khi đọc
img01.close()

"""
#hiển thị toàn bộ hình ảnh = display
for img in imgs:
    display(img)
