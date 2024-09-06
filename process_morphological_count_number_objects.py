import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image

my_path = 'C:/computer_vision/img/dem.jpg'
im= Image.open(my_path)
gray_image = im.convert('L')    #chuyển về ảnh xám
image_array = np.array(gray_image)    #chuyển sang mảng

#chuyển sang ảnh nhị phân
binary_image = 1*(image_array>200)    #điểm nào lớn hơn 200 thì quay về 1, ngược lại thì về 0 -> vật thể thành đen, nền trắng
#ngược lại, nếu 1*(image_array<200) thì vật thể trắng nền đen
#mốc 200 có thể thay đổi theo ý mình

#thực hiện opening để loại bỏ nhiễu và nối các đối tượng
#thực hiện closing thì là binary_closing
opened_image = ndimage.binary_opening(binary_image, structure = np.ones((3,3)))
#sử dụng cấu trúc 3x3 để thực hiện, tất nhiên cấu trúc này là tùy mình quy định, ví dụ 9,5
#ta sẽ tùy chỉnh cấu trúc sao cho chính xác nhất

#đánh nhãn
labeled_image, num_features = ndimage.label(binary_image)
#đánh nhãn ảnh sau khi thực hiện opening
labeled_opening_image, num_opening_features = ndimage.label(opened_image)

#tạo lưới subplot với 3 dòng và 1 cột
fig, axs = plt.subplots(2, 2, figsize=(50, 50))
# ảnh xám
axs[0, 0].imshow(gray_image, cmap='gray')
axs[0, 0].set_title('Ảnh xám')
#hình ảnh nhị phân
axs[0, 1].imshow(binary_image, cmap='gray')
axs[0, 1].set_title('Hình ảnh nhị phân')
#hình ảnh đã đánh nhãn
axs[1, 0].imshow(labeled_image, cmap='nipy_spectral')   #nipy_spectral tô mỗi đối tượng 1 màu
axs[1, 0].set_title(f'Hình ảnh đã đánh nhãn {num_features} đối tượng')
# f'Hình ảnh... thể hiện num_features là kiểu float
#hình ảnh sau khi thực hiện opening đã đánh nhãn
axs[1, 1].imshow(labeled_opening_image, cmap='nipy_spectral')   #nipy_spectral tô mỗi đối tượng 1 màu
axs[1, 1].set_title(f'Hình ảnh sau opening đã đánh nhãn {num_opening_features} đối tượng')
plt.show()