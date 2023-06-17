import cv2
import time
# import os
import finger as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


pTime = 0
detector = htm.handDetector(detectionCon=0.95)

tipIds = [4, 8, 12, 16, 20]

gestures = ["Thumbs Up", "NO", "I Love You", "Angry", "Stop","YES"]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)

        cv2.putText(img, gestures[totalFingers - 1], (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    5, (255, 0, 0), 15)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime



    cv2.imshow("Image", img)
    img1=cv2.imread("YES1.png")
    img1=cv2.resize(img1,(400,400))
    cv2.imshow("Image1", img1)
    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break
