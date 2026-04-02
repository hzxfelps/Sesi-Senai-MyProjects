# 🌊 Ecoflutuador

Projeto de um veículo aquático automatizado desenvolvido para estudar controle de motores e sistemas embarcados.

## 🚀 Visão geral

O ecoflutuador funciona a partir de um microcontrolador (Arduino/ESP32) que envia sinais para controlar os motores responsáveis pela propulsão na água.

O projeto possui diferentes versões, testando abordagens com motor DC e motor brushless.

## ⚙️ Lógica das programações

De forma geral, todas as versões seguem a mesma lógica:

1. O microcontrolador inicializa os pinos e configura os componentes  
2. Recebe ou define comandos de movimento  
3. Controla a velocidade dos motores usando PWM  
4. Ajusta direção e intensidade conforme a lógica implementada  

### 🔹 Motor DC
Controle direto da velocidade através de variação de sinal (PWM), com resposta simples e fácil de implementar.

### 🔹 Motor Brushless
Uso de um ESC (Electronic Speed Controller), que interpreta o sinal enviado pelo microcontrolador para controlar o motor com mais eficiência e potência.

## 📌 Objetivo

Comparar diferentes formas de controle de propulsão e entender o comportamento de cada tipo de motor na prática.

---
# 🌊 Ecoflutuador

Projeto de um veículo aquático automatizado desenvolvido para estudar controle de motores e sistemas embarcados.

## 🚀 Visão geral

O ecoflutuador funciona a partir de um microcontrolador (Arduino/ESP32) que envia sinais para controlar os motores responsáveis pela propulsão na água.

O projeto possui diferentes versões, testando abordagens com motor DC e motor brushless.

## ⚙️ Lógica das programações

De forma geral, todas as versões seguem a mesma lógica:

1. O microcontrolador inicializa os pinos e configura os componentes  
2. Recebe ou define comandos de movimento  
3. Controla a velocidade dos motores usando PWM  
4. Ajusta direção e intensidade conforme a lógica implementada  

### 🔹 Motor DC
Controle direto da velocidade através de variação de sinal (PWM), com resposta simples e fácil de implementar.

### 🔹 Motor Brushless
Uso de um ESC (Electronic Speed Controller), que interpreta o sinal enviado pelo microcontrolador para controlar o motor com mais eficiência e potência.

## 📌 Objetivo

Comparar diferentes formas de controle de propulsão e entender o comportamento de cada tipo de motor na prática.

---
