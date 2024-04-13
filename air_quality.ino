//if you guys have to change stuff go ahead 

#include <Wire.h>

#include <MQ135.h>
#include <MHMQ7.h>

// Define sensor IDs -- simple 1 & 2 for now. 
const int MQ135_ID = 1;
const int MHMQ7_ID = 2;

// Define sensor pins for  - Given over to hardward
const int MQ135_PIN = A0;
const int MHMQ7_PIN = A1;

// Create sensor objects -

MQ135 mq135(MQ135_PIN);
MHMQ7 mhmq7(MHMQ7_PIN);

void setup() {
  Serial.begin(9600);
  Wire.begin();


void loop() {

  // Read MQ135 sensor data
  float mq135Value = mq135.getPPM();
  Serial.print("Sensor ID: ");
  Serial.println(MQ135_ID);
  Serial.print("MQ135 value: ");
  Serial.print(mq135Value);
  Serial.println(" ppm");
  Serial.println();

  // Read MHMQ7 sensor data
  float mhmq7Value = mhmq7.getCOPPM();
  Serial.print("Sensor ID: ");
  Serial.println(MHMQ7_ID);
  Serial.print("MHMQ7 CO value: ");
  Serial.print(mhmq7Value);
  Serial.println(" ppm");
  Serial.println();

  delay(2000); // Wait for 2 seconds before taking the next readings