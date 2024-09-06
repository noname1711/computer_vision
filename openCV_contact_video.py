import cv2
import time #phải import để lấy time

#đọc video từ file
my_video = cv2.VideoCapture('C:/computer_vision/vid/video.mp4')
#tạo cửa sổ để hiển thị
cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)

# định nghĩa 1 số thông số của text để hiển thị fps:
font = cv2.FONT_HERSHEY_SIMPLEX
font_color= (255, 255, 255)
font_scale = 5     #chữ to hơn 5 lần so với cỡ chữ mặc định của font hershey_simplex
font_thickness = 2

#hiển thị từng khung ảnh
while True:
    #thời gian trước khi đọc 1 ảnh
    start_time = time.time()

    #đọc 1 frame (đọc từng khung hình một)
    ret, frame = my_video.read()
    #nếu không thể đọc frame nào nữa thì thoát
    if not ret:
        break

    #thời gian sau khi đọc 1 ảnh
    end_time = time.time()

    # tính fps
    fps = 1/(end_time - start_time) 

    #ghi số lượng fps
    cv2.putText(frame, f'FPS: {fps:.2f}', (10,150), font, font_scale, font_color, font_thickness)
    #hiển thị
    cv2.imshow('Video Player', frame)
    ## khi nào hết video (10s) hoặc gõ q-> enter thì thoát
    if (cv2.waitKey(10)== ord('q')):    
        break
#hủy bỏ player
my_video.release()   #ko đọc video đó nữa
cv2.destroyAllWindows()
