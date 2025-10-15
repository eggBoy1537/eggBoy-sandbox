'''
#code_5_13:2つの戻り値を返す? → そう見えるだけで実際は1つ
def plus_and_minus(a, b):
    return a + b, a - b

next, prev = plus_and_minus(1978, 1)
print(next, prev)

#code_5_14:code_5_13は戻り値のタプルをアンパック代入していただけ
def plus_and_minus(a, b):
    return (a + b, a - b)           #実際はタプル．タプルは丸かっこを省略できる．code_5_13は省略していただけ．

(next, prev) = plus_and_minus(1978, 1)      #代入先の変数もタプル
'''
'''
#code_5_15:松田君の食生活を表示する
def eat(breakfast, lunch, dinner):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'夜は{dinner}を食べました')

print('8月1日')
eat('トースト', 'おにぎり', 'カレー')
print('8月2日')
eat('納豆ごはん', 'ラーメン', 'カレー')
print('8月3日')
eat('バナナ', 'そば', '焼肉')
print('8月4日')
eat('サンドイッチ', 'しゅうまい弁当', 'カレー')
'''

#code_5_16:松田君の言うまでもない食生活を表示する(デフォルト引数)


#code_5_17:


#code_5_18:


#code_5_19:


#code_5_20: