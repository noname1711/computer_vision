from PIL import Image
from IPython.display import display  #thư viện IPython để dùng display
#import imgtools.py vừa code và lấy mọi phương thức = *
from imgtools import *

my_path = 'C:/computer_vision/img/hust.jpg'
img = load_image(my_path)

#chuyển từ ảnh RGB sang ảnh xám
gray_image= img.convert("L")   #L là dạng ảnh xám
gray_image.show()

#phân RGB thành 3 tầng màu khác nhau
#lưu ý ko hiểu nhầm tách màu sẽ ra đỏ, xanh hoàn toàn mà chỉ là màu tầng khác nhau(độ đậm khác nhau)
red_band, green_band, blue_band = img.split()
red_band.show()
green_band.show()
blue_band.show()


#trộn ảnh
#khi trộn 3 ảnh trên vào sẽ ra ảnh ban đầu( ảnh gốc có màu)
merge_image = Image.merge("RGB",(red_band,green_band, blue_band))
merge_image.show()