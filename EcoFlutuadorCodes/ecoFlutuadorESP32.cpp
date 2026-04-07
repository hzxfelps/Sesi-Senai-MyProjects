#include "BluetoothSerial.h"
BluetoothSerial SerialBT;

//Codigo com motor dc
int IN1 = 25;
int IN2 = 26;
int IN3 = 27;
int IN4 = 14;

void setup() {
  SerialBT.begin("EcoBarco");

  //saidas dos motores
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}

//comando de direcoes
void loop() {
  if (SerialBT.available()) {
    char comando = SerialBT.read();

    if (comando == 'F') frente();
    else if (comando == 'L') esquerda();
    else if (comando == 'R') direita();
    else parar();
  }
}

//funcoes de movimentacao
void frente() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void esquerda() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void direita() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

void parar() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}