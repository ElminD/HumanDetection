import cv2
import numpy as np




face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
upperbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')



def process(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 25)
    img_canny = cv2.Canny(img_blur, 5, 50)
    kernel = np.ones((3, 3))
    img_dilate = cv2.dilate(img_canny, kernel, iterations=4)
    img_erode = cv2.erode(img_dilate, kernel, iterations=1)
    return img_erode

def get_contours(img, img_original):
    img_contours = img_original.copy()
    contours, hierarchies = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), -1) 

    return img_contours

cap = cv2.VideoCapture(0)


success, img1 = cap.read()
success, img2 = cap.read()
heat_map = np.zeros(img1.shape[:-1])

while success:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    upperbodys = upperbody_cascade.detectMultiScale(gray, 1.1, 5)
    for(x, y, w, h) in upperbodys:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,255), 2)
    bodys = body_cascade.detectMultiScale(gray, 1.1, 5)
    for(x, y, w, h) in bodys:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
            

    cv2.imshow('frame', frame)
    
    

    diff = cv2.absdiff(img1, img2)
    img_contours = get_contours(process(diff), img1)

    heat_map[np.all(img_contours == [0, 255, 0], 2)] += 3 # The 3 can be tweaked depending on how fast you want the colors to respond
    heat_map[np.any(img_contours != [0, 255, 0], 2)] -= 3
    heat_map[heat_map < 0] = 0
    heat_map[heat_map > 255] = 255

    img_mapped = cv2.applyColorMap(heat_map.astype('uint8'), cv2.COLORMAP_JET)



    cv2.imshow("Original", img1)
    cv2.imshow("Heat Map", img_mapped)
    
    
    img1 = img2
    success, img2 = cap.read()
    
    if cv2.waitKey(1) == ord('q'):
        break