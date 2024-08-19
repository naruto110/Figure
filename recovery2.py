import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rcParams['pdf.fonttype'] = 42

# labels = ['BUP', 'RECEIPT', 'TMA-Ins', 'TMA-Del']

datasets = ['g500-22', 'uni-22', 'OR']
labels = ['Teseo', 'Sortleton', 'DGAP', 'HMDG']
# datasets = ['YT', 'BC', 'MR', 'DT', 'GH', 'IM']

figs, axes = plt.subplots(nrows=1, ncols=1)

data = np.array([
    [24.3, 12.8, 121, 6.4],
    [25, 9.6, 97, 2.4],
    [37.5, 18.5, 211, 16.7]
]
)

nv = np.array([3.5, 1.5, 9.2])
rc = np.array([0.8, 1.4, 6.6])

bar_width = 0.12
space_width = 0.03  # 柱子之间的间距

colors = ['C4', 'C6', 'C2', 'C3', 'C9']
hatches = ['///', '\\\\\\', '...', 'xxx', '']

for i, label in enumerate(labels):
    x = np.arange(len(datasets)) + (i - 2) * (bar_width + space_width)
    bars = axes.bar(x, data[:, i], bar_width, edgecolor='black', color=colors[i], hatch=hatches[i])

    for ib, bar in enumerate(bars):
        height = bar.get_height()
        axes.annotate('{:.0f}x'.format(height / rc[ib]),
                      xy=(bar.get_x() + bar.get_width() / 2, height),
                      xytext=(0, 3),  # 3 points vertical offset
                      textcoords="offset points",
                      ha='center', va='bottom', rotation=90)

x = np.arange(len(datasets)) + (3 - 2) * (bar_width + space_width)
axes.bar(x, nv, bar_width, edgecolor='black', color='#FFA8A8', hatch='xxx')

x = np.arange(len(datasets)) + (4 - 2) * (bar_width + space_width)
bars = axes.bar(x, rc, bar_width, edgecolor='black', color='C9', hatch='')
for ib, bar in enumerate(bars):
    height = bar.get_height()
    axes.annotate('1x',
                  xy=(bar.get_x() + bar.get_width() / 2, height),
                  xytext=(0, 3),  # 3 points vertical offset
                  textcoords="offset points",
                  ha='center', va='bottom', rotation=90)

axes.set_xticks(range(len(datasets)))
axes.set_xticklabels(datasets)
axes.set_yscale('symlog', linthresh=30)
axes.set_yticks([0, 10, 20, 30, 100, 1000])
axes.set_yticklabels(['0', '10', '20', '30', '$10^2$', '$10^3$'])
axes.set_ylim(0, 2000)
axes.axhline(y=30, color='grey', linestyle='--', linewidth=1)
# axes.set_xlim(-1.5, 3.5)

axes.set_ylabel('Time cost (seconds)')
# axes.text(-0.45, 90, '(log scale)', rotation=90)

patches = [
    mpatches.Patch(facecolor=colors[0], edgecolor='black', hatch=hatches[0]),
    mpatches.Patch(facecolor=colors[1], edgecolor='black', hatch=hatches[1]),
    mpatches.Patch(facecolor=colors[2], edgecolor='black', hatch=hatches[2]),
    mpatches.Patch(facecolor=colors[3], edgecolor='black', hatch=hatches[3]),
    mpatches.Patch(facecolor='#FFA8A8', edgecolor='black', hatch=hatches[3]),
    mpatches.Patch(facecolor=colors[4], edgecolor='black', hatch=hatches[4])
]
# 'Teseo', 'Sortleton', 'DGAP', 'HMDG'
fig_leg = plt.figlegend(labels=['Teseo', 'Sortleton', 'DGAP', 'HMDG',
                                'HMDG-Volatile', 'HMDG-Recovery'],
                        loc='lower center',
                        # bbox_to_anchor=(0.5, 1.1),
                        handles=patches,
                        handlelength=2.5,
                        handleheight=1.5,
                        ncol=3)
fig_leg.get_frame().set_edgecolor('black')

figs.tight_layout(rect=[0, 0.23, 1, 1], h_pad=0, w_pad=0)
# figs.tight_layout(rect=[0, 0, 1, 0.88], h_pad=0, w_pad=0)  # [左, 下, 右, 上] [0,0,1,1]
figs.set_figheight(3)
figs.set_figwidth(6)
# plt.show()
figs.savefig('./experiment/recovery2.pdf', bbox_inches='tight', transparent="True", pad_inches=0.01)
