import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rcParams['pdf.fonttype'] = 42

# labels = ['BUP', 'RECEIPT', 'TMA-Ins', 'TMA-Del']

datasets = ['OR', 'g500-22', 'uni-22']
labels = ['PMAG', 'Terrace', 'Stinger', 'Teseo', 'DGAP', 'Sortleton', 'HMDG']

# datasets = ['YT', 'BC', 'MR', 'DT', 'GH', 'IM']

figs, axes = plt.subplots(nrows=1, ncols=1)

data = np.array([
    [1474, 13071, 1320, 529, 211, 452, 151],
    [726, 4397, 7140, 319, 121, 336, 112],
    [728, 6042, 222, 299, 97, 197, 61],
]
)

bar_width = 0.06
space_width = 0.02  # 柱子之间的间距

colors = ['C5', 'C7', 'C4', 'C6', 'C3', 'C1', 'C2']
hatches = ['\\\\', '***', '///', 'xxx', 'ooo', '+++', '---']

for i, label in enumerate(labels):
    x = np.arange(len(datasets)) + i * (bar_width + space_width) - 0.24
    axes.bar(x, data[:, i], bar_width, edgecolor='black', color=colors[i], hatch=hatches[i])


axes.set_xticks(range(len(datasets)))
axes.set_xticklabels(datasets)
axes.set_yscale('log')

axes.set_ylabel('Time cost (seconds)')

patches = [
    mpatches.Patch(facecolor=colors[0], edgecolor='black', hatch=hatches[0]),
    mpatches.Patch(facecolor=colors[1], edgecolor='black', hatch=hatches[1]),
    mpatches.Patch(facecolor=colors[2], edgecolor='black', hatch=hatches[2]),
    mpatches.Patch(facecolor=colors[3], edgecolor='black', hatch=hatches[3]),
    mpatches.Patch(facecolor=colors[4], edgecolor='black', hatch=hatches[4]),
    mpatches.Patch(facecolor=colors[5], edgecolor='black', hatch=hatches[5]),
    mpatches.Patch(facecolor=colors[6], edgecolor='black', hatch=hatches[6])
]

fig_leg = plt.figlegend(labels=labels,
                        loc='lower center',
                        # bbox_to_anchor=(0.5, 1.1),
                        handles=patches,
                        handlelength=2.5,
                        handleheight=1.5,
                        ncol=4)
fig_leg.get_frame().set_edgecolor('black')

figs.tight_layout(rect=[0, 0.23, 1, 1], h_pad=0, w_pad=0)
# figs.tight_layout(rect=[0, 0, 1, 0.88], h_pad=0, w_pad=0)  # [左, 下, 右, 上] [0,0,1,1]
figs.set_figheight(3)
figs.set_figwidth(5)
# plt.show()
figs.savefig('./experiment/serial-insertion.pdf', bbox_inches='tight', transparent="True", pad_inches=0.01)
