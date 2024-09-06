import cv2
import time #phải import để lấy time

#đọc video từ cam
cam = cv2.VideoCapture(0)    # số 0 là cam đầu tiên trên máy tính
# nếu nhiều camera thì thay 1,2,... ứng với số cam

#tạo cửa sổ để hiển thị
cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)
interval =5 # đặt biến thể hiện cứ 5s (5 khung hình) thì lưu ảnh xuống
count = 0

# định nghĩa 1 số thông số của text để hiển thị fps:
font = cv2.FONT_HERSHEY_SIMPLEX
font_color= (255, 255, 255)
font_scale = 1
font_thickness = 2

#hiển thị từng khung ảnh
while True:
    #thời gian trước khi đọc 1 ảnh
    start_time = time.time()

    #đọc 1 frame (đọc từng khung hình một)
    ret, frame = cam.read()
    #nếu không thể đọc frame nào nữa thì thoát
    if not ret:
        break

    #tăng count lên nếu count chia hết cho 5 thì lưu xuống một cách định kì
    count +=1
    if (count% interval ==0):
        # lưu ảnh xuống đường dẫn
        cv2.imwrite(f'C:/computer_vision/img/image_{count}.jpg', frame)

    #thời gian sau khi đọc 1 ảnh
    end_time = time.time()

    # tính fps
    fps = 1/(end_time - start_time) 

    #ghi số lượng fps
    cv2.putText(frame, f'FPS: {fps:.2f}', (10,30), font, font_scale, font_color, font_thickness)
    #hiển thị
    cv2.imshow('Video Player', frame)
    ## khi nào hết video (10s) hoặc gõ q-> enter thì thoát
    if (cv2.waitKey(10)== ord('q')):    
        break
#hủy bỏ player
cam.release()   #ko đọc video đó nữa
cv2.destroyAllWindows()
