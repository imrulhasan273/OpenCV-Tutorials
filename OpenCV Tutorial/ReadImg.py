#Show Image (VS Code)
#For any IDE below is ok
import cv2
img=cv2.imread('obama.jpg', 0)  
cv2.imshow('image', img)  #As per title cv2.imshow(img) is crashing the server.
cv2.waitKey(0)
cv2.destroyAllWindows()