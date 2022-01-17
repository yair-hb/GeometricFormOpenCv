from ssl import ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION
import cv2
import numpy as np 

def figColor (imgHSV):
    #para el color rojo
    rojoBajo1= np.array([0,100,20], np.uint8)
    rojoAlto1= np.array([10,255,255],np.uint8)
    rojoBajo2= np.array([175,100,20], np.uint8)
    rojoAlto2=  np.array([180,255,255], np.uint8)

    #naranja
    naranjaBajo= np.array([11,100,20], np.uint8)
    naranjaAlto= np.array([19,255,255], np.uint8)

    #amarillo
    amarilloBajo= np.array([20,10,20], np.uint8)
    amarilloAlto= np.array([19,255,255], np.uint8)

    #verde
    verdeBajo= np.array([36,100,20], np.uint8)
    verdeAlto= np.array([70,255,255], np.uint8)

    #violeta
    violetaBajo= np.array([130,100,20], np.uint8)
    violetaAlto= np.array([145,255,255], np.uint8)

    #rosa
    rosaBajo= np.array([146,100,20], np.uint8)
    rosaAlto= np.array([170,255,255], np.uint8)

    maskRojo1= cv2.inRange(imgHSV,rojoBajo1,rojoAlto1)
    maskRojo2= cv2.inRange(imgHSV, rojoBajo2,rojoAlto2)
    maskRojo= cv2.add(maskRojo1,maskRojo2)
    maskNaranja= cv2.inRange(imgHSV,naranjaBajo, naranjaAlto)
    maskAmarillo= cv2.inRange(imgHSV,amarilloBajo,amarilloAlto)
    maskVerde= cv2.inRange(imgHSV, verdeBajo, verdeAlto)
    maskVioleta= cv2.inRange(imgHSV,violetaBajo,violetaAlto)
    maskRosa= cv2.inRange(imgHSV, rosaBajo,rosaAlto)

    cntsRojo= cv2.findContours(maskRojo,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsNaranja= cv2.findContours(maskNaranja,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsAmarillo= cv2.findContours(maskAmarillo,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsVerde= cv2.findContours(maskVerde,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsVioleta= cv2.findContours(maskVioleta,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsRosa= cv2.findContours(maskRosa,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

    if len(cntsRojo) >0: 
        color = 'Rojo'
    if len(cntsNaranja) >0:
        color = 'Naranja'
    if len (cntsAmarillo)>0:
        color = 'Amarillo'
    if len (cntsVerde) >0: 
        color = 'Verde'
    if len (cntsVioleta) >0:
        color = 'Violeta'
    if len (cntsRosa) >0:
        color = 'Rosa'

    return color

def figNombre (contorno,width, height):
    epsilon = 0.01*cv2.arcLength(contorno, True)
    approx = cv2.approxPolyDP(contorno,epsilon,True)

    if len(approx) == 3:
        figNombre = 'Triangulo'

    if len(approx) == 4:
        aspect_ratio = float(width)/height
        if aspect_ratio == 1:
            figNombre = 'Cuadrado'
        else:
            figNombre = 'Rectangulo'
    
    if len (approx) == 5:
        figNombre = 'Pentagono'
    
    if len(approx) == 6:
        figNombre = 'Hexagono'

    if len(approx) >10:
        figNombre = 'Circulo'

    return figNombre

imagen = cv2.imread('figuras.png')
imGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(imGris, 10,150)
canny = cv2.dilate(canny,None, iterations=1)
canny = cv2.erode(canny, None,iterations=1)
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL,  cv2.CHAIN_APPROX_SIMPLE)
imgHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    imAux = np.zeros(imagen.shape[:2], dtype="uint8")
    imAux = cv2.drawContours(imAux, [c], -1, 255,-1)
    maskHSV = cv2.bitwise_and(imgHSV,imgHSV, mask=imAux)
    nombre = figNombre(c,w,h)
    color = figColor(maskHSV)
    colorNombre = nombre + ' ' + color
    cv2.putText(imagen, colorNombre, (x,y-5),1,0.8,(0,255,0),1)
    cv2.imshow('imagen', imagen)
    cv2.waitKey(0)
