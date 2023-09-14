import numpy as np
import cv2


def contornos(frame):


############## caracteristicas video #################################
	
	#dimensions = frame.shape
	# height, width, number of channels in image
	#height = frame.shape[0]
	#width = frame.shape[1]
	#channels = frame.shape[2]

	#print('Image Dimension    : ',dimensions)
	#print('Image Height       : ',height)
	#print('Image Width        : ',width)
	#print('Number of Channels : ',channels)

###############################################

	#frame1=frame

################ Punto referencia ############

	#cv2.circle(frame, (150,150), radius=5, color=(0, 0, 255), thickness=-1)

###############################################





################# Segmentacion ###############

	roi = frame[40:200, 40:200]
	dimensions = roi.shape
	#print("dimensions =", dimensions)
	#print("dimensions =", dimensions[0])
	centro_roi_x=int(dimensions[0]/2)
	centro_roi_y=int(dimensions[1]/2)


	cv2.circle(roi, (centro_roi_x,centro_roi_y), radius=5, color=(0, 0, 255), thickness=-1)

	frame_rgb = cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)
	frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	ret,thresh1 = cv2.threshold(frame_hsv,200,255,cv2.THRESH_BINARY)
	BN = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
	#th3 = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	#Hori = np.concatenate((frame, BN), axis=1)
	blurred = cv2.GaussianBlur(thresh1, (7, 7), 0)
	#(T, threshInv) = cv2.threshold(frame, 0, 255,cv2.THRESH_BINARY_INV,cv2.THRESH_OTSU)
	Linea_negra=cv2.inRange(frame_rgb, (0,0,0),(50,50,50))
	Linea_negra1=cv2.inRange(frame_hsv, (0,0,0),(100,80,100))
	blurred = cv2.GaussianBlur(Linea_negra, (7, 7), 0)
	#thresh1 = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
	

	#ret,thresh = cv2.threshold(BN,60,255,cv2.THRESH_BINARY_INV)

	kernel=np.ones((3,3),np.uint8)
	Linea_negra=cv2.erode(Linea_negra,kernel,iterations=1)

	Linea_negra=cv2.dilate(Linea_negra,kernel,iterations=4)

	cv2.line(roi,(0,150),(500,150),(255,0,0),3)

	cnts,hierarchy = cv2.findContours(Linea_negra, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(roi,cnts,-1,(0,255,0),3)
	#print(type(contours))
	#print("Number of contours in image:",len(cnts))
	perimetro_ordenado={}

	for n in range(len(cnts)):
		cnt=cnts[n]
		area = cv2.contourArea(cnt)
		perimeter = cv2.arcLength(cnt, True)
		perimeter = round(perimeter, 4)
		#print('Area: ', area)
		#print('Perimeter: {n} = {perimeter}'.format(n=n, perimeter=perimeter))
		perimetro_ordenado[n]=perimeter

	print("perimetro_ordenado =",perimetro_ordenado)
	a = max(perimetro_ordenado, key=lambda x:perimetro_ordenado[x])
	print(a)
	x,y,w,h = cv2.boundingRect(cnts[a])
	#cv2.rectangle(frame,(x,y),(x+w,y+h),(0,50,255),3)
	#print((x+(w/2), 200))

	cv2.line(roi, (int(x+(w/2)), 0), (int(x+(w/2)), 500),(255,0,0),3)
	b=int(x+(w/2))

	cv2.circle(roi, (b,int(dimensions[1]/2)), radius=5, color=(0, 0, 255), thickness=-1)
	
	distancia_x=centro_roi_x-int(x+(w/2))
	
	#if a>0:
	#	distancia_xdistancia_x*-1
	print("distancia_x =", distancia_x)


	#if len(contours)>0:
	#	x,y,w,h = cv2.boundingRect(contours[0])

	#	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
		
		#######Esta linea debe


##############################################

##############################################


	cv2.imshow('frame',frame)
	cv2.imshow('roi',roi)
	#cv2.imshow("hsv",frame_hsv)
	#cv2.imshow("ret",thresh1)
	#cv2.imshow("img",img)
	#cv2.imshow("BN",BN)
	cv2.imshow("blurred",blurred)
	#cv2.imshow("Mean Adaptive Thresholding", thresh1)
	#cv2.imshow("thresh",thresh)
	cv2.imshow("Linea_Negra",Linea_negra)
	#cv2.imshow("Linea_negra1",Linea_negra1)
	#cv2.imshow("threshInv",threshInv)

	# Move window to (10,50) position
	# using moveWindow() function
	cv2.moveWindow("frame", 10, 50)
	cv2.moveWindow("roi", 10, 500)
	#cv2.moveWindow("ret", 950, 50)
	cv2.moveWindow("blurred", 500, 50)
	cv2.moveWindow("Linea_Negra", 950, 200)
	#cv2.moveWindow("Linea_Negra1", 10, 200)
	#cv2.moveWindow("Mean Adaptive Thresholding", 650, 500)
  



	return(distancia_x)


