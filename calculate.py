import pandas as pd
import numpy as np
import time


def write(path, w_data):
    # 計算結果配列calc_resをDataFrame型に変換し、csvに出力
    pd.DataFrame(w_data).to_csv(path, encoding="shift_jis")


class Calculate_Strain:
    def __init__(self, input_path, output_path):
        self.in_process = True
        self.progress = 0
        self.in_path = input_path
        self.out_path = output_path
        # CSVファイル読み込み（上2行、左1列をそれぞれヘッダーとインデックスとする）
        self.data = pd.read_csv(self.in_path, header=1, index_col=0)

    def calc_strain(self):
        self.in_process = True

        # 計算に必要な変数の生成
        x1 = float(self.data.values[0, 0])
        y1 = float(self.data.values[0, 1])
        x2 = float(self.data.values[0, 4])
        y2 = float(self.data.values[0, 5])
        x3 = float(self.data.values[0, 8])
        y3 = float(self.data.values[0, 9])

        # 計算に必要な行列を生成
        a = np.matrix([[1, x1, y1, 0, 0, 0],
                       [0, 0, 0, 1, x1, y1],
                       [1, x2, y2, 0, 0, 0],
                       [0, 0, 0, 1, x2, y2],
                       [1, x3, y3, 0, 0, 0],
                       [0, 0, 0, 1, x3, y3]])

        a1 = np.linalg.inv(a)

        x = np.matrix([0, 1, 0, 0, 0, 0])
        y = np.matrix([0, 0, 0, 0, 0, 1])
        z1 = np.matrix([0, 0, 1, 0, 0, 0])
        z2 = np.matrix([0, 0, 0, 0, 1, 0])

        # 計算結果を格納する配列
        calc_res = np.zeros((len(self.data), 3), dtype=np.float64)

        for i in range(len(self.data)):
            # u1～V3までの値をCSVから読み込む
            u1 = float(self.data.values[i, 2])
            v1 = float(self.data.values[i, 3])
            u2 = float(self.data.values[i, 6])
            v2 = float(self.data.values[i, 7])
            u3 = float(self.data.values[i, 10])
            v3 = float(self.data.values[i, 11])

            # 行列を生成
            d = np.matrix([[u1],
                           [v1],
                           [u2],
                           [v2],
                           [u3],
                           [v3]])

            # ひずみを計算
            # Exx:X方向のひずみ
            calc_res[i, 0] = np.dot(np.dot(x, a1), d)
            # Eyy:Y方向のひずみ
            calc_res[i, 1] = np.dot(np.dot(y, a1), d)
            # Exy:XY面のひずみ
            calc_res[i, 2] = np.dot(np.dot(z1, a1), d) + np.dot(np.dot(z2, a1),
                                                                d)

            self.progress = 100 * (i + 1) / len(self.data)
            time.sleep(0.0005)

        # プロセスフラグをFalseに変更
        self.in_process = False

        write(self.out_path, calc_res)
