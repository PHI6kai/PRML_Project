## 基于贝叶斯最小错误率决策的分类

import numpy as np
import math

x = [-2.67, -3.55, -1.24, -0.98, -0.79, -2.85,
     -2.76, -3.73, -3.54, -2.27, -3.45, -3.08,
     -1.58, -1.49, -0.74, -0.42, -1.12, 4.25,
     -3.99, 2.88, -0.98, 0.79, 1.19, 3.07]

P_w1 = 0.9
P_w2 = 0.1
x_i = 0

mean1 = -2
std1 = np.sqrt(1.5)
mean2 = 2
std2 = np.sqrt(2)

data_w1 = []
data_w2 = []

for x_i in x:

    P_x_w1 = 1 / (std1 * pow(2 * math.pi, 0.5)) * np.exp(-((x_i - mean1) ** 2) / (2 * std1 ** 2))
    P_x_w2 = 1 / (std2 * pow(2 * math.pi, 0.5)) * np.exp(-((x_i - mean2) ** 2) / (2 * std2 ** 2))

    P_x = P_x_w1 * P_w1 + P_x_w2 * P_w2
    P_w1_x = (P_x_w1 * P_w1) / P_x
    P_w2_x = 1 - P_w1_x

    if P_w1_x > P_w2_x:
        data_w1 = np.append(data_w1, x_i)
    if P_w1_x < P_w2_x:
        data_w2 = np.append(data_w2, x_i)

print("data_w1=", data_w1)
print("data_w2=", data_w2)
