import cv2
import numpy as np

video = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier('cascade_caneca3.xml')

while True:
    conectado, frame = video.read()
    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    deteccoes = classificador.detectMultiScale(imagemCinza, scaleFactor=1.3, minNeighbors=9, minSize=(60, 60))
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (8, 0, 255), 2)

        # retângulo hétero: => não considera a rotação do objeto. É enconctrado pela função: cv2.boundingRect()
        # x, y, w, h = cv2.boudingRect (cnt)
        # img = cv2.rectangle = (img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # é basicamente o retângulo que está no laço for acima!

        # retângulo girado: => é desenhado com uma área mínima, ou seja, considera a rotação do objeto.
        # utiliza a função cv2.minAreaReact(). Para desenhá-lo, é preciso ter os 4 cantos do retângulo, que é obtido
        # pela função cv2.boxPoints()
        # rect = cv2. minAreaRect ( CNT )
        # box = cv2.boxPoints (rect)
        # box = np.int0 ( box )
        # im = drawContours (im [ box ], 0, (0, 0, 255), 2)

        # para localizar uma circunferência de um objeto, usa-se a função cv2.minEnclosingCircle()
        # esta função cobre completamente o objeto coma a área mínima.
        # (x, y). radius = minEnclosingCircle (cnt)
        # center = (int (x).int(y))
        # radius = int(radius)
        # img = cv2.circle(img, center, radius, (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()