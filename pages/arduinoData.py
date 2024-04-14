import serial
import hashlib  # Import for hash calculation (optional)

## Setup the serial connection
ser = serial.Serial('/dev/cu.usbmodem1301', 9600, timeout=1)

# Empty string to store weather data
weatherInfo = ""


def update_blockchain(weather_data):
  """
  Updates the blockchain with the provided weather data.

  This function imports the `create_blockchain` function from `testChain.py`
  and creates a new blockchain with the weather data. You can modify this
  function to interact with your existing blockchain implementation.

  Args:
      weather_data (str): The weather data to be added to the blockchain.
  """
  # Import the create_blockchain function from testChain.py
  from testChain import create_blockchain

  # Create a new blockchain with the weather data
  blockchain = create_blockchain(weather_data)

  # Print or store the blockchain (optional)
  print(f"Latest Block - {blockchain[-1]['data']}")
  print(f"Latest Block Hash - {blockchain[-1]['hash']}")


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
        weatherInfo = f"MQ135 senses {sensor_data[0]} and MHMQ7 senses {sensor_data[1]}"

        # Call update_blockchain to add data to the chain
        update_blockchain(weatherInfo)
        print("-----------------------------------------------------------------------")
        print()

  except serial.SerialException as e:
      print(f"Serial Error: {e}")
      break  # Exit on serial errors

# Close the serial port (optional)
ser.close()
