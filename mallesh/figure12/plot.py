import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':18})

means = [4535, 250, 2600000, 4500000, 5300000]

ind = np.arange(5)  # the x locations for the groups
width = 0.25
fig, ax1 = plt.subplots()
fig.tight_layout()
fig.subplots_adjust(left=0.1, bottom=0.3, right=0.95)

rects1 = ax1.bar(ind, means, width, edgecolor='k', fill=False, linewidth=6, log=True)
#rects1 = ax1.bar(ind, means, width, edgecolor='k', fill=False, linewidth=6)
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    la = ['4.3K', '250', '4.5M', '5.3M']
    c = 0
    for rect in rects:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., 1.05*height, la[c],
                #'%d' % int(height),
                ha='center', va='bottom', fontsize=24)
        c +=1

#autolabel(rects1)

plt.xticks(np.arange(len(means)), ['OAI', 'PhantomNet\n(OpenEPC)', 'CloudRAM', 'Our Stateful\n(Intel DPDK)', 'Our Stateless\n(Intel DPDK)'], fontsize=18)
plt.ylabel('Throughput (PPS)')
ax1.grid(linestyle='--')
plt.savefig("./throughput-fig12.pdf", bbox_inches='tight')
plt.show()
