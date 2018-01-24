import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
import scipy.stats as stats
import math
import matplotlib.mlab as mlab


#data1 = []
#data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
count = 0
with open("./scale_data.txt", "r") as ins:
    for line in ins:
        count = count +1

# Traffic Rate.
#with open("./scale_data.txt", "r") as ins:
#    for line in ins:
#        line = line.strip()
#        words = line.split(",")
#        x = words[0]
#        y = words[1]
#        data1.append(float(x))
#        data2.append(float(y))

# NF Scaling Plot.
nfcount = 1
hostcount = 1
with open("./latency_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        nfcount = float(words[1])
        hostcount = float(words[2])
        latency = float(words[3])
        
        data3.append(float(x))
        data4.append(float(nfcount))
        data5.append(float(hostcount))
        data6.append(float(latency))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(data3, data4, 'r--')
#ax2.plot(data3, data6, 'b--')

ax1.set_xlim([0,400])
ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('# NFs / Hosts (Scaling)', color='b')
ax2.set_ylabel('Average Control Procedure Latency (msec)', color='g')

#plt.plot(data1, data2, linewidth=3, linestyle='--', color='r', label='Traffic Generation')
plt.scatter(data3, data6, linewidth=3, linestyle='--', color='b', label='Average Control Procedure Latency (msec)')
#plt.ylim([0, 13000])
#plt.ylim([0, 130])
ax1.set_ylim([0,13])
ax2.set_ylim([0,50])

#plt.grid(linestyle='--')
plt.savefig("./latency-scale.pdf", bbox_inches='tight')
plt.show()
