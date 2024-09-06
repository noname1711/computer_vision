import cv2    #import open CV

#ta có thể tạo 1 hàm để thay cho việc hiển thị ảnh rườm rà
#tuy nhiên như thế này ảnh sẽ hiển thị lần lượt chứ ko cùng lúc
# sử dụng display('base', img) để hiển thị
def display(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(10000)
    cv2.destroyWindow(title)

#đọc một ảnh
path='C:/computer_vision/img/1.png'
img=cv2.imread(path)
#in thông tin ảnh
print(img)           #kết quả là bảng 3 chiều
#lấy kích thước và in ra
print(img.shape)          #(225, 225 , 3)
x, y,z = img.shape
print(x)      #225
print(y)      #225
print(z)      #3
#hiển thị ảnh
display('base', img)
cv2.imshow('hust',img)     #title là hust 
# chờ 1 khoảng thời gian
cv2.waitKey(10000)   # ảnh hiển thị trong 10s
# đóng cửa sổ sau 10s
cv2.destroyWindow('hust')  #đóng cửa sổ tên hust

#tách màu
b,g ,r = cv2.split(img) 
cv2.imshow('base',img)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
# chờ 1 khoảng thời gian 
cv2.waitKey(15000)   # ảnh hiển thị trong 15s 
#cv2.waitKey(0)   # ảnh hiển thị mãi trừ khi user tự bấm 1 phím nào đó
cv2.destroyAllWindows()    #đóng tất cả cửa sổ

# chuyển màu ảnh
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #gõ COLOR_ rồi tự chọn mã màu
img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      # thử mã màu khác
cv2.imshow('base',img)
cv2.imshow('COLOR_BGR2GRAY', gray_img)
cv2.imshow('COLOR_BGR2RGB', img_2)
cv2.waitKey(15000)
cv2.destroyAllWindows()

#tô màu 1 phần ảnh
#thay đổi thông số của điểm ảnh
height, width, z = img.shape
quater_h = height/2
quater_w = width/2
#định nghĩa màu sắc
green_color = (0,255,0)
#copy hình ảnh
img2 = img.copy()
# thay đổi màu góc phần tư bên trái trên của ảnh thành màu xanh lá
#ép kiểu về int vì mặc định là float thì bị lỗi TypeError: 'float' object cannot be interpreted as an integer
for y in range(int(quater_h)):
    for x in range(int(quater_w)):
        img2[y,x] = green_color
#hiển thị
cv2.imshow('base',img)
cv2.imshow('change', img2)
cv2.waitKey(15000)
cv2.destroyAllWindows()