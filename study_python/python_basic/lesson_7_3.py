#code_7_3:mathモジュールをしようする(モジュールの取り込み)
import math                                                 #mathモジュールの取り込みを宣言

print(f'円周率は{math.pi}です')                               #mathモジュールの変数piを参照
print(f'小数点以下を切り捨てれば{math.floor(math.pi)}です')       #mathモジュールの関数floorを呼び出す
print(f'小数点以下を切り上げれば{math.ceil(math.pi)}です\n')        #mathモジュールの関数ceilを呼び出す

#code_7_4:mathモジュールに別名を付けて利用する
import math as m        #モジュールに別名をつける「import モジュール名 as 別名」

print(f'円周率は{m.pi}です')
print(f'小数点以下を切り捨てれば{m.floor(m.pi)}です')
print(f'小数点以下を切り上げれば{m.ceil(m.pi)}です\n')

#code_7_5:特定の変数や関数だけを利用する(取り込み方)
from math import floor      #モジュールmathから関数floorのみを取り込む
from math import pi         #モジュールmathから変数piのみを取り込む

print(f'円周率は{pi}です')                            #取り込んだ変数piを参照．指定して取り込んだ変数はそのまま使用可能．
print(f'小数点以下を切り捨てると{floor(pi)}です\n')       #取り込んだfloor関数の呼び出し．
'''上記で取り込んだもの以外の変数，関数の使用は不可．上記の場合，ceil関数の使用も不可'''

#code_7_6:関数名の重複(特定の変数や関数のみを取り込んだ場合の背反)
from math import log                #mathモジュールからlog関数を取り込む

def log(msg):                       #ログ出力を行う自作のlog関数を定義
    print(f'{msg}を記録します\n')
log(10)                             #対数を求めるつもりが自作'ログ'関数のメッセージ表示機能が出力される．

#code_7_7:特定の変数や関数だけに別名を付けて利用する
from math import pi as ensyuritsu
from math import floor as kirisute

print(f'円周率は{ensyuritsu}')
print(f'小数点以下を切り捨てれば{kirisute(ensyuritsu)}です\n')
'''from モジュール名 import 変数名または関数名 as 別名'''

#code_7_8:ワイルドカードインポートを使ってモジュールを利用する
from math import *      #「from モジュール名 import *」でモジュールのすべての変数，関数を取り込む

print(f'円周率は{pi}です')
print(f'小数点以下を切り捨てれば{floor(pi)}です')
print(f'小数点以下を切り上げれば{ceil(pi)}です\n')
'''取り込んだ変数，関数の把握が難しく，意図しない名前の衝突が起こる可能性が高くなるため使用は非推奨．'''

#まとめ
'''「import モジュール名」，「from モジュール名 import 変数名または関数名」の使用頻度が多いらしい'''

