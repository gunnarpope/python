from eda_serialcoms import *

sensor = Sensor()
exp = Experiment()

# connect with the sensor
sensor.establishConnection()

# set sensor time
sensor.setSensorTime()  # does not work

# get sensor time
sensor.getSensorTime()  # works

sensor.disconnect()
exit()