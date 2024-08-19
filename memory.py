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
    np.array([248458280, 137725780, 86915940, 69311620]) / (1024 * 1024),
    np.array([189226620, 131695840, 105362600, 93490420]) / (1024 * 1024),
    np.array([3155367920, 2203638660, 1733391540, 1515508460]) / (1024 * 1024),
    np.array([164192360, 94081220, 71899720, 71899720]) / (1024 * 1024),
    np.array([2807967980, 1568009300, 984149980, 984149360]) / (1024 * 1024)
]
)

data2 = np.array([
    np.array([1590132992, 1762889984, 2225048064, 3548754944]) / (1024 * 1024),
    np.array([1211050368, 1685706752, 2697282560, 4786709504]) / (1024 * 1024),
    np.array([20194354688, 28206574848, 44374823424, 77594033152]) / (1024 * 1024),
    np.array([1050831104, 1204239616, 1840632832, 3681265664]) / (1024 * 1024),
    np.array([17970995072, 20070519040, 25194239488, 50388447232]) / (1024 * 1024)
]
)

y1lim = [
    (60, 250),
    (88, 190),
    (1500, 3200),
    (65, 170),
    (980, 3000)
]

y2lim = [
    (0, 3.6),
    (0, 5),
    (0, 80),
    (0.9, 4),
    (15, 50)
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
        ticks = np.arange(tick_start, tick_end + 0.1, (10 ** offset) / 10)

    while len(ticks) > 5:
        ticks = [ticks[i] for i in range(len(ticks)) if i % 2 == 0]

    # 设置yticks
    ax.set_yticks(ticks)
    # 设置yticklabels
    # ax.set_yticklabels([f"{tick:.1f}" for tick in ticks])


bar_width = 0.1
space_width = 0.03  # 柱子之间的间距
for index in range(5):
    axes[index].set_title(datasets[index])
    axes[index].set_xlabel("Slots per block")
    axes[index].plot(labels, data[index], marker='s', linestyle='-', color='C4', markerfacecolor='C4',
                     markeredgecolor='black', markersize=8, label="DRAM usage")
    if index == 0:
        axes[index].set_ylabel('DRAM Usage (MB)')
    # axes[index].ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    axes[index].set_ylim(y1lim[index])

    custom_yticks(axes[index])

    ax2 = axes[index].twinx()
    ax2.plot(labels, data2[index] / 1000, marker='o', linestyle='-', color='C3', markerfacecolor='C3',
             markeredgecolor='black',
             markersize=8, label="SCM Usage")
    if index == 4:
        ax2.set_ylabel('SCM Usage (GB)')

    # ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax2.set_ylim(y2lim[index])

    custom_yticks(ax2)

figs.tight_layout(rect=[0, 0.23, 1, 1], h_pad=0, w_pad=-2.3)
# figs.tight_layout(rect=[0, 0, 1, 0.88], h_pad=0, w_pad=0)  # [左, 下, 右, 上] [0,0,1,1]
figs.set_figheight(2.5)
figs.set_figwidth(15)

import matplotlib.lines as mlines

handles1 = mlines.Line2D([], [], marker='s', linestyle='-', color='C4', markerfacecolor='C4',
                         markeredgecolor='black', markersize=8, )
handles2 = mlines.Line2D([], [], marker='o', linestyle='-', color='C3', markerfacecolor='C3',
                         markeredgecolor='black', markersize=8, )

fig_leg = plt.figlegend(labels=['DRAM Usage (MB)', 'SCM Usage (GB)'],
                        loc='lower center',
                        handles=[handles1, handles2],
                        handlelength=2.5,
                        handleheight=1.5,
                        ncol=2)
fig_leg.get_frame().set_edgecolor('black')

# from matplotlib.ticker import FormatStrFormatter
# plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

# plt.show()
figs.savefig('./experiment/memory.pdf', bbox_inches='tight', transparent="True", pad_inches=0.01)
