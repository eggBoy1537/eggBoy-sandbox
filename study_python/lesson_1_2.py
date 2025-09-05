#code_1-10：変数への代入
name    = '松田'
age     = 22
print(name)
print(age,'\n')

#code_1_11：変数を用いた円周の計算
print('半径が3cmの円の直径は，')
dia = 3*2
print(dia)
print('その円の円周は，')
print(dia * 3.14,'\n')

#code_1_13：アンパック代入(まとめて代入),変数の上書き
name,age = '浅木',21
print(name,age,'\n')

#code_1_15：自分自身への代入
print('浅木さんの今年の年齢は，')
print(age)
print('来年の年齢は，')
age = age + 1
print(age)
print('再来年の年齢は，')
age = age + 1
print(age,'\n')

#code_1_16：複合代入演算子
age = 24
print(age)
age += 1
print(age)
price = 1000
print(price)
price *= 1.5
print(price,'\n')

#code_1_17：キーボード入力値の代入変数名 = input(文字列)
name = input('名前を入力してください>>')
print('おお' + name + 'よ，そなたを待っていた！\n')

#column：予約語の確認方法
import keyword
print(keyword.kwlist)
