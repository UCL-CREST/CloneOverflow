#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 18
fresh =     (1, 4, 0, 7, 5, 11, 0, 0, 0, 1, 0, 0, 0, 2, 3, 0, 3, 0)
outdated =  (0, 0, 2, 5, 9, 4,  2, 4, 4, 0, 2, 2, 3, 1, 9, 1, 0, 7)
deleted =   (0, 0, 0, 0, 0, 1,  0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0)
other =     (0, 0, 0, 0, 0, 0,  0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, outdated, width, color='yellow')
p2 = plt.bar(ind, deleted, width, color='red', bottom=outdated)
#p3 = plt.bar(ind, other, width, color="blue", bottom=deleted)
#p4 = plt.bar(ind, fresh, width, color='green', bottom=other)

plt.ylabel('Amount')
#plt.title('Scores by group and gender')
plt.xticks(ind + width/2., ('ant', 'log4j', 'aspectj', 'eclipse', 'hadoop', 'hibernate', 'jasperreports', 'jfreechart', 'jgraph', 'jgrapht', 'jstock', 'jung', 'junit', 'poi', 'spring', 'struts', 'tomcat', 'weka'),rotation=30)

plt.yticks(np.arange(0, 16))
#plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Outdated', 'Deleted', 'Others', 'Fresh'), loc=2)

plt.show()