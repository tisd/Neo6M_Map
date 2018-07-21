from nmea_utils import NMEA_Utils
from serial_reader import Serial_Reader
import time

sr = Serial_Reader('/dev/ttyUSB0') # create a serial reader
sr.start_reading() # will start reading in separate thread
nu = NMEA_Utils()

while True:
    data = nu.get_fix_data(sr.get_latest_gga())
    print('Lat: ' + data['lat_str'])
    print('Long: ' + data['long_str'])
    time.sleep(1)
