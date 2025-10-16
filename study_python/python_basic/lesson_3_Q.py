#3_1
'''
(1)priceの1.1倍が30000以下であれば成立
(2)演算子が不適．==と表記すべき．
(3)kansaiという変数にgihuという文字列が含まれていれば成立
(4)a+bが60より大きいかつdayが3の時に成立
(5)不成立(0)の場合成立．
'''

#3_2
'''
(1)initial == 'K'
(2)point >= 80 and point < 256
(3)bmi < 20 or bmi > 25
(4)year % 4 == 0
(5)day != 28 and day != 30 and day != 31
   not(day in [28,30,31])

#3_3_(1)
isError = False
n = 10
if isError == False and n < 100:
    print('OK')

#3_3_(2)
value = int(input('数字を入力してください>>'))
if value % 2 == 0:
    print('入力値は「偶数」')
else:
    print('入力値は「奇数」')
'''
#3_3_(2)別解：三項条件演算子を利用した表現(値X if 条件式 else 値Y)
value = int(input('数字を入力してください>>'))
div = '偶数' if value % 2 == 0 else '奇数'      #条件成立で'偶数'，不成立で'奇数'を表示．
print(f'{div}です')
'''
#3_3_(3)
greet = input('入力してください>>')
if 'こんにちは' in greet:
    print('ようこそ!')
elif '景気は?' in greet:
    print('ぼちぼちです．')
elif 'さようなら' in greet:
    print('お元気で!')
else:
    print('どうしました？')
'''

#3_4
'''
ブロック①：1,3,5,7,8,10,12
ブロック②：2以外× → 4,6,9,11
ブロック③：2
'''
