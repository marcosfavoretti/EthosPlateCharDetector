from ultralytics import YOLO
from resolvePlates import ResolvePlates
class PlatesDetector:
    def __init__(self) -> None:
        self.model = YOLO("C:/Users/marco/OneDrive/Documentos/PlatesModelJob/model/best.pt")
        self.resolve =  ResolvePlates()

    
    def roiPlates(self, picture):
        results = self.model(picture, stream=True)
        raw_img = picture.copy()
        for result in results:
            picture = result.plot()
            if len(result.boxes.data) != 0:
                self.resolve.findPlates(raw_img,result.boxes.data)
            result.save(filename='ResultsLog/result.jpg')  
        