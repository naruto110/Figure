import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rcParams['pdf.fonttype'] = 42


datasets = ['g500-22', 'uni-22']
labels = ['Stinger', 'Teseo', 'Sortleton', 'HMDG']

figs, axes = plt.subplots(nrows=1, ncols=1)

data = np.array([
    [1940, 202, 127, 73.1],
    [61.7, 201, 93, 34.7]
]
)

bar_width = 0.05
space_width = 0.015  # 柱子之间的间距

colors = ['C4', 'C3', 'C1', 'C2']
hatches = ['xxx', 'ooo', '+++', '---']



for i, label in enumerate(labels):
    x = np.arange(len(datasets)) + i * (bar_width + space_width) + 1 - 0.1
    print(x)
    axes.bar(x, data[:, i], bar_width, edgecolor='black', color=colors[i], hatch=hatches[i])


# axes.set_xticks(range(len(datasets)))
axes.set_xticks((1, 2))
axes.set_xticklabels(datasets)
axes.set_yscale('log')
plt.xlim(0.5, 2.5)

axes.set_ylabel('Time cost (seconds)')

patches = [
    mpatches.Patch(facecolor=colors[0], edgecolor='black', hatch=hatches[0]),
    mpatches.Patch(facecolor=colors[1], edgecolor='black', hatch=hatches[1]),
    mpatches.Patch(facecolor=colors[2], edgecolor='black', hatch=hatches[2]),
    mpatches.Patch(facecolor=colors[3], edgecolor='black', hatch=hatches[3]),
    # mpatches.Patch(facecolor=colors[4], edgecolor='black', hatch=hatches[4]),
    # mpatches.Patch(facecolor=colors[5], edgecolor='black', hatch=hatches[5])
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
figs.savefig('./experiment/mixed.pdf', bbox_inches='tight', transparent="True", pad_inches=0.01)
