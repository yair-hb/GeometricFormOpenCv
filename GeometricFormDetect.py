import cv2

imagen = cv2.imread('figuras.png')
imGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#se usa el metodo canny para deteccion de bordes en las imagenes 
canny = cv2.Canny(imGris, 10,150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny,None,iterations=1)
#se puede utilizar el metodo de umbralizacion simple en vez de CANNY
#_,th = cv2.threshold(imGris,10,255, cv2.THRESH_BINARY)

cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    epsilon = 0.01*cv2.arcLength(c,True)
    approx =  cv2.approxPolyDP(c,epsilon,True)
    print (len(approx))
    x,y,w,h = cv2.boundingRect(approx)

if len (approx) ==3:
    cv2.putText(imagen, 'Triangulo',(x,y-5),1,1.5(0,255,0),2)

if len (approx) == 4:
    aspect_ratio = float(w)/h
    print ('aspectRatio = ', aspect_ratio)
    if aspect_ratio == 1:
        cv2.putText(imagen,'Cuadrado',(x,y-5),1,1.5,(0,255,0),2)
    else:
        cv2.putText(imagen, 'Rectangulo',(x,y-5),1,1.5,(0,255,0),2)

if len(approx)==5:
    cv2.putText(imagen,'Pentagono',(x,y-5),1,1.5,(0,255,0),2)

if len(approx)==6:
    cv2.putText(imagen,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
    

cv2.imshow('IMAGEN DE ENTRADA',imagen)
cv2.imshow('METODO CANNY', canny)
#Se usa para mostrar la umbralizacion simple en caso de haberlo usao
#cv2.imshow('UMBRALIZACION SIMPLE', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
