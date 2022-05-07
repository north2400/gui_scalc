# gui_scalc
GUI strain calculation tool from csv to csv

## ● Abstract 
とあるソフトから出力されるCSVファイルの座標から、歪を計算して別のCSVに計算結果を出力するプログラムです。
個人用に作成したソフトのため、使用・改変は自己責任でお願いします。<br><br>

リポジトリ内に個人情報が含まれている場合がありますが、悪用厳禁でお願いします。<br>
学術計算の手助けとなれば幸いです。

## ● How to Use
### 1.dist内のscalc.exeを実行
### 2.source fileに計算したいCSVファイルを選択
### 3.destination fileに出力ファイル名を入力（BrowseからGUI操作可能）
### 4.Calculateボタンをクリック

## ● Other
プログレスバーを表示するのに手こずりました。もっと良い方法があればいいのですが、、、
とりあえず動くので暫定版を公開します。
プログレスバーの動作確認のため、time.sleep()で計算スピードを落としています。
待てない人は、calculate.pyのtime.sleep(0.0005)を削除してください。
欲しければ、計算スピードを落としていないexeも作ります。
