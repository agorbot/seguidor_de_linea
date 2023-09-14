#include "SerialTransfer.h"

//////////////////////////////////////////////////////////////////////
///////////////////// Motores ruedas /////////////////////////////////
//////////////////////////////////////////////////////////////////////
int RPWM_A_Output = 10; // Arduino PWM output pin 5; connect to IBT-2 pin 1 (RPWM)
int LPWM_A_Output = 11; // Arduino PWM output pin 6; connect to IBT-2 pin 2 (LPWM)

int RPWM_B_Output = 8; // Arduino PWM output pin 5; connect to IBT-2 pin 1 (RPWM)
int LPWM_B_Output = 9; // Arduino PWM output pin 6; connect to IBT-2 pin 2 (LPWM)

int RPWM_C_Output = 7; // Arduino PWM output pin 5; connect to IBT-2 pin 1 (RPWM)
int LPWM_C_Output = 6; // Arduino PWM output pin 6; connect to IBT-2 pin 2 (LPWM)

int RPWM_D_Output = 5; // Arduino PWM output pin 5; connect to IBT-2 pin 1 (RPWM)
int LPWM_D_Output = 4; // Arduino PWM output pin 6; connect to IBT-2 pin 2 (LPWM)
int pwm = 50;

///////////////////////////////////////////////////////////////////////
/////////////comunicacion//////////////////////////////////////////////////////////
SerialTransfer myTransfer;
int32_t list[3];
int32_t valor;

int32_t a;
////////////////Tiempos actuación///////////////////
long previousMillis = 0;
long interval = 500;  // interval at which to (milliseconds)

///////////////////////////////////////////////////////////////////////
void setup() 
{


   pinMode(RPWM_A_Output, OUTPUT);
   pinMode(LPWM_A_Output, OUTPUT);
   pinMode(RPWM_B_Output, OUTPUT);
   pinMode(LPWM_B_Output, OUTPUT);
   pinMode(RPWM_C_Output, OUTPUT);
   pinMode(LPWM_C_Output, OUTPUT);
   pinMode(RPWM_D_Output, OUTPUT);
   pinMode(LPWM_D_Output, OUTPUT);

   Serial.begin(9600);
   myTransfer.begin(Serial);

}



void loop() {

////////// Recibir datos ////////

if(myTransfer.available()) /////////////Recibe data
  {
     a=myTransfer.rxObj(valor);

    //Serial.println("Received:");
    //Serial.print(list[0]);
    //Serial.println(list[1]);
    //Serial.println();
  }

  
/////////////////////////////////////////////  
  unsigned long currentMillis = millis();

  if(currentMillis - previousMillis > interval) {
    // save the last time you blinked the LED 
    previousMillis = currentMillis;   

    if (valor>0){
    I();       }
    if (valor<0) {
    D();
    }
      }
  

////// Enviar datos ///////////

// use this variable to keep track of how many
// bytes we're stuffing in the transmit buffer
 uint16_t sendSize = 0;

  ///////////////////////////////////////// Stuff buffer 
 sendSize = myTransfer.txObj(valor, sendSize);
  ///////////////////////////////////////// Send buffer
 myTransfer.sendData(sendSize);
  
  delay(50);
  }
///////////////////////////////////////////////////////////////////



void A() //Adelante
{
 analogWrite(LPWM_A_Output, pwm);
 analogWrite(RPWM_A_Output, 0);

 analogWrite(LPWM_B_Output, pwm);
 analogWrite(RPWM_B_Output, 0);

 analogWrite(LPWM_C_Output, pwm); 
 analogWrite(RPWM_C_Output, 0);

 analogWrite(LPWM_D_Output, pwm);
 analogWrite(RPWM_D_Output, 0);

 delay (400);

 analogWrite(LPWM_A_Output, 0);
 analogWrite(RPWM_A_Output, 0);

 analogWrite(LPWM_B_Output, 0);
 analogWrite(RPWM_B_Output, 0);

 analogWrite(LPWM_C_Output, 0);
 analogWrite(RPWM_C_Output, 0);

 analogWrite(LPWM_D_Output, 0);
 analogWrite(RPWM_D_Output, 0);
}

void R() //Retroceder
{
 analogWrite(LPWM_A_Output, 0);
 analogWrite(RPWM_A_Output, pwm);

 analogWrite(LPWM_B_Output, 0);
 analogWrite(RPWM_B_Output, pwm);

 analogWrite(LPWM_C_Output, 0);
 analogWrite(RPWM_C_Output, pwm);

 analogWrite(LPWM_D_Output, 0);
 analogWrite(RPWM_D_Output, pwm);

 delay (400);

 analogWrite(LPWM_A_Output, 0);
 analogWrite(RPWM_A_Output, 0);

 analogWrite(LPWM_B_Output, 0);
 analogWrite(RPWM_B_Output, 0);

 analogWrite(LPWM_C_Output, 0);
 analogWrite(RPWM_C_Output, 0);

 analogWrite(LPWM_D_Output, 0);
 analogWrite(RPWM_D_Output, 0);
}

void D() //Derecha
{
 analogWrite(LPWM_A_Output, 0);
 analogWrite(RPWM_A_Output, 120);

 analogWrite(LPWM_B_Output, 120);
 analogWrite(RPWM_B_Output, 0);

 analogWrite(LPWM_C_Output, 120);
 analogWrite(RPWM_C_Output, 0);

 analogWrite(LPWM_D_Output, 0);
 analogWrite(RPWM_D_Output, 120); 

  delay (200);

 analogWrite(LPWM_A_Output, 0);
 analogWrite(RPWM_A_Output, 0);

 analogWrite(LPWM_B_Output, 0);
 analogWrite(RPWM_B_Output, 0);

 analogWrite(LPWM_C_Output, 0);
 analogWrite(RPWM_C_Output, 0);

 analogWrite(LPWM_D_Output, 0);
 analogWrite(RPWM_D_Output, 0);
}


void I() //Izquierda
{
 analogWrite(LPWM_A_Output, 120);
 analogWrite(RPWM_A_Output, 0);

 analogWrite(LPWM_B_Output, 0);
 analogWrite(RPWM_B_Output, 120);

 analogWrite(LPWM_C_Output, 0);
 analogWrite(RPWM_C_Output, 120);

 analogWrite(LPWM_D_Output, 120);
 analogWrite(RPWM_D_Output, 0); 

 delay (200);

 analogWrite(LPWM_A_Output, 0);
 analogWrite(RPWM_A_Output, 0);

 analogWrite(LPWM_B_Output, 0);
 analogWrite(RPWM_B_Output, 0);

 analogWrite(LPWM_C_Output, 0);
 analogWrite(RPWM_C_Output, 0);

 analogWrite(LPWM_D_Output, 0);
 analogWrite(RPWM_D_Output, 0);
}
