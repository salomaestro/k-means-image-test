import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

i = 0
while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    a = 40
    for (x, y, w, h) in faces:
        # cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.rectangle(gray, (x - a, y - a), (x + w + a, y + h + a), (0, 0, 255), 2)

    cv2.imshow("img", gray)

    x, y, w, h = faces[0]

    gray = gray[y-a:y+h+a, x - a:x+w+a]

    cv2.imwrite(r"facedetection_test\frame" + str(i) + ".jpg", gray)

    i += 1

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

print("Total of {} frames".format(i))

cap.release()
cv2.destroyAllWindows()
