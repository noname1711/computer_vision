import cv2
import numpy as np

#tải ảnh đầu vào 
img = cv2.imread('C:/computer_vision/img/nhieu_face.jpg')
#hiển thị ảnh gốc
cv2.imshow('Base image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#tải mô hình đã được huấn luyện từ trước
net = cv2.dnn.readNetFromCaffe('C:/computer_vision/models/deploy.prototxt',
                               'C:/computer_vision/models/res10_300x300_ssd_iter_140000_fp16.caffemodel')

#chuẩn bị dữ liệu đầu vào
#1.0 scale ảnh về tỉ lệ 1.0, tức là ảnh ko bị co giãn
#(300, 300) là kích thước mà mô hình yêu cầu cho đầu vào
# (104,177,123) màu sắc trung bình
# swapRB = False ko hoán đổi kênh màu đỏ và xanh
blob = cv2.dnn.blobFromImage(img, 1.0, (300,300), (104,177, 123), swapRB= False)

#đặt dữ liệu đầu vào cho mạng
net.setInput(blob)

#chạy mạng để phát hiện khuôn mặt
#hàm sẽ chạy dần trên ảnh để tìm khuôn mặt
faces= net.forward()

#lấy kích thước của ảnh đầu vào
h = img.shape[0]
w = img.shape[1]

#in thông tin
print(faces.shape)    #(1, 1, 200, 7)
#1: số lượng ảnh đầu vào, 1: số lượng ảnh đầu ra, 200 khuôn mặt đc phát hiện, 7 thông tin
print(faces[0, 0, 0, ])    #in ra 7 trường thông tin
#[0.         1.         0.99763405 0.45528927 0.71117806 0.5378257
# 0.8057307 ]

#duyệt từng khuôn mặt đã được phát hiện 
for i in range(0, faces.shape[2]):     #vị trí thứ 2 của faces là độ tin cậy
    confidence = faces[0,0, i,2]    #vị trí độ tin cậy
    #kiểm tra xem độ tin cậy có > 0.5 hay không
    if confidence > 0.9:
        #trích xuất tọa độ
        print(faces[0,0,i,3:7])  # lấy từ pt 3 tới 6
        # đưa tọa độ về số nguyên để dễ vẽ hình chữ nhật
        startx= int(faces[0,0,i,3] *w)
        starty = int(faces[0,0,i,4] * h)
        endx = int(faces[0,0,i,5] * w)
        endy = int(faces[0,0,i,6] * h)
        print(startx, starty, endx, endy)

        #vẽ hình chữ nhật quanh khuôn mặt đã phát hiện
        cv2.rectangle(img, (startx, starty), (endx, endy),(0,255,0),2)

        #hiển thị độ tin cậy
        text = 'Face: {:.2f}%'.format(confidence*100)   #2 con số sau dấu ,
        cv2.putText(img, text, (startx, starty-10), cv2.FONT_HERSHEY_PLAIN,1 ,(255,255,255))

#hiển thị ảnh:
cv2.imshow('Image detect face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()