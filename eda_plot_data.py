
# by: gunnar pope
# date: 11/19/2018
import csv
import matplotlib.pyplot as plt
import numpy as np

# file = 'data/u1800@lab.d10.p01.10192018.txt'
file = 'data/uIONA@lab.d01.p01.10022018.txt'

data = []
with open(file, 'r') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        data.append(row)

setting = data[0]

if setting == ['lab']:

    header  = data[1]
    starttime = data[2]
    units     = data[3]
    timerdata = np.array( data[4:] )

print( units)
print( timerdata[:4])

C = 0.047e-6
Fclk = 32768.0

def NtoGskin(n):
    """Convert from number of timer clock cycles, n, to units of skin conductance, G (uS)
    Input:
        N = integer from 0-32768 where N is the rising-edge-to-rising-edge pulse time (change + discharge cycle
        of sensor.
    Output:
        G = skin conductance in (uS)"""

    G = (1.4*C*Fclk)/ (1.0*n) *1e6  - 1/13.3e3 #in uS

    return G # in microSiemens

gskin = [ NtoGskin(int(n)) for n in timerdata]
t = np.linspace(0,len(gskin)/2.0,len(gskin))/3600


plt.plot(t,gskin)
plt.title("EDA during labor")
plt.ylabel("Skin Conductance (uS)")
plt.xlabel("Hours")
plt.show()