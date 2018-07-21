import serial
import time
import threading

class Serial_Reader:
    # read charatcer stream from serial interface and populate raw_sentence_store
    def __init__(self, port, raw_sentence_store_limit=500, reading_interval_sec=1):
        self.raw_sentence_store = []
        self.raw_sentence_store_limit = raw_sentence_store_limit
        self.ser = serial.Serial()
        # set NMEA standard config
        self.ser.baudrate = 4800
        self.ser.port = port
        self.ser.bytesize = 8
        self.ser.parity = 'N'
        self.ser.stopbits = 1

        self.reading_interval_sec = reading_interval_sec
    
    def add_to_raw_sentence_store(self, new_sentence):
        if len(self.raw_sentence_store) + 1 <= self.raw_sentence_store_limit:
            # if we can add more sentences to store
            self.raw_sentence_store.append(new_sentence)
        else:
            # raw_sentence_store_limit reached
            del self.raw_sentence_store[0] # remove oldest sentence
            self.raw_sentence_store.append(new_sentence)
    
    def start_reading(self):
        self.ser.open()
        t = threading.Thread(target=self.read)
        t.start()
    
    def read(self):
        while self.s.is_open:
            new_data = self.s.read(self.s.in_waiting) # read all characters in_waiting
            new_sentences = new_data.splitlines() # get lines
            
            for x in new_sentences:
                if x[0] != '$':
                    # remove incomplete sentences
                    new_sentences.remove(x)
                # add complete sentences to raw_sentence_store
                self.add_to_raw_sentence_store(x)
            time.sleep(self.reading_interval_sec)
    
    def get_latest_gga(self):
        for x in reversed(self.raw_sentence_store):
            if x[0:6] == '$GPGGA':
                return x

# print("Starting to read data")
# raw_data = ""
# chars_read = 0
# count = 0
# while s.is_open:
#     new_data = s.read(s.in_waiting)
#     count += 1
#     # chars_read += 1
#     print(new_data) # to see raw NMEA sentences
#     raw_data += new_data
#     if count == 10000:
#         break

# lines = raw_data.splitlines()
# print(raw_data)
# s.close()