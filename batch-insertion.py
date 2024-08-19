import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rcParams['pdf.fonttype'] = 42

# labels = ['BUP', 'RECEIPT', 'TMA-Ins', 'TMA-Del']

datasets = ['OR', 'UK', 'g500-22', 'g500-26', 'uni-22', 'uni-26']
# labels = ['PMAG', 'Terrace', 'Stinger', 'Teseo', 'DGAP', 'Sortleton', 'HMDG']
labels = ['Terrace', 'Stinger', 'Teseo', 'Sortleton', 'HMDG']
# datasets = ['YT', 'BC', 'MR', 'DT', 'GH', 'IM']

figs, axes = plt.subplots(nrows=1, ncols=1)

data = np.array([
    [411, 32, 37.5, 18.5, 9.2],
    [0, 0, 0, 694, 566],
    [188, 188, 24.3, 12.8, 3.5],
    [4149, 0, 276, 231, 60],
    [220, 6.8, 25, 9.6, 4.4],
    [6185, 0, 285, 150, 74]
]
)

bar_width = 0.1
space_width = 0.03  # 柱子之间的间距

colors = ['C4', 'C6', 'C3', 'C1', 'C2']
hatches = ['///', 'xxx', 'ooo', '+++', '---']

for i, label in enumerate(labels):
    x = np.arange(len(datasets)) + i * (bar_width + space_width) - 0.26
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
    # mpatches.Patch(facecolor=colors[5], edgecolor='black', hatch=hatches[5])
]

fig_leg = plt.figlegend(labels=labels,
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
figs.set_figwidth(5)
plt.show()
# figs.savefig('./experiment/batch-insertion.pdf', bbox_inches='tight', transparent="True", pad_inches=0.01)
