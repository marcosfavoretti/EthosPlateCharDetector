import cv2
from ocr import Ocr
class Plate:
    def __init__(self):#passar tudo por parametro do contrutor !melhora
        self.plate = None
        self.maintext = None
        self.subtext = None
        self.filePath = None
        self.ocr = Ocr()
        self.fatherImage = None
    
    def saveRecort(self,img_raw):
        self.fatherImage = img_raw
        tensor = self.plate.cpu().numpy()
        interact_img = img_raw.copy()
        array_converted = tensor.tolist()  # convertendo para lista Python se necessário
        plate_recort = interact_img[int(array_converted[1]):int(array_converted[3]),int(array_converted[0]):int(array_converted[2])]
        self.filePath = "ResultsLog/plates/plate%d.png"  %int(self.plate[0])
        cv2.imwrite("ResultsLog/plates/plate%d.png" %int(self.plate[0]), plate_recort)

    def ocrLabels(self):
        if not self.isvalidPlate(): return
        mainText = self.maintext.cpu().numpy()
        subText = self.subtext.cpu().numpy()
        posmainText = mainText.tolist()  # convertendo para lista Python se necessário
        posSubText = subText.tolist()  # convertendo para lista Python se necessário
        maintText_output =self.ocr.ocr(self.fatherImage[int(posmainText[1]):int(posmainText[3]),int(posmainText[0]):int(posmainText[2])])
        subText_output=self.ocr.ocr(self.fatherImage[int(posSubText[1]):int(posSubText[3]),int(posSubText[0]):int(posSubText[2])])

        print('saidas\nmainText: %s\nsubtext: %s' % (maintText_output, subText_output))
        
    def isvalidPlate(self)-> bool:
        if self.maintext ==None or self.subtext == None:
            return False
        return True