# Face detection

import cv2

# loading xml file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# capturing video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # converting into grayScale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # scan and detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)    
    # 1.1 is balanced(not too slow & blind)
    # 5 means --> minNeighbors (5 clues needed to say a face)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
        # (x,y) --> top-left corner of the face
        # (x+w, y+h) --> bottom-right corner of the face

    cv2.imshow('Webcam Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



