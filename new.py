from machine import I2C, Pin, Timer, ADC
import time
from ads1x15 import ADS1115  # Importing the ADS1115 module

# Constants and initialization
ADDR = 72               # I2C address for ADS1115
GAIN = 1                # Gain setting for ADS1115
FREQUENCY = 408808      # I2C frequency
CHORD_CHANNEL = 0       # ADS1115 channel to read chord length voltage

# Initialize I2C and ADS1115
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=FREQUENCY)
ads = ADS1115(i2c, addr=ADDR, gain=GAIN)

def get_length():
    """
    Reads a value from the ADS1115 on channel 0 and converts it to voltage,
    then adjusts it with a scaling factor for chord length measurement.
    """
    val_raw = ads.read(CHORD_CHANNEL)  # Read raw data from channel 0
    vol = ads.raw_to_v(val_raw)        # Convert raw data to voltage
    length_mm = int(vol * 188) / 100   # Adjust voltage to length in mm
    print(f"Measured length: {length_mm} mm")  # Print length in mm
    return length_mm

def calculate_diameter(c, d):
    """
    Calculate the diameter of the circle based on the chord length and distance from the chord midpoint.
    Formula: D = (c^2 / (2 * d)) + d
    """
    D = ((c ** 2) / (2 * d)) + d
    return D

# Input for the calculation
try:
    c = float(input("Enter the chord length (c) in mm: "))
    d = float(input("Enter the distance (d) from chord midpoint to outer edge in mm: "))

    # Calculate diameter and print result
    diameter = calculate_diameter(c, d)
    print(f"The diameter of the train's wheel is: {diameter} mm")

except ValueError:
    print("Please enter valid numerical values for chord length and distance.")