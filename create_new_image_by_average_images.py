import numpy as np
from PIL import Image

#xây dựng hàm tính trung bình ảnh
def average_images(image_list):          #hàm nhập vào 1 danh sách ảnh
    total_array = np.array(Image.open(image_list[0]), 'f')   #ban đầu total_array là ảnh đầu tiên
    count= 1    #biến chỉ số lượng ảnh
    for image_path in image_list[1:]:
        try:
            image_array = np.array(Image.open(image_path),'f')
            #'f' là tham số chỉ định kiểu dữ liệu của các phần tử trong mảng NumPy.
            #'f' là viết tắt của float32, tức là mỗi giá trị pixel trong mảng sẽ được lưu trữ dưới dạng số thực (32-bit floating-point).
            #Kiểu float32 thường được dùng khi cần thực hiện các phép tính toán có độ chính xác cao trên các giá trị pixel (ví dụ như xử lý ảnh phức tạp hoặc áp dụng các bộ lọc ảnh).
            total_array += image_array   #cộng hết phần tử trên mảng lại với nhau
            count += 1
        except:
            print("Skip ", image_path)

    average_array= total_array/count    #tính trung bình
    average_image = Image.fromarray(average_array.astype('uint8'))     #chuyển đổi kết quả trung bình thành hình ảnh
    return average_image

#sử dụng hàm
#lấy 2 ảnh cùng kích cỡ
my_path_1 = 'C:/computer_vision/img/1.png'
my_path_2 = 'C:/computer_vision/img/2.png'
image_list = [my_path_1,my_path_2]    #danh sách ảnh tính trung bình
result_image = average_images(image_list)
result_image.show()