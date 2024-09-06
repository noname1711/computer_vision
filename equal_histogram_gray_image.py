import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def histogram_equalization(image, nbr_bins=256):
    # Đảm bảo rằng ảnh đầu vào là ảnh xám (grayscale).
    # Nếu ảnh không phải là ảnh xám (chế độ màu 'L'), thì chuyển đổi nó thành ảnh xám.
    # Ảnh xám có các giá trị pixel từ 0 (màu đen) đến 255 (màu trắng).
    if image.mode != 'L':
        image = image.convert('L')
    
    # Chuyển đổi hình ảnh từ định dạng của thư viện PIL thành một mảng numpy.
    # Mảng này chứa các giá trị pixel của ảnh, mỗi giá trị là một số nguyên từ 0 đến 255.
    image_array = np.array(image)
    
    # Tính toán histogram của ảnh.
    # Histogram là một biểu đồ biểu diễn sự phân bố tần suất của các giá trị pixel trong ảnh.
    # Hàm np.histogram() trả về hai giá trị: 
    #   - 'histogram': chứa số lượng pixel ở mỗi mức độ xám (trong khoảng từ 0 đến 255).
    #   - 'bins': là các khoảng giá trị tương ứng với mỗi bin trong histogram (ở đây chia làm 'nbr_bins' bin).
    histogram, bins = np.histogram(image_array, bins=nbr_bins, range=(0, 256), density=True)
    
    # Tính toán hàm phân phối tích lũy (CDF) từ histogram.
    # CDF cho biết xác suất tích lũy rằng một pixel sẽ có giá trị nhỏ hơn hoặc bằng một giá trị nhất định.
    # Hàm cumsum() tính tổng tích lũy của histogram, tức là cộng dồn các giá trị lại với nhau.
    cdf = histogram.cumsum()
    
    # Chuẩn hóa CDF để các giá trị nằm trong khoảng từ 0 đến 255 (tương ứng với mức độ xám trong ảnh).
    # Việc chuẩn hóa này đảm bảo rằng khi áp dụng CDF lên ảnh, giá trị pixel mới cũng sẽ nằm trong khoảng từ 0 đến 255.
    cdf = 255 * cdf / cdf[-1]  # cdf[-1] là giá trị cuối cùng của CDF, tương đương với tổng số pixel trong ảnh.
    
    # Ánh xạ các giá trị pixel ban đầu trong 'image_array' sang các giá trị mới dựa trên CDF.
    # Hàm np.interp() thực hiện nội suy (interpolation) để tìm giá trị mới cho từng pixel dựa trên bins và CDF.
    # 'bins[:-1]' là các giá trị bin trừ đi giá trị cuối cùng (vì bins có nhiều hơn một phần tử so với histogram).
    image_equalized = np.interp(image_array, bins[:-1], cdf)
    
    # Chuyển đổi mảng numpy sau khi cân bằng histogram thành một hình ảnh.
    # Hàm astype('uint8') chuyển đổi các giá trị pixel về kiểu số nguyên 8 bit (giá trị từ 0 đến 255).
    image_equalized = Image.fromarray(image_equalized.astype('uint8'))
    
    # Trả về hình ảnh đã được cân bằng histogram.
    return image_equalized


my_path = 'C:/computer_vision/img/sang.jpg'
im = Image.open(my_path)
# áp dụng cân bằng lược đồ ảnh xám
equalized_image = histogram_equalization(im)
# tạo một lưới 2x2 để hiển thị hình ảnh và biểu đồ
plt.figure(figsize=(15,10))
#hiển thị ảnh gốc
plt.subplot(2,2,1)
plt.imshow(im.convert('L'), cmap='gray')
plt.title('Ảnh gốc')
# vẽ biểu đồ histogram của ảnh gốc
plt.subplot(2,2,2)
plt.hist(np.array(im.convert('L')).flatten(), bins= 128)
plt.title('Histogram ảnh gốc')
#hiển thị ảnh sau khi cân bằng
plt.subplot(2,2,3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Ảnh đã cân bằng' )
#vẽ biểu đồ histogram của hình ảnh đã cân bằng
plt.subplot(2,2,4)
plt.hist(np.array(equalized_image).flatten(), bins= 128)
plt.title('Histogram ảnh đã cân bằng')

plt.show()