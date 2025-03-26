import cv2

cap = cv2.VideoCapture('parking1.mp4')

ret, frame = cap.read()

frame = cv2.resize(frame, (1020,500))

if ret:
    rois = cv2.selectROI('select rois', frame, showCrosshair=True, fromCenter=False)
    cv2.destroyAllWindows()

    # Print ROI coordinates
    print("Selected ROIs (x, y, width, height):", list(rois))

'''
[2, 366, 25, 66]
[43, 363, 41, 73]
[96, 362, 46, 67]
[151, 360, 53, 66]
[212, 359, 59, 61]
[269, 351, 70, 64]
[332, 349, 77, 53]
[397, 344, 79, 52]
[467, 338, 67, 55]
[516, 333, 71, 48]
[567, 329, 77, 44]
[632, 321, 55, 45]
[669, 309, 84, 42]
'''