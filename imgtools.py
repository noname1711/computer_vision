import os
from PIL import Image

#hàm load file, ở py ko dùng {} mà dùng :
def load_image(image_path):
    """
    đọc ảnh từ đường dẫn cho trước và trả về đối tượng ảnh
    Args: image_path:
    :return: đối tượng hình ảnh
    """
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        # nếu lỗi thì in ra
        print("Lỗi khi đọc hình ảnh từ: ", image_path," ",e)
        return None    #lỗi thì phải về none(ko phải về null)
    # try except thì dù đoạn code bị lỗi thì vẫn sẽ được thực thi chứ không crash


def is_image_file(file_path):
    """
    return true nếu là ảnh, false nếu ko phải ảnh
    """
    extensions = (".jpg",".jpeg",".png",".gif",".bmp") #quy định đuôi ntn là ảnh
    return file_path.lower().endswith(extensions)
    #lower() để chuyển về viết thường thì có kthuc như kia thì true

def get_image_list(folder_path):
    #hàm lấy hết ảnh
    image_list =[]
    #ta kiểm tra xem thư mục có tồn tại hay ko và có phải thư mục(isdir) hay ko
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        filenames = os.listdir(folder_path)  #lấy toàn bộ file
        for filename in filenames: #duyệt toàn bộ file
            file_path = os.path.join(folder_path, filename)   #kết nối folder_path vs filename
            if os.path.isfile(file_path) and is_image_file(file_path):
                img = load_image(file_path)
                image_list.append(img)
    return image_list