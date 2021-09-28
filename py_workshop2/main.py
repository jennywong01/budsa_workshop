import numpy as np
import pandas as pd
import math

new_score = {}
wb = pd.read_excel("scorebook.xlsx")
dic = dict(wb.values)
print("------------")
print(wb)
print("------------")
print(dic)
print("------------")
print(list(dic.values()))

# print([90, 80, 40, 50] == list(dic.values()))
mean = np.mean(list(dic.values()))
print(mean)
