import numpy as np
import cv2

cap = cv2.VideoCapture('parking1.mp4')

parking_lots = [
[2, 366, 25, 66],
[43, 363, 41, 73],
[96, 362, 46, 67],
[151, 360, 53, 66],
[212, 359, 59, 61],
[269, 351, 70, 64],
[332, 349, 77, 53],
[397, 344, 79, 52],
[467, 338, 67, 55],
[516, 333, 71, 48],
[567, 329, 77, 44],
[632, 321, 55, 45],
[669, 309, 84, 42]]

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break
        
    frame=cv2.resize(frame,(1020,500))

    #image preprocessing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_thrsh= cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    blurred = cv2.medianBlur(img_thrsh, 5)
    kernel = np.ones((3,3), np.int8)
    dil = cv2.dilate(blurred, kernel)

    #number of parking lots
    n_spots = 0

    for x,y,w,h in parking_lots:
        cut = dil[y:y+w,x:x+h]
        qnt_white_pixels = cv2.countNonZero(cut)
        cv2.putText(frame,str(qnt_white_pixels),(x, y+h-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
        # cv2.putText(dil,str(qnt_white_pixels),(x, y+h-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)

        # cv2.rectangle(frame,(x,y), (x+h,y+w), (0,255,0),3)

        if qnt_white_pixels > 1000:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            n_spots +=1

    
    cv2.rectangle(frame,(90,0),(415,60),(255,0,0),-1)
    cv2.putText(frame,f'LIVRE: {n_spots}/13',(95,45),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),5)


    cv2.imshow('video', frame)
    # cv2.imshow('video2', dil)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()