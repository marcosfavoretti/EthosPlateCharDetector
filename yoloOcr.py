import pytesseract
import cv2
from PIL import Image
import numpy as np
from ultralytics import YOLO
class YoloOcr:
    def __init__(self) -> None:
        self.count = 0
        self.yolo: YOLO = YOLO('C:/Users/marco/OneDrive/Documentos/PlatesModelJob/model/best-number.pt')
        
    def ocr(self,mat):
        results = self.yolo(mat, stream=True)
        raw_img = mat.copy()
        for result in results:
            mat = result.plot()
            if len(result.boxes.data) != 0:
                print(result.boxes.data)
            result.save(filename='ResultsLog/okay.jpg')  