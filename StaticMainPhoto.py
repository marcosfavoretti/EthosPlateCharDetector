from ultralytics import YOLO
from resolvePlates import ResolvePlates
from ocr import Ocr
import cv2
def main():
    path = "C:/Users/marco/OneDrive/Documentos/PlatesModelJob/20240221_164410.jpg"
    img = cv2.imread(path) 
    raw_image = img.copy()
    model = YOLO("C:/Users/marco/OneDrive/Documentos/PlatesModelJob/model/best.pt")
    resolve = ResolvePlates()
    results = model(img, stream=True)
    for result in results:
        img = result.plot()
        if len(result.boxes.data) != 0:
            resolve.findPlates(raw_image,result.boxes.data)
        result.save(filename='ResultsLog/result.jpg')  
    
    ocr = Ocr()
    ocr.readChars(resolve.plates)

    

if __name__ == "__main__":
    main()