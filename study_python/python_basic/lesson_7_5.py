'''
#code_7_12:matplotlibでリストのデータを可視化する
#%matplotlib inline     #他のIDE(JupyterLab)に必要な記述.PyCharmではエラーが出る．不要．
import matplotlib.pyplot as plt     #pyplotをpltとするのは慣習であり他の名前でも問題ないが慣習に従うのが一般的

weight = [68.4, 68.0, 69.5, 68.4, 68.6, 70.2, 71.4, 70.8, 68.5, 68.6, 68.3, 68.4]
plt.plot(weight, marker = 'o')
plt.title("Weight Trend")
plt.xlabel("Month")
plt.ylabel("Weight[kg]")
plt.grid(True)
plt.show()      #IDEによって記述方法が異なる．PyCharm特有の記述．
'''
'''
#code_7_13:requestsでPythonの公式サイトを取得する
import requests         #パッケージによってはrequestsのようにモジュール名を入れずに取り込めるものも存在．

response = requests.get('https://www.python.org/downloads/')
text = response.text
print(text)
'''

#code_7_14:標準ライブラリを利用したWebページの取得(code_7_13と同じこと標準ライブラリでやってみたパターン)
import http.client      #パッケージ名，モジュール名の指定

conn = http.client.HTTPSConnection('www.python.org')    #関数の指定と引数(URL)：Webページにアクセスするためのオブジェクトを作成
conn.request('GET','/downloads/')           #サーバーにGETリクエストを送信し指定のページを要求
response = conn.getresponse()                           #サーバーからのレスポンスを取得
text = response.read().decode('UTF-8')                  #受け取ったデータを読み取り，UTF-8で文字列にデコード
print(text)                                             #ページの内容(HTML)を出力
conn.close()                                            #接続を閉じる
'''①接続 → ②リクエスト送信 → ③レスポンス受信 → ④表示 → ⑤切断'''