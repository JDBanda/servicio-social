#Importar OpenCV
import cv2
#Importar numpy
import numpy as np
#Importar matplotlib
import matplotlib.pyplot as plt
#Asignar la lectura de la imagen a una variable
img = cv2.imread('img/plaga_maiz.png')
#Convertir de BGR a RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Convertir de RGB a HSV
hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2HSV)
#Mostrar gráfica
#plt.imshow(hsv_img)
#plt.show()
#Rangos 0,72,0 a 147,255,175
verde_obscuro = [0,72,0]
verde_claro = [150, 255, 100]
#Definiendo el rango a la máscara 
mask = cv2.inRange(hsv_img, np.float32(verde_obscuro), np.float32(verde_claro))
#resultado
result = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()
cv2.imshow('',hsv_img);
cv2.waitKey