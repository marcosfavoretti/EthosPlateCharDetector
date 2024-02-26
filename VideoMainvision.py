from ultralytics import YOLO
import cv2
import numpy as np
from resolvePlates import ResolvePlates

cap = cv2.VideoCapture(0)
resolve = ResolvePlates()
model = YOLO("./model/best.pt")
# model = model.to('cpu')

while True:
    success, img = cap.read()

    if success:
        # Redimensionar a imagem para 640x640
        img = cv2.resize(img, (640, 640))

        results = model(img)

        # Processar a lista de resultados
        for result in results:
            # Visualizar os resultados no frame
            print(result.boxes.data)
            img = result.plot()
            if len(result.boxes.data) != 0:
                resolve.findPlates(result.boxes.data)
        cv2.imshow("Tela", img)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("desligando")
