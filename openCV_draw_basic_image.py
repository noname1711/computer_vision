import cv2
import numpy as np

def display(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyWindow(title)

#tạo 1 ảnh
img = np.zeros((512, 512, 3), np.uint8)   #ảnh toàn điểm 0 nên ảnh sẽ đen hoàn toàn
#vẽ đường thẳng xuất phát từ tọa độ (50,50), end ở tọa độ (350,50), màu là xanh lam mã(255,0,0), độ dày 2
cv2.line(img, (50,50),(350,50), (255,0,0), 2)    
#vẽ hình tròn
cv2.circle(img, (100,100), 50, (0,255,0), -1)
#vẽ hình chữ nhật
cv2.rectangle(img, (100,100), (300,300), (255,0,0), -1)
#ghi text lên hình
content = 'Le Viet Hung'
cv2.putText(img, content, (10, 380), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255),2)   #kích cỡ chữ: 0,6 độ dày 2
display('Image', img)
