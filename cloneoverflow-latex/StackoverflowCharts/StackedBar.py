import pandas as pd
import matplotlib.pyplot as plt

raw_data = {'systems': ['ant', 'log4j', 'aspectj', 'eclipse', 'hadoop', 'hibernate', 'jasperreports', 'jfreechart', 'jgraph', 'jgrapht', 'jstock', 'jung', 'junit', 'poi', 'spring', 'struts', 'tomcat', 'weka'],
            'fresh': [1, 4, 0, 7, 5, 11, 0, 0, 0, 1, 0, 0, 0, 2, 3, 0, 0, 3],
            'outdated': [0, 0, 2, 5, 9, 4,  2, 4, 4, 0, 2, 2, 3, 1, 9, 1, 7, 0],
            'deleted': [0, 0, 0, 0, 0, 1,  0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
            'other': [0, 0, 0, 0, 0, 0,  0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
df = pd.DataFrame(raw_data, columns=['systems', 'fresh', 'outdated', 'deleted', 'other'])
df

# Create the general blog and the "subplots" i.e. the bars
f, ax1 = plt.subplots(1, figsize=(10,5))

# Set the bar width
bar_width = 0.5

# positions of the left bar-boundaries
bar_l = [i+1 for i in range(len(df['fresh']))]

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i+(bar_width/2) for i in bar_l]

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the fresh data
        df['fresh'],
        # set the width
        width=bar_width,
        # with the label pre score
        label='Fresh',
        # with color
        color='green')

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the outdated data
        df['outdated'],
        # set the width
        width=bar_width,
        # with fresh on the bottom
        bottom=df['fresh'],
        # with the label mid score
        label='Outdated',
        # with color
        color='yellow')

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the deleted data
        df['deleted'],
        # set the width
        width=bar_width,
        # with outdated and fresh on the bottom
        bottom=[i+j for i,j in zip(df['outdated'],df['fresh'])],
        # with the label post score
        label='Deleted',
        # with color
        color='red')

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the other data
        df['other'],
        # set the width
        width=bar_width,
        # with deleted and outdated on the bottom
        bottom=[i+j for i,j in zip(df['deleted'],df['outdated'])],
        # with the label post score
        label='Other',
        # with color
        color='blue')

# set the x ticks with names
plt.yticks(fontsize=14)
plt.xticks(tick_pos, df['systems'], rotation=40, fontsize=14)

# Set the label and legends
ax1.set_ylabel("Amount").set_fontsize(14)
#ax1.set_xlabel("Systems")
plt.legend(loc='upper center', fontsize=14)

# Set a buffer around the edge
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
plt.subplots_adjust(bottom=0.3)
#plt.show()
plt.savefig(('/Users/Chaiyong/IdeasProjects/StackAnalyzer/cloneoverflow-latex/outdated.pdf'))