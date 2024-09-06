import cv2
import time

# hàm để hiển thị
def display(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(10000)
    cv2.destroyWindow(title)

def detect(img):
    #khởi tạo Haar cascade classifier cho nhận diện khuôn mặt và mắt có đeo kính
    face_cascade = cv2.CascadeClassifier('C:/computer_vision/data/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('C:/computer_vision/data/haarcascade_eye_tree_eyeglasses.xml')
    #chuyển ảnh sang màu xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #tìm khuôn mặt
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize=(30,30))             #nhận diện nhiều ảnh cùng 1 lúc
    #scaleFactor kéo dãn, minNeighbors k/c gần nhất, minSize = kích cỡ mặt min
    #tìm mắt
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1, minSize=(5,5))             #nhận diện nhiều ảnh cùng 1 lúc
    #vẽ hộp chứa khuôn mặt
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
    #vẽ hộp chứa mắt
    for (x,y,w,h) in eyes:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    #trả về ảnh 
    return img

#đọc ảnh
img = cv2.imread('C:/computer_vision/img/kinh.jpg')

#hiển thị ảnh 
display('Face Detection', detect(img))



# nhận diện từ video 
my_video = cv2.VideoCapture(0)
#tạo cửa sổ để hiển thị
cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)

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
    ret, frame = my_video.read()
    #nếu không thể đọc frame nào nữa thì thoát
    if not ret:
        break

    #thời gian sau khi đọc 1 ảnh
    end_time = time.time()

    # tính fps
    fps = 1/(end_time - start_time) 
    # detect khuôn mặt và mắt
    frame = detect(frame)

    #ghi số lượng fps
    cv2.putText(frame, f'FPS: {fps:.2f}', (10,30), font, font_scale, font_color, font_thickness)
    #hiển thị
    cv2.imshow('Video Player', frame)
    ## khi nào hết video (10s) hoặc gõ q-> enter thì thoát
    if (cv2.waitKey(10)== ord('q')):    
        break
#hủy bỏ player
my_video.release()   #ko đọc video đó nữa
cv2.destroyAllWindows()