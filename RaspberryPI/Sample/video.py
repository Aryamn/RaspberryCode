import cv2

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    frame = cv2.resize(frame , None , fx = 0.5 , fy = 0.5 , interpolation=cv2.INTER_AREA)
    image = cv2.imencode('.jpg', frame)[1].tostring() 
    print(len(image))
    cv2.imshow('Input' , frame)

    c = cv2.waitKey(1)
    if c==27:
        break

cap.release()
cv2.destroyAllWindows()