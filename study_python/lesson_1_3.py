'''
#code_1_19：pythonにおける変数の型(代入値の型に関係なく変数に対して代入が可能．)
x = '松田'    #str型を代入
print(x)
x = 22      #int型を代入
print(x)
x = 176.5   #float型を代入
print(x,'\n')

#code_1_20：type関数による型の確認
x = 10
print(type(x))
x = '松田'
print(type(x))
x = 175.6
print(type(x),'\n')

#code_1_21：キーボード入力値の型 → str型
price = input('値段を入力>>')
print(type(price),'\n')

#code_1_22：データ型の変換
x = 3.14
y = int(x)
print(y)
print(type(y))
z = str(x)
print(z)
print(type(z))
print(z * 2,'\n')

#code_1_23：キーボード入力値の型変換の必要性(pythonでは数値と文字列の結合は不可能．)
price = input('金額を入力して下さい>>')
price = int(price)
member = input('人数を入力して下さい>>')
member = int(member)
payment = price / member
payment = int(payment)
#print('一人当たりの支払額は' + payment + '円です．\n')
print('一人当たりの支払額は' + str(payment) + '円です.\n')
'''
#code_1_24：文字列に数値を埋め込む
name = '松田光太'
age = 23
height = 175.6
print('私の名前は' + name + 'で，年齢は' + str(age) + '歳，身長は' + str(height)+ 'cmです．\n')
'''
#code_1_25：文字列に数値を埋め込む(format関数，プレースホルダー{})
print('私の名前は{}で，年齢は{}歳，身長は{}cmです．\n'.format(name, age, height))

#code_1_26：割り勘計算プログラム(完成)
price = int(input('金額を入力してください>>'))
member = int(input('人数を入力してください>>'))
payment = int(price / member)
print('支払金額は{}円です．\n'.format(payment))
'''
#code_1_27：文字列に数値を埋め込む(f-string(format関数の後継．python3.6以降でのみ使用可能．))
#code_1-24の値を引用
print(f'私の名前は{name}で，年齢は{age}歳，身長は{height}cmです．')
print(f'私の名前は{name}で，年齢は{age}歳，身長は{height/100}mです．\n')
'''
#column：f-string評価式付き表示
hp, maxHp = 80, 100
print(f'{hp} / {maxHp}')
print(f'{hp = } / {maxHp = }')
print(f'{hp / maxHp = }')
'''
