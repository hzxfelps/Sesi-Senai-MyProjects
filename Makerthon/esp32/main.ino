#include <WiFi.h>
#include <HTTPClient.h>
#include "wifi_config.h"

int potPin = 34;
int leds[] = {2, 4, 5, 18, 19, 21, 22, 23, 25, 26};

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Conectando...");
  }

  Serial.println("Conectado!");

  for (int i = 0; i < 10; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {
  int valor = analogRead(potPin);

  // converte 0–4095 para 0–10
  int nivel = map(valor, 0, 4095, 0, 10);

  // acende LEDs
  for (int i = 0; i < 10; i++) {
    digitalWrite(leds[i], i < nivel ? HIGH : LOW);
  }

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String json = "{\"grupo\":1,\"nivel\":" + String(nivel) + "}";

    int httpResponseCode = http.POST(json);

    Serial.println(httpResponseCode);

    http.end();
  }

  delay(3000);
}