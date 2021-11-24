from scipy.stats import norm
import numpy as np

# 生成健康样本

f_health = open("data_health.csv", mode="w+", encoding="utf-8")

x_norm = norm.rvs(loc=7000, scale=3000, size=9500)

print(x_norm)

for i in x_norm:
    f_health.write(f"{abs(round(i,1))}\n")

f_health.close()

# 生成患病样本

f = open("data_ill.csv", mode="w+", encoding="utf-8")

x_norm = norm.rvs(loc=2000, scale=1000, size=500)

print(x_norm)

for i in x_norm:
    f.write(f"{abs(round(i,1))}\n")

f.close()























# # f.close()
#
# f = open("data.txt", mode="r", encoding="utf-8")
#
# line = f.readline()  # 以行的形式进行读取文件
# list1 = []
# while line:
#     m = line.split()
#     n = m[0:1]  # 这是选取需要读取的位数
#     list1.append(m)  # 将其添加在列表之中
#     line = f.readline()
#
# a = list1[2] #加一个for
# # a = float(np.array(a))
# a = np.array(a).astype(float)
# a = np.round(a, 1)
#
# print(a)


