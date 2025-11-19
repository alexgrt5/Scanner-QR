import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

# Acceder a la camara web
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# Lectura de marcos
while True:
    ret,frame = cap.read()

    # Lectura de datos del código de barras
    for barcode in decode(frame):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)

        # Dibujar un rectangulo alrededor del código QR y mostrar los datos
        pts = np.array([barcode.polygon],np.int32)
        cv.polylines(frame,[pts],True,(255,0,0),5)
        pts2 = barcode.rect
        cv.putText(frame,myData,(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    # Mostramos el marco
    cv.imshow('In', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break 

    #Code create by alexgrt5