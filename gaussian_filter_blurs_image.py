from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

image_path = 'C:/computer_vision/img/hust.jpg'
image = Image.open(image_path)
gray_image = image.convert('L')   # Chuyển ảnh sang ảnh xám để dễ quan sát độ mờ
image_a = np.array(gray_image)     # Chuyển ảnh xám thành mảng

# Làm mờ ảnh với bộ lọc Gauss với các giá trị sigma khác nhau
blurred_image_a = ndimage.gaussian_filter(image_a, sigma=1, mode="constant")
blurred_image_b = ndimage.gaussian_filter(image_a, sigma=3, mode="constant")
blurred_image_c = ndimage.gaussian_filter(image_a, sigma=5, mode="constant")

# Hiển thị ảnh bằng cách sử dụng subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Hiển thị ảnh gốc xám
axs[0, 0].imshow(gray_image, cmap='gray')
axs[0, 0].set_title('Ảnh xám gốc')

# Hiển thị các ảnh mờ với các giá trị sigma khác nhau
axs[0, 1].imshow(blurred_image_a, cmap='gray')
axs[0, 1].set_title('Ảnh mờ sigma = 1')

axs[1, 0].imshow(blurred_image_b, cmap='gray')
axs[1, 0].set_title('Ảnh mờ sigma = 3')

axs[1, 1].imshow(blurred_image_c, cmap='gray')
axs[1, 1].set_title('Ảnh mờ sigma = 5')

# Điều chỉnh bố cục và hiển thị hình ảnh
plt.tight_layout()  #đảm bảo các subplots sẽ không bị chồng chéo và khớp vừa vặn trong cửa sổ figure
plt.show()
