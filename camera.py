import cv2
from ocr import Ocr
from ultralytics import YOLO
from resolvePlates import ResolvePlates
class Camera:
    def cameraStart(self):
        cam = cv2.VideoCapture(0)
        while True:
            success ,img = cam.read()
            if success:
                cv2.imshow('camera',img)
                k = cv2.waitKey(1)
                if k == ord('q'):
                    break
                elif k == ord('p'):
                    self.takeShot(img=img)
                    cv2.destroyWindow('camera')
        
    def takeShot(self, img):
        model = YOLO("C:/Users/marco/OneDrive/Documentos/PlatesModelJob/model/best.pt")
        resolve = ResolvePlates()
        results = model(img, stream=True)
        raw_img = img.copy()
        for result in results:
            img = result.plot()
            if len(result.boxes.data) != 0:
                resolve.findPlates(raw_img,result.boxes.data)
            result.save(filename='ResultsLog/result.jpg')  
        