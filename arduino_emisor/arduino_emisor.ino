// Ejemplo: Arduino Uno, lectura de A0 aproximadamente cada 100 ms.
// Conectar un potenciómetro entre 5 V y GND, cursor a A0 (placa Uno de 5 V).
// Para otra placa, respetar su tensión admisible de entrada.
void setup() {
  Serial.begin(115200);
}

void loop() {
  unsigned long t = millis();
  int valor = analogRead(A0);
  Serial.print(t);
  Serial.print(",");
  Serial.println(valor);
  delay(100);
}
