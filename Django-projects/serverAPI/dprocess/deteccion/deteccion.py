import cv2
import numpy as np

class Detect:
    def __init__(self, url):
        self.url = url

    def imagenVerde(self):
        original = cv2.imread(self.url)
        hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
        #Rango 1, necesitaría ajustarse este valor
        verdeBajo1 = np.array([40,25,20], np.uint8)
        verdeAlto1 = np.array([100,255,255], np.uint8)
        #Máscaras
        mask = cv2.inRange(hsv, verdeBajo1, verdeAlto1)
        maskGreen = cv2.bitwise_and(original, original, mask=mask)
        cv2.imshow('HSV',hsv)
        cv2.imshow('Imagen original',original)
        cv2.imshow('Imagen binarizada',mask)
        cv2.imshow('Imagen segmentada', maskGreen)
        cv2.waitKey()
        #cv2.imwrite("http://127.0.0.1:8000/media/imagenes/"+self.name+"/"+self.name+".png", maskGreen)
        #imgP = cv2.imread("http://127.0.0.1:8000/media/imagenes/"+self.name+"/"+self.name+".png")
        #return imgP