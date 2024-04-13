#include <Wire.h>
#include <MQ135.h>
#include "MQ7.h"

// Define sensor IDs -- simple 1 & 2 for now.
const int MQ135_ID = 1;
const int MHMQ7_ID = 2;

// Define sensor pins for - Given over to hardware
const int MQ135_PIN = A0;
const int MHMQ7_PIN = A1;

// Create sensor objects - Assuming 5.0V as the typical input voltage for the MQ7
MQ135 mq135(MQ135_PIN);
MQ7 mhmq7(MHMQ7_PIN, 5.0);  // Proper instantiation of MQ7 with required voltage parameter

void setup() {
  Serial.begin(9600);
  Wire.begin();  // This call initializes the I2C bus (check if your setup requires this)

  // Add any additional initialization code here if necessary
}

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
  float mhmq7Value = mhmq7.getPPM();  // Correct method call to read CO ppm from MQ7
  Serial.print("Sensor ID: ");
  Serial.println(MHMQ7_ID);
  Serial.print("MHMQ7 CO value: ");
  Serial.print(mhmq7Value);
  Serial.println(" ppm");
  Serial.println();

  delay(2000); // Wait for 2 seconds before taking the next readings
}
