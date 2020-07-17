import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

z=1

f1 = "cross.csv"
f2 = "total.csv"

r0 = []
r1 = []
rr0 = []
rr1 = []
header = 3


with open(f1, 'r') as csvfile:
  
    reader= csv.reader(csvfile, delimiter=';')

    for i in range(header):
      next(reader)
        

    for row in reader:
      
      r0.append(float(row[0])/1e6)
      r1.append(float(row[1]))
    

with open(f2, 'r') as csvfile:
  
    reader= csv.reader(csvfile, delimiter=';')

    for i in range(header):
      next(reader)
        

    for row in reader:
      
      rr0.append(float(row[0])/1e6)
      rr1.append(float(row[1]))

plt.plot(rr0,rr1,label = "TENDL-2015 MT=5(z, anything)",color = 'red')
plt.plot(r0,r1,label = "TENDL-2009 MT=28(z, n+p)" )

plt.xlabel("Energy [MeV]")
plt.ylabel("Cross Section [b]")
plt.xlim(0,120)

plt.yscale('log')

plt.legend()
plt.show()

