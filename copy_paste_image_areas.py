from PIL import Image

from IPython.display import display  #thư viện IPython để dùng display

#import imgtools.py vừa code và lấy mọi phương thức = *
from imgtools import *

my_path = 'C:/computer_vision/img/hust.jpg'

img = load_image(my_path)

#img.show()

#định vị khu vực cắt 
region = (80,65, 210, 200)    #80, 65 lần lượt là tọa độ xy, 210 200 là kích thước vùng cắt xy
# cắt vùng ảnh thành 1 ảnh mới
cropped_image= img.crop(region)
cropped_image.show()

#dán hình ảnh vừa cut
#xác định vị trí cần dán
paste_position= (250,250)
img.paste(cropped_image,paste_position)   #dán ảnh đã cắt(cropped_image) vào vị trí dán(paste_position)
img.show()
