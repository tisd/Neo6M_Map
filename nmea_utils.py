class NMEA_Utils:
    def __init__(self):
        pass
                
    def get_fix_data(self, gga):
        # Takes gga nmea sentence and outputs data dict
        data = {}
        items = gga.split(',')
        data['time_str'] = items[1]
        data['lat_str'] = str(self.get_decimal_lat(items[2])) + ' ' + items[3]
        data['long_str'] = str(self.get_decimal_long(items[4])) + ' ' + items[5]
        data['fix_quality'] = self.get_fix_quality(items[6])
        data['num_of_satelites'] = int(items[7])
        data['hdop'] = float(items[8])
        data['altitude_m'] = float(items[9])
        data['hog_m'] = float(items[11])
        data['time_sec_since_last_dgps_update'] = items[13]
        data['dgps_sta_id'] = items[14]
        # data['checksum_data'] = items[15]
        return data
    
    def get_decimal_lat(self, nmea_lat):
        # nmea has ddmm.mmmm format for latitude
        return (int(nmea_lat[0:2]) + (float(nmea_lat[2:])/60))
    
    def get_decimal_long(self, nmea_long):
        # nmea has dddmm.mmmm format for longitude
        return (int(nmea_long[0:3]) + (float(nmea_long[3:])/60))

    def get_fix_quality(self, fix_quality_num):
        # Takes a number and converts to string, which to some extent explains fix quality
        fix_quality_num = int(fix_quality_num)
        fix_quality_strings = ['Invalid', 'GPS fix', 'DGPS fix', 'PPS fix', 'Real Time Kinematic', 'Float RTK', 'Estimated', 'Manual input mode', 'Simulation mode']
        if fix_quality_num in range(0, 9):
            return fix_quality_strings[fix_quality_num]
        else:
            raise("Invalid input to determine fix quality")
        

