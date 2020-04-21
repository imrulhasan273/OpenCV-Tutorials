import cv2
# cap = cv2.VideoCapture("ex.mvi")
cap = cv2.VideoCapture(0)  #device indexing for cemera
# index = 0 (default) or -1
#index = 1(cemera2)/2(cemera3)
#-----Video Writer class-----
#fourcccode website
fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi', fourcc,20.0,(640,480)) #(filename,fourccCode,numberOfFrame,Size)
print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()  #read each frame (scene)
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #width of frame
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #height of frame
        out.write(frame)
        cv2.imshow('frame', frame) #mask : 0xFF for 64bit machine
        #   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #   cv2.imshow('frame', gray) #mask : 0xFF for 64bit machine
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break 
cap.release() #release the video to show
out.release()
cv2.destroyAllWindows()