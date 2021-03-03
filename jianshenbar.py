import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

plt.style.use("fivethirtyeight")

df = pd.read_excel('jianshen.xlsx', '1')

slices = list(df['total'])
labels = list(df['学员'])

labels.reverse()
slices.reverse()

plt.bar(labels, slices)
plt.tight_layout()

plt.show()
