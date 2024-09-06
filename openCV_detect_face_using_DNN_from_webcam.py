import cv2
import numpy as np

#tải mô hình đã được huấn luyện từ trước
net = cv2.dnn.readNetFromCaffe('C:/computer_vision/models/deploy.prototxt',
                               'C:/computer_vision/models/res10_300x300_ssd_iter_140000_fp16.caffemodel')

#mở webcam
cap = cv2.VideoCapture(0)  #cam mặc định
while True: 
    #đọc khung hình từ cam
    ret, frame = cap.read()
    #nếu ko đọc được
    if not ret:
        break

    #chuẩn bị dữ liệu đầu vào
    #1.0 scale ảnh về tỉ lệ 1.0, tức là ảnh ko bị co giãn
    #(300, 300) là kích thước mà mô hình yêu cầu cho đầu vào
    # (104,177,123) màu sắc trung bình
    # swapRB = False ko hoán đổi kênh màu đỏ và xanh
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300,300), (104,177, 123), swapRB= False)

    #đặt dữ liệu đầu vào cho mạng
    net.setInput(blob)

    #chạy mạng để phát hiện khuôn mặt
    #hàm sẽ chạy dần trên ảnh để tìm khuôn mặt
    faces= net.forward()

    #lấy kích thước của ảnh đầu vào
    h = frame.shape[0]
    w = frame.shape[1]

    #duyệt từng khuôn mặt đã được phát hiện 
    for i in range(0, faces.shape[2]):     #vị trí thứ 2 của faces là độ tin cậy
        confidence = faces[0,0, i,2]    #vị trí độ tin cậy
        #kiểm tra xem độ tin cậy có > 0.5 hay không
        if confidence > 0.9:
            #trích xuất tọa độ
            #print(faces[0,0,i,3:7])  # lấy từ pt 3 tới 6
            # đưa tọa độ về số nguyên để dễ vẽ hình chữ nhật
            startx= int(faces[0,0,i,3] *w)
            starty = int(faces[0,0,i,4] * h)
            endx = int(faces[0,0,i,5] * w)
            endy = int(faces[0,0,i,6] * h)
            #print(startx, starty, endx, endy)

            #vẽ hình chữ nhật quanh khuôn mặt đã phát hiện
            cv2.rectangle(frame, (startx, starty), (endx, endy),(0,255,0),2)

            #hiển thị độ tin cậy
            text = 'Face: {:.2f}%'.format(confidence*100)   #2 con số sau dấu ,
            cv2.putText(frame, text, (startx, starty-10), cv2.FONT_HERSHEY_PLAIN,1 ,(255,255,255))

    #hiển thị:
    cv2.imshow('Camera detect face', frame)
    if (cv2.waitKey(10)  == ord('q')):
        break

cap.release()         #giải phóng camera
cv2.destroyAllWindows()