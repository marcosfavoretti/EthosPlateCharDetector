import cv2
from Platesdetector import PlatesDetector

class Camera:
    def __init__(self) -> None:
        self.detector = PlatesDetector()
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
        self.detector.roiPlates(img)