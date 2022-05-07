import pandas as pd
import numpy as np
import tkinter.filedialog as fd
import os


# x1～y3までの値をCSVから読み込む
"！同じ処理を繰り返すため、forループに入れるのもあり"
x1 = float(data.values[0, 0])
y1 = float(data.values[0, 1])
x2 = float(data.values[0, 4])
y2 = float(data.values[0, 5])
x3 = float(data.values[0, 8])
y3 = float(data.values[0, 9])

# 計算に必要な行列を生成
A = np.matrix([[1, x1, y1, 0, 0, 0],
               [0, 0, 0, 1, x1, y1],
               [1, x2, y2, 0, 0, 0],
               [0, 0, 0, 1, x2, y2],
               [1, x3, y3, 0, 0, 0],
               [0, 0, 0, 1, x3, y3]])

A1 = np.linalg.inv(A)

x = np.matrix([0, 1, 0, 0, 0, 0])
y = np.matrix([0, 0, 0, 0, 0, 1])
z1 = np.matrix([0, 0, 1, 0, 0, 0])
z2 = np.matrix([0, 0, 0, 0, 1, 0])

# 計算結果を格納する配列
calc_res = np.zeros((len(data), 3), dtype=np.float64)
print(calc_res)

for i in range(len(data)):
    # u1～V3までの値をCSVから読み込む
    U1 = float(data.values[i, 2])
    V1 = float(data.values[i, 3])
    U2 = float(data.values[i, 6])
    V2 = float(data.values[i, 7])
    U3 = float(data.values[i, 10])
    V3 = float(data.values[i, 11])

    # 行列を生成
    d = np.matrix([[U1],
                   [V1],
                   [U2],
                   [V2],
                   [U3],
                   [V3]])

    # ひずみを計算
    # Exx:X方向のひずみ
    calc_res[i, 0] = np.dot(np.dot(x, A1), d)
    # Eyy:Y方向のひずみ
    calc_res[i, 1] = np.dot(np.dot(y, A1), d)
    # Exy:XY面のひずみ
    calc_res[i, 2] = np.dot(np.dot(z1, A1), d) + np.dot(np.dot(z2, A1), d)


def read(path):
    # CSVファイル読み込み（上2行、左1列をそれぞれヘッダーとインデックスとする）
    data = pd.read_csv(path,
                       header=1,
                       index_col=0)
    return data


def write(path):
    # 計算結果配列calc_resをDataFrame型に変換し、csvに出力
    pd.DataFrame(calc_res).to_csv(path, encoding="shift_jis")


class Calculate_Strain:
    def __init__(self, input_path, output_path):
        self.progress = 0
        self.in_path = input_path
        self.out_path = output_path
        read(self.in_path)
