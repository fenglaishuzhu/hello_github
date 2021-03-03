# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

plt.style.use("fivethirtyeight")

size = 0.3
df = pd.read_excel('jianshen.xlsx', '1')

slices = list(df['total'])
labels = list(df['学员'])

patches,l_text,p_text = plt.pie(slices, labels=labels, shadow=True,
                                startangle=90, autopct='%1.1f%%',
                                wedgeprops=dict(width=size, edgecolor='w'))
for t in l_text:
    t.set_size(8)
for t in p_text:
    t.set_size(8)

plt.title("My Awesome Pie Chart")
plt.tight_layout()


plt.show()
