from PIL import Image

#thư mục chứa hình ảnh
dir = 'C:/computer_vision/img'

#đường dẫn đến hình ảnh
image_path = dir + '/hust.JPG'
print(image_path)

#sử dụng Image.open() để đọc ảnh
img01 = Image.open(image_path)

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
