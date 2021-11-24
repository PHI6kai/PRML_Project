from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import re

'''
norm.cdf 返回对应的累计分布函数值
norm.pdf 返回对应的概率密度函数值
norm.rvs 产生指定参数的随机变量
norm.fit 返回给定数据下，各参数的最大似然估计（MLE）值
'''
# file_in = "data_health.csv"
file_in = "data_ill.csv"

# 读取文件
f = open(file_in, "r", encoding="utf-8")

# 读取浮点数
datas = f.readlines()
l = []
for data in datas:
    a = np.array(data).astype(float)
    l.append(a)

# 在这组数据下，正态分布参数的最大似然估计值
x_norm = l
x_mean, x_std = norm.fit(x_norm)
print('mean, ', x_mean)  # 均值
print('x_std, ', x_std)
plt.hist(x_norm, density=True, stacked=True, bins=15)  # 归一化直方图（用出现频率代替次数），将划分区间变为 20（默认 10）
# x = np.linspace(4000, 10000, 70)  # 在在(4000,10000)之间返回均匀间隔的30个数字。
x = np.linspace(1000, 3000, 70)
plt.plot(x, norm.pdf(x), 'r-')
plt.show()
