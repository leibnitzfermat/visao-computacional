import cv2
import mediapipe as mp

#video = cv2.VideoCapture("rtsp://leibnitz:leibnitz@192.168.1.7/stream1")
video = cv2.VideoCapture(0)


hand = mp.solutions.hands
hands = hand.Hands(max_num_hands = 2)

mpDraw = mp.solutions.drawing_utils


while True:
    success, img = video.read()
    frameRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []
    if handPoints:
        for points in handPoints:
            mpDraw.draw_landmarks(img, points)
            #podemos enumerar esses pontos da seguinte forma
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                #cv2.putText(img, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                pontos.append((cx,cy))

            dedos = [8,12,16,20]
            contador = 0
            if pontos:
                if pontos[4][0] < pontos[3][0]:
                    contador += 1
                for x in dedos:
                   if pontos[x][1] < pontos[x-2][1]:
                       contador +=1

            cv2.rectangle(img, (80, 10), (200,110), (255, 0, 0), -1)
            cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)
            #print(contador)

    cv2.imshow('Imagem',img)
    cv2.waitKey(1)
