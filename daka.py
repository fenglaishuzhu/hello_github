# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

plt.style.use("fivethirtyeight")

df = pd.read_excel('打卡总表.xlsx', 'Sheet1')

labels = list(df['name'])
total = list(df['total'])
lose = list(df['lose'])
target = list(df['target'])
width=0.5

plt.bar(labels, target,color='#252422',width=width,label="目标")
plt.bar(labels, lose,color='#fffcf2',width=width,label="遗漏")
plt.bar(labels, total,color="#eb5e28",width=width,label="打卡总数")

#设置数值标签
for x,y in zip(labels, target):
    plt.text(x, y+0.05,'%.f'%y,ha='center',va='bottom')

for x,y in zip(labels, total):
    plt.text(x, y+0.05,'%.f'%y,ha='center',va='bottom',color="#ffffff",fontsize=8)

plt.tight_layout()

plt.xticks(rotation=-30) #设置x轴标签旋转角度
plt.tick_params(axis='x', labelsize=10) #设置x轴标签大小

plt.ylim((0, 30)) #设置y轴范围

plt.legend() #图标

plt.title('Just do it')
plt.xlabel('进击的同学')
plt.ylabel('完成度')
plt.show()
