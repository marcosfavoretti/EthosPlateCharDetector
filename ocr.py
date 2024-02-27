import pytesseract
import cv2
from PIL import Image
import numpy as np
class Ocr: 
    def __init__(self):
        self.count = 0
    
    def ocr(self, mat):
        image = np.array(mat, dtype=np.uint8)  # Exemplo de matriz 3x3 como imagem (BGR)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
        #pre processamento de img
        
        # Aplica binarização (opcional, dependendo da qualidade da imagem)
        _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        cv2.imwrite('ResultsLog/debug%d.png' %self.count, binary_image)
        whitelist = '0123456789'
        self.count+=1
        text = pytesseract.image_to_string(image=binary_image,config=f'--psm 6 -c tessedit_char_whitelist={whitelist}')
        return text