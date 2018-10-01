import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 14, 10

means = [3635, 250, 2600000, 4301755, 4120387]

ind = np.arange(5)  # the x locations for the groups
width = 0.3
fig, ax1 = plt.subplots()
fig.tight_layout()
fig.subplots_adjust(left=0.12, right=0.99)

rects1 = ax1.bar(ind, means, width, edgecolor='k', color='gold', linewidth=6)#, log=True)
#rects1 = ax1.bar(ind, means, width, edgecolor='k', fill=False, linewidth=6)
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    la = ['3.6K', '250', '2.6M', '4.3M', '4.1M']
    #la = [3635, 250, 2600000, 43017557, 3780387]
    c = 0
    for rect in rects:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., 1.05*height, la[c],
                #'%d' % int(height),
                ha='center', va='bottom', fontsize=24)
        c +=1

autolabel(rects1)

plt.xticks(np.arange(len(means)), ['OAI', 'PhantomNet\n(OpenEPC)', 'RAMCloud', 'Stateful\n(DPDK)', 'Stateless\n(DPDK)'], fontsize=30)
plt.ylabel('Throughput (PPS)')
#b_patch = mpatches.Patch(color='lightblue', label='Stateless')
#b_patch = mpatches.Patch(color='lightblue', label='Stateless')
#g_patch = mpatches.Patch(color='lightgreen', label='stateful')
#plt.legend(handles=[b_patch, g_patch])
plt.yscale('symlog')
plt.ylim([10, 100000000])
ax1.grid(linestyle='--')
plt.savefig("./throughput-fig12.pdf", bbox_inches='tight')
plt.show()