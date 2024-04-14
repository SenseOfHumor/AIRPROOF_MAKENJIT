import serial

# Empty string to store weather data
weatherInfo = ""

## Setup the serial connection
ser = serial.Serial('/dev/cu.usbmodem1301', 9600, timeout=1)

while True:
  try:
    # Check if data is available
    if ser.inWaiting() > 0:
      # Read and decode data line
      data = ser.readline().decode('utf-8').rstrip()

      # Split the data assuming comma separation (modify if different)
      sensor_data = data.split(',')

      # Check if there are at least two sensor values
      if len(sensor_data) >= 2:
        # Update weatherInfo string
        weatherInfo = f"MQ135 senses {sensor_data[0]} and MHDQ7 senses {sensor_data[1]}"
        print(weatherInfo)

  except serial.SerialException as e:
      print(f"Serial Error: {e}")
      break  # Exit on serial errors

# Close the serial port (optional)
ser.close()
