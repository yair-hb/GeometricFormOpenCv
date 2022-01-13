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


cv2.imshow('IMAGEN DE ENTRADA',imagen)
cv2.imshow('METODO CANNY', canny)
#Se usa para mostrar la umbralizacion simple en caso de haberlo usao
#cv2.imshow('UMBRALIZACION SIMPLE', th)
cv2.waitKey(0)
cv2.destroyAllWindows()