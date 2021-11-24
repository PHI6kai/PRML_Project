import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

p_0 = 0.995  # 未患病概率
p_1 = 0.005
# 设置先验概率

l = [0, 1, 100, 0]
# 设置风险系数，前两个为分成未患病类的风险，后两个为分成患病的风险

file_in = "data_test.csv"

# 读取文件
f = open(file_in, "r", encoding="utf-8")

# 读取浮点数
# dates = f.readlines()
# date=[]
# for i in dates:
#     date.append(i.split())

datas = f.readlines()
li = []
for data in datas:
    # a = np.array(data).astype(float)
    li.append(float(data))
print(li)

# 数据集

def normal(aver, var, x):
    return (np.exp((-1 / 2) * np.square(x - aver) / var)) / (np.sqrt(2 * np.pi * var))


# 正态分布概率密度函数，返回x处的概率值

def R(x):
    temp_0 = normal(7064.4, 2941.3, x) * p_0
    temp_1 = normal(2090.6, 947.3, x) * p_1
    print(temp_0,temp_1)
    temp = temp_0 + temp_1
    # temp_0 = temp_0 / temp
    # temp_1 = temp_1 / temp
    R_0 = temp_0 * l[0] + temp_1 * l[1]
    R_1 = temp_0 * l[2] + temp_1 * l[3]
    return R_0, R_1


# 风险函数，返回一个元组，第一个元素为0类的风险，第二个为1类的风险

r0 = []
r1 = []
for i in li:
    R0, R1 = R(i)
    r0.append(R0)
    r1.append(R1)
    # judge = max(R0, R1)
    if R0>R1 :
        print('数据%f，决策为类型1:患病' % i)
    else:
        print('数据%f，决策为类型0:健康' % i)

r0 = np.array(r0).astype(float)
r1 = np.array(r1).astype(float)
# 遍历数据集，根据最小风险分类

sns.set(font='SimHei')
plt.rcParams['axes.unicode_minus'] = False
ax1 = sns.scatterplot(x=li, y=r0*1e50, label='0', marker="o")
sns.scatterplot(x=li, y=r1*1e50, label='1', marker="o")
ax1.set_xlabel('观察值x')
ax1.set_ylabel('条件风险')
ax1.set_xticks([-5, 5])
plt.show()
# 用seaborn绘图
