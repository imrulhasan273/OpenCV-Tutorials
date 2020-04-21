import cv2
import numpy as np
from matplotlib import pyplot as plt

#---------------------------------------------
def nothing(x):
    pass

cv2.namedWindow("Tracking") #tracking window
cv2.createTrackbar("TH1", "Tracking", 0, 255, nothing)
cv2.createTrackbar("TH2", "Tracking", 0, 255, nothing)
#--------------------------------------------------------
while True:
    k= cv2.waitKey(1) & 0xFF
    if k==27: #27=escape key
        break

    img = cv2.imread("image/lena.jpg", 0)

    TH1=cv2.getTrackbarPos("TH1","Tracking")
    TH2=cv2.getTrackbarPos("TH2","Tracking")

    # canny = cv2.Canny(img,100,200)
    canny = cv2.Canny(img,TH1,TH2)

    titles = ['image','canny']
    images = [img,canny]

    for i in range(2):
        plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.show()  
    
cv2.destroyAllWindows()