import cv2
import numpy as np
from ximbi_linea import *
import time
import pdb
import serial
from pySerialTransfer import pySerialTransfer as txfer


#########################################
## Crea serial para abrirlo despues #####
#link = txfer.SerialTransfer('/dev/ttyUSB0',115200) ########## replace COM port number ##########
#link = txfer.SerialTransfer('/dev/ttyUSB0', 9600) 
#link.open()        
#########################################




def enviar_datos(distancia_x):
    #link.open()  
    #if  
    print("los valores a ser enviados:", distancia_x)
    link.send(link.tx_obj(distancia_x))
    #print("los valores a ser enviado:", list_)
    print("Los datos estan siendo enviados *****")
    time.sleep(0.05)
   
    if link.available():
        print("link available")
        y= link.rx_obj(obj_type='i')
        while y == None:
            print("esperando")
        print("y:",y)
        return(y)
    
    while not link.available():
                if link.status < 0:
                    if link.status == txfer.CRC_ERROR:
                        print('ERROR: CRC_ERROR')
                    elif link.status == txfer.PAYLOAD_ERROR:
                        print('ERROR: PAYLOAD_ERROR')
                    elif link.status == txfer.STOP_BYTE_ERROR:
                        print('ERROR: STOP_BYTE_ERROR')
                    else:
                        print('ERROR: {}'.format(link.status))    
        





cap = cv2.VideoCapture("/home/cactus1/Documentos/AOB/Haciendo/Linea_negra/video2.mp4")
#cap = cv2.VideoCapture(2)
while(True):
    ret, frame = cap.read()

    ##===================cambio de dimenciones===============    
    height , width , layers =  frame.shape        
    new_h=300
    new_w=300
    frame = cv2.resize(frame, (new_w, new_h)) 
    
    ##=======================================================


#    cv2.imshow('frame',frame)
   
    distancia_x = int(contornos(frame))
    print("distancia_x =", distancia_x)
    print("tipo distancia_x =", type(distancia_x))
    time.sleep(0.05)
    


    #instruccion = distancia_x # Adelante
    #frase = str((instruccion))

#####################################################
    #retorno = enviar_datos(distancia_x)
    #print("retorno =",retorno)
    print("========")
#####################################################   

    #print(frase)
    # arduino.write(frase.encode())
     
    # rawString = arduino.readline() # Recibe
    # print("rawString = ", rawString)


    #pdb.set_trace()






    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()