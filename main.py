import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

app = tk.Tk()
app.geometry("720x300")
app.title("GUI STRAIN CALC.")
app.resizable(0, 0)

# ファイルダイアログ用の拡張子格納配列
typ = [("CSV FILE", "*.csv")]

# プログラム本体の位置を取得
dir = os.path.abspath(os.path.dirname(__file__))

# エラーウィンドウタイトル
title_error_same = "FILE NAME ERROR"

# 入力と出力のファイルパスが同じ場合のエラーメッセージ
msg_error_same = "Please select a different file or location for the input " \
                 "source and output destination. "


# ==============================================================================
# 入力ファイルのBrowseボタン押下時の処理
def browse(mode):
    # src（入力元）モードの場合
    if mode == "src":
        # filedialogのaskopenfilenameを呼び出し
        file_path = fd.askopenfilename(filetypes=typ, initialdir=dir)
        # destのエントリに入力されているファイルパスと比較
        if file_path == dest_box.get():
            mb.showerror(title_error, msg_error_same)
        else:
            src_box.delete(0, tk.END)
            src_box.insert(0, file_path)
    # dest（出力先）モードの場合
    elif mode == "dest":
        file_path = fd.asksaveasfilename(filetypes=typ, initialdir=dir,
                                         initialfile="output.csv",
                                         defaultextension=".csv")
        # srcのエントリに入力されているファイルパスと比較
        if file_path == src_box.get():
            mb.showerror(title_error, msg_error_same)
        else:
            dest_box.delete(0, tk.END)
            dest_box.insert(0, file_path)


# ==============================================================================
# 入出力ファイル選択関連ウィジェット用のフレーム作成
top_frame = tk.Frame(app, relief=tk.GROOVE, pady=10, padx=10)
top_frame.pack(anchor=tk.W)

# ==============================================================================
# 入力用ボックスのラベル
src_label = tk.Label(top_frame, text="Source file", anchor=tk.W)
src_label.grid(row=0, column=0, padx=10)

# 入力用ボックス本体
src_box = tk.Entry(top_frame, width=70)
src_box.grid(row=0, column=1, padx=10)

# 入力ファイル選択ボタン
src_btn = tk.Button(top_frame, width=20, text="Browse...",
                    command=lambda: browse("src"))
src_btn.grid(row=0, column=2, padx=10)

# ==============================================================================
# 出力用ボックスのラベル
dest_label = tk.Label(top_frame, text="Destination file", anchor=tk.W)
dest_label.grid(row=1, column=0, padx=10)

# 出力用ボックス本体
dest_box = tk.Entry(top_frame, width=70)
dest_box.grid(row=1, column=1, padx=10)

# 出力ファイル選択ボタン
dest_btn = tk.Button(top_frame, width=20, text="Browse...",
                     command=lambda: browse("dest"))
dest_btn.grid(row=1, column=2, padx=10)
app.mainloop()
