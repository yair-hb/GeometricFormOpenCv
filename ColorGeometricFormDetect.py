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



