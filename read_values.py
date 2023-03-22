import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes
print("Chip ID: ", data.id)
print("Timestamp: ", data.timestamp)
print("Temp: ", data.temperature, " °C")
print("Pressure: ", data.pressure, " hPa")
print("Humidity: ", data.humidity, " %")

# there is a handy string representation too
# print(data)