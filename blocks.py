import matplotlib.pyplot as plt
import numpy as np
import math

import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rcParams['pdf.fonttype'] = 42
# mpl.rcParams['ytick.labelsize'] = 25
# mpl.rcParams['xtick.labelsize'] = 25

# labels = ['BUP', 'RECEIPT', 'TMA-Ins', 'TMA-Del']

datasets = ['OR', 'g500-22', 'g500-26', 'uni-22', 'uni-26']
labels = ['32', '64', '128', '256']

figs, axes = plt.subplots(nrows=1, ncols=5)

data = np.array([
    [144, 142, 142, 151],  # 0, 20, 5
    [116, 106, 107, 112],  # 30, 60, 10
    [2003, 1987, 1982, 1978],  # 60, 120, 20
    [65, 64, 57, 61],  # 1380, 1460, 20
    [1016, 1083, 978, 993]  # 2900, 3000, 20
]
)

# data2 = np.array([
#     [2026544, 1842253, 1758454, 1723288],
#     [6469881, 5375911, 4991820, 4886827],
#     [7134608, 4665505, 3605154, 3247468],
#     [174443790, 115061433, 87005475, 75136869],
#     [228600601, 157149327, 126748993, 114645331]
# ]
# )

data2 = np.array([
    [12422914, 6886289, 4345797, 3465581],
    [9461331, 6584792, 5268130, 4674521],
    [157768396, 110181933, 86669577, 75775423],
    [8209618, 4704061, 3594986, 3594986],
    [140398399, 78400465, 49207499, 49207468]
]
)

y1lim = [
    (120, 170),
    (90, 140),
    (1970, 2010),
    (45, 75),
    (930, 1130)
]

y2lim = [
    (3300, 13000),
    (4500, 10000),
    (72000, 162000),
    (3200, 8500),
    (45000, 145000)
]


def get_highest_digit_and_offset(num):
    if num < 1.0:
        return 0, 0

    num = int(num)

    cnt = 0
    while num >= 10:
        num //= 10
        cnt += 1

    return num, cnt


def custom_yticks(ax):
    # 获取当前轴的y轴限制
    ymin, ymax = ax.get_ylim()

    # 计算最小值和最大值的最高位数
    highest_max, offset = get_highest_digit_and_offset(ymax)
    highest_min = int(ymin // (10 ** offset))

    # 确定tick的生成方式
    if highest_max - highest_min > 1:
        tick_start = highest_min * (10 ** offset)
        tick_end = highest_max * (10 ** offset)
        ticks = np.arange(tick_start, tick_end + 1, (10 ** offset))
    else:
        tick_start = ymin // ((10 ** offset) / 10) * ((10 ** offset) / 10)
        tick_end = ymax // ((10 ** offset) / 10) * ((10 ** offset) / 10)
        ticks = np.arange(tick_start, tick_end + 1, (10 ** offset) / 10)

    while len(ticks) > 5:
        ticks = [ticks[i] for i in range(len(ticks)) if i % 2 == 0]

    # 设置yticks
    ax.set_yticks(ticks)
    # 设置yticklabels
    # ax.set_yticklabels([f"{tick:.1f}" for tick in ticks])


from matplotlib.lines import Line2D


def add_marker_to_ylabel(ax, label, marker, markersize=10, padding=10, fontsize=12):
    # ylabel
    ax.set_ylabel(label, fontsize=fontsize)

    # 获取 y 轴标签的位置和变换参数
    transform = ax.get_yaxis_transform()

    # 获取 ylabel 的位置
    label_xpos = 0  # y轴的标签通常在0位置（标准化坐标）
    label_ypos = 0.5  # 通常在中点

    # 创建一个 Line2D 对象，用作 marker
    line = Line2D([label_xpos - padding / 72.], [label_ypos], marker=marker, color='blue', markersize=markersize,
                  transform=transform, clip_on=False)

    # 添加这个线对象到坐标轴上
    ax.add_line(line)


bar_width = 0.1
space_width = 0.03  # 柱子之间的间距
for index in range(5):
    axes[index].set_title(datasets[index])
    axes[index].set_xlabel("Slots per block")
    axes[index].plot(labels, data[index], marker='s', linestyle='-', color='C0', markerfacecolor='C0',
                     markeredgecolor='black', markersize=8, label="DRAM usage")
    if index == 0:
        axes[index].set_ylabel('Time cost (seconds)')
        # add_marker_to_ylabel(axes[index], 'xxxx', marker='o')
        # transform = axes[index].get_xaxis_transform()
        # line = Line2D([-10, -10], [0.4, 0.6], marker='o', color='red', transform=transform, clip_on=False)
        # axes[index].add_line(line)
    #

    axes[index].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    axes[index].set_ylim(y1lim[index])

    custom_yticks(axes[index])

    ax2 = axes[index].twinx()
    ax2.plot(labels, data2[index] / 1000, marker='o', linestyle='-', color='C1', markerfacecolor='C1',
             markeredgecolor='black',
             markersize=8, label="SCM usage")
    if index == 4:
        ax2.set_ylabel('Number of blocks')

    ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax2.set_ylim(y2lim[index])

    custom_yticks(ax2)

figs.tight_layout(rect=[0, 0.23, 1, 1], h_pad=0, w_pad=-2.5)
# figs.tight_layout(rect=[0, 0, 1, 0.88], h_pad=0, w_pad=0)  # [左, 下, 右, 上] [0,0,1,1]
figs.set_figheight(2.5)
figs.set_figwidth(15)

# from matplotlib.ticker import FormatStrFormatter
# plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))


import matplotlib.lines as mlines

handles1 = mlines.Line2D([], [], marker='s', linestyle='-', color='C0', markerfacecolor='C0',
                     markeredgecolor='black', markersize=8,)
handles2 = mlines.Line2D([], [], marker='o', linestyle='-', color='C1', markerfacecolor='C1',
                     markeredgecolor='black', markersize=8,)

fig_leg = plt.figlegend(labels=['Insertion Performance', 'LPMB Number of blocks'],
                        loc='lower center',
                        handles=[handles1, handles2],
                        handlelength=2.5,
                        handleheight=1.5,
                        ncol=2)
fig_leg.get_frame().set_edgecolor('black')

# plt.show()
figs.savefig('./experiment/blocks.pdf', bbox_inches='tight', transparent="True", pad_inches=0.01)
