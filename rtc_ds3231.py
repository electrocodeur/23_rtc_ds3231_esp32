"""# Import necessary modules
from machine import I2C, Pin
from ds3231 import *
import time

# Define the pins for I2C communication
sda_pin=Pin(21)
scl_pin=Pin(22)

# Initialize the I2C interface with the specified pins
i2c = I2C(0, scl=scl_pin, sda=sda_pin)
time.sleep(0.5)

# Create an instance of the DS3231 class for interfacing with the DS3231 RTC
ds = DS3231(i2c)

# Set the DS3231 RTC to current system time
ds.set_time()



"""
from machine import I2C, Pin
from ds3231 import *
import time

sda_pin=Pin(21)
scl_pin=Pin(22)

i2c = I2C(0, scl=scl_pin, sda=sda_pin)
time.sleep(0.5)

ds = DS3231(i2c)

# Print the current date in the format: month/day/year
print( "Date={}/{}/{}" .format(ds.get_time()[1], ds.get_time()[2],ds.get_time()[0]) )

# Print the current time in the format: hours:minutes:seconds
print( "Time={}:{}:{}" .format(ds.get_time()[3], ds.get_time()[4],ds.get_time()[5]) )



#These tuples are of the form: (year, month, day, hour, minute, second, weekday, yearday).
