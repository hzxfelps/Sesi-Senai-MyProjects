#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "WI-FI EDUC";
const char* password = "ac8ce4ss8@educ";

const char* serverUrl = "http://10.121.235.55:5000/update";

#define BOTAO 18

void setup() {
  Serial.println("INICIOU");
  Serial.begin(115200);

  pinMode(BOTAO, INPUT_PULLUP); // MUITO IMPORTANTE

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando...");
  }

  Serial.println("Conectado!");
}

void loop() {
  if (digitalRead(BOTAO) == LOW) { // botão pressionado

    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;

      int grupo = 1;
      int nivel = 2; // pode mudar depois

      String url = String(serverUrl) + "?grupo=" + grupo + "&nivel=" + nivel;

      http.begin(url);
      int httpResponseCode = http.GET();

      Serial.println("BOTAO APERTADO -> enviando");

      http.end();
    }

    delay(1000); // debounce simples
  }
}