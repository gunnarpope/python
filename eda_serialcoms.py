# # from datetime import datetime, date, time
import serial
import time
import io
from python.pytime import *


class Sensor:

    STARTUP_CMD   = '1'
    DOWNLOAD_CMD  = 'D'
    SETTIME_CMD   = 'T'
    QUIT_CMD      = 'Q'
    LABMODE_CMD   = 'S'
    FIELDMODE_CMD = 'C'
    GETTIME_CMD   = 't'
    GETEVENTS_CMD = 'E'



    def __init__(self):
        self.connectionState = False
        self.data = [[]]
        self.events = []
        self.ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=115200,
            timeout=0.1,
            bytesize=serial.EIGHTBITS
        )
        self.ser.isOpen()
        self.con = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))

    def downloadData(self):
        for i in range(3):
            if (self.sendCommand(self.GETEVENTS_CMD)):
                print("Downloading Events...")
                self.events = self.con.read()
                print(self.events)
                break
            else:
                print("Failed to download events. Trying again...")
                self.con.flush()

        for i in range(3):
            if (self.sendCommand(self.DOWNLOAD_CMD)):
                print("Downloading...")
                self.data= self.con.read()

                print(self.data)
                break
            else:
                print("Bad Download")
                self.con.flush()

        return ( self.data )


    def establishConnection(self):
        for i in range(3):
            if ( self.sendCommand(self.STARTUP_CMD) ):
                self.con.flush()
                print("Connection Established.")
                self.connectionState = True
                break

            else:
                print("Trying to connect with device...")

        if (self.connectionState == False):
            print("Failed to connect with device.")


    def disconnect(self):
        # self.con.write('q')
        if (self.sendCommand(self.QUIT_CMD) ):
            print('Sensor Settings Summary:')
            resp = self.con.readlines()

            for response in resp:
                print(response)
            print('Serial Session Closed')

        else:
            print("Failed to start recording")

        self.ser.close()

    def disconnectWithoutReset(self):
        self.ser.close()


    def recordNonCompression(self):
        if (self.sendCommand(self.LABMODE_CMD) ):
            # print("Recording in Laboratory Mode (Continuous, Non-Compressed)")
            resp = self.con.readlines()
            for response in resp:
                print(response)
        else:
            print("Failed to Record")


    def recordCompression(self):
        if (self.sendCommand(self.FIELDMODE_CMD) ):

            resp = self.con.readlines()
            for response in resp:
                print(response)
            # print("Recording in Field Mode (Continuous Compression)")
        else:
            print("Failed to Record")

    def getSensorTime(self):
        if (self.sendCommand(self.GETTIME_CMD) ):
            resp = self.con.readlines()
            for response in resp:
                print(response)
        else:
            print("Failed to Retrieve Sensor Time")

    def setSensorTime(self):
        if (self.sendCommand(self.SETTIME_CMD) ):

            year  = str( getYear() ).zfill(2)
            month = str( getMonth() ).zfill(2)
            day   = str( getDay() ).zfill(2)
            DOW   = str( getDOW() ).zfill(2)
            hr    = str( getHour() ).zfill(2)
            min   = str( getMinute() ).zfill(2)
            sec   = str( getSecond() ).zfill(2)

            timestamp = year + month + day + DOW + hr + min + sec

            for ch in timestamp:
                self.sendCommand(ch)

        else:
            print("Failed to Set Sensor Time")

    def sendCommand(self,command):
        """Input type is a BYTE
           Returns 1 if BTYE is returned from UART
        """
        self.con.flush()
        self.con.readlines()

        self.con.write(command)
        time.sleep(0.1)
        self.con.flush()
        try:
            rx = self.con.read(1)
            if (rx == command):
                return 1
        except:
            return 0

class Experiment:
    def __init(self):
        data = []
        events = []
        time = []
        file = []

if __name__ == '__main__':

    sensor = Sensor()
    exp = Experiment()

    # connect with the sensor
    sensor.establishConnection()


    ########################################## start commands below ######################33
    # reset the memory
    # sensor.resetMemory()  #works

    # set the sensor into compression mode
    # sensor.recordCompression()

    # set the sensor into continuous recording
    # sensor.recordNonCompression() # works

    # set sensor time
    sensor.setSensorTime() # does not work



    # get sensor time
    sensor.getSensorTime() #works

    # sample for 10 seconds

    # download the data
    # exp.data = sensor.downloadData()
    # timestamp = getNowTime()
    # print(exp.data)

    # disconnect the sensor
    ######################################### disconnect the sensor ##########################3

    sensor.disconnect()
    exit()

