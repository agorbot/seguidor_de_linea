# seguidor_de_linea
Seguidor de linea negra utilizando cámara y segmentación
Este programa es utilizado para seguir una linea negra mediante el uso de una cámara y un robot de 4 motores.
El seguimiento se realiza primero realizando la segmentación de la imagen, buscando resaltar el color negro y oscurecer todo el resto. 
Se obtiene la distancia desde un punto de referencia a la linea generada. Una vez obtenida la distancia, esta es enviada a un microcontrolador (Arduino). 
Si el valor está a la izquierda de la linea negra, el robot se mueve a la derecha. Si el robot está a la derecha de la linea negra, el robot semueve a la 
izquiera.

El programa esta compuesto de 3 archivos:

**main.py**

Este es el main del seguidor de linea negra. Aqui se llama al archivo que realiza la segmentación, desde donde se obtiene la distancia desde el centro 
de la linea al punto de referencia. Una vez obtenida esta distancia, se envía este valor al microcontrolador.

Utiliza las siguientes librerías:
- openCV
- numpy
- time
- pySerialTransfer
(además del debuguer pdb)

**ximbi_linea.py**
Aqui se realiza la segmentación de la imagen, se define el punto de referencia del robot y se obtiene la distancia desde el 

**seguidor_de_linea.ino**
Se utilizan las siguientes funciones:
- enviar datos
