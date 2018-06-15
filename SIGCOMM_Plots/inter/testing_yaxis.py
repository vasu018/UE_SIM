import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO
#import numpy as np
import matplotlib
#import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':60})
matplotlib.rcParams['figure.figsize'] = 14, 10

s = StringIO(u"""     SDResource     SLOViolation
RR+RR        7.85   4.25
Inter+RR     23.7   6.92
RR+Intra     9.25   12.35
Inter+Intra  25.75   17.89""")

df = pd.read_csv(s, index_col=0, delimiter=' ', skipinitialspace=True)

fig = plt.figure() # Create matplotlib figure

ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.25

#rects2 = ax1.bar(ind+0.1, s2, width, color='lightgreen', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='50% Skew', hatch='/')
#df.SDResource.plot(kind='bar', color='salmon', ax=ax, width=width, position=1)
#df.SLOViolation.plot(kind='bar', color='royalblue', ax=ax2, width=width, position=0)

df.SDResource.plot(kind='bar', color='salmon', ax=ax,error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, label='SD Resource', hatch='/', position=1)
df.SLOViolation.plot(kind='bar', color='royalblue', ax=ax2, error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, label='SLO Violation', hatch ='.', position=0)

for tick in ax.get_xticklabels():
    tick.set_rotation(30)

ax.set_ylabel('SDResource')
ax2.set_ylabel('SLOViolation')
plt.legend(loc='upper right',ncol=1, fontsize=60, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)

ax.xaxis.grid(color='gray',linestyle='--')
ax.yaxis.grid(color='gray', linestyle='--')
plt.savefig("./inter-intra.pdf", bbox_inches='tight')

plt.show()
