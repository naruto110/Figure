import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rcParams['pdf.fonttype'] = 42

# labels = ['BUP', 'RECEIPT', 'TMA-Ins', 'TMA-Del']

datasets = ['OR', 'g500-22', 'g500-26', 'uni-22', 'uni-26']
labels = ['1', '8', '16', '32', '64']

figs, axes = plt.subplots(nrows=1, ncols=5)

data = np.array([
    [151, 37, 28, 16, 9.2],
    [112, 18, 10, 5.8, 3.5],
    [1978, 271, 140, 87, 60],
    [61, 10, 5.7, 3.8, 1.5],
    [993, 169, 97, 68, 22.5]]
)

bar_width = 0.1
space_width = 0.03  # 柱子之间的间距
# index = 0

for index in range(5):
    axes[index].plot(labels, data[index], marker='s', linestyle='-', color='C2', markerfacecolor='C2', markeredgecolor='black', label=labels[index], markersize=8)
    # ax.set_title(datasets[index])  # 设置每个子图的标题为对应的标签
    axes[index].set_xlabel("Number of threads")
    # axes[index].set_xticks(fontsize=25)  # 设置X轴刻度标签的字体大小
    # axes[index].set_yticks(fontsize=25)  # 设置Y轴刻度标签的字体大小
    if index == 0:
        axes[index].set_ylabel("Time cost (seconds)")
    axes[index].set_title(datasets[index])
    axes[index].ticklabel_format(style='sci', axis='y', scilimits=(-2, 2))




figs.tight_layout(rect=[0, 0, 1, 1], h_pad=0, w_pad=-1.1)
# figs.tight_layout(rect=[0, 0, 1, 0.88], h_pad=0, w_pad=0)  # [左, 下, 右, 上] [0,0,1,1]
figs.set_figheight(1.7)
figs.set_figwidth(13)
# plt.show()
figs.savefig('./experiment/thread.pdf', bbox_inches='tight', transparent="True", pad_inches=0.01)
