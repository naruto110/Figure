import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rcParams['pdf.fonttype'] = 42

# labels = ['BUP', 'RECEIPT', 'TMA-Ins', 'TMA-Del']

datasets = ['OR, 4008', 'uni-22, 4008', 'OR, 16008', 'uni-22, 16008']
labels = ['Single Socket-Serial', 'Single Socket-Concurrency', 'Dual Socket-Serial', 'Dual Socket-Concurrency']
# datasets = ['YT', 'BC', 'MR', 'DT', 'GH', 'IM']

figs, axes = plt.subplots(nrows=1, ncols=1)

data1 = np.array([
    [47, 31.8, 28.4, 18.2],
    [37.6, 29.6, 21.8, 17.2],
    [47.1, 31.7, 28.4, 18.5],
    [37.7, 29.6, 22.4, 17.5]
]
)

bar_width = 0.11
space_width = 0.03  # 柱子之间的间距

colors = ['C0', 'C2', 'C1', 'C2']
hatches = ['xxx', 'ooo', '+++', '---']

for i, label in enumerate(labels):
    x = np.arange(len(datasets)) + i * (bar_width + space_width) - 0.21
    bars = axes.bar(x, data1[:, i], bar_width, edgecolor='black', color=colors[i], hatch=hatches[i])
    # 在每个柱子上添加数值标签
    # for bar in bars:
    #     height = bar.get_height()
    #     axes.annotate(f'{height}',
    #                 xy=(bar.get_x() + bar.get_width() / 2, height),
    #                 xytext=(0, 3),  # 3 points vertical offset
    #                 textcoords="offset points",
    #                 ha='center', va='bottom', rotation=90)

# plt.ylim(top=2000)
axes.set_xticks(range(len(datasets)))
axes.set_xticklabels(datasets)
# axes.set_yscale('log')

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
                        ncol=2)
fig_leg.get_frame().set_edgecolor('black')

figs.tight_layout(rect=[0, 0.22, 1, 1], h_pad=0, w_pad=0)
# figs.tight_layout(rect=[0, 0, 1, 0.88], h_pad=0, w_pad=0)  # [左, 下, 右, 上] [0,0,1,1]
figs.set_figheight(3)
figs.set_figwidth(5)
# plt.show()
figs.savefig('./experiment/concurrency.pdf', bbox_inches='tight', transparent="True", pad_inches=0.01)
