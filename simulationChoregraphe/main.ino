#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "SEU_WIFI";
const char* password = "SUA_SENHA";

const char* serverUrl = "http://192.168.0.100:5000/update"; // IP do notebook

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando...");
  }

  Serial.println("Conectado!");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    int nivel = random(0, 10); // simula potenciometro
    int grupo = 1;

    String url = String(serverUrl) + "?grupo=" + grupo + "&nivel=" + nivel;

    http.begin(url);
    int httpResponseCode = http.GET();

    Serial.print("Enviado -> Grupo: ");
    Serial.print(grupo);
    Serial.print(" Nivel: ");
    Serial.println(nivel);

    http.end();
  }

  delay(5000);
}