from labels import label
from plate import Plate
from typing import List
import cv2
class ResolvePlates:
    def __init__(self):
        self.plates: List[Plate] = []

    def findPlates(self,image_raw,dataArray):
        print("looking for plates")
        for predict in dataArray:
            if label[int(predict[-1])] == 'plate':
                # print('plate found',predict)
                plate = Plate()
                [x1_m,y1_m,x2_m,y2_m,prob_m,classe_m] = predict
                plate.plate = predict
                # print(int(x1_m),int(y1_m),int(x2_m),int(y2_m))
                for someResult in dataArray:
                    [x1,y1,x2,y2,prob,classe] = someResult
                    # print(int(x1),int(y1),int(x2),int(y2))

                    if (int(x1_m)<int(x1) and int(x2_m)>int(x2)) and (int(y1_m)<int(y1) and int(y2_m)>int(y2)):
                        # print('sub plate')
                        if classe == 0:#class de maintext
                            plate.maintext = someResult
                            # print('achou um main text')
                        elif classe == 2:#classe de subtext
                            plate.subtext = someResult
                            # print('achou um subtext')
                self.plates.append(plate)
        print('end of process plates, %d plates found' %len(self.plates) )
        for plate in self.plates:
            plate.saveRecort(image_raw)
            plate.ocrLabels()

        