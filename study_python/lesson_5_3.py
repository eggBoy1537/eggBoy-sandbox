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
'''
#code_5_16:松田君の言うまでもない食生活を表示する(デフォルト引数)
def eat(breakfast, lunch, dinner = 'カレー'):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')

print('8月1日')
eat('トースト', 'おにぎり')
print('8月2日')
eat('納豆ごはん', 'ラーメン')
print('8月3日')
eat('バナナ', 'そば', '焼肉')
print('8月4日')
eat('サンドイッチ','しゅうまい弁当')
'''
'''
#code_5_16(NG版):デフォルト引数を使用する場合には必ず一番後ろから順にデフォルト値を指定するようにする．
def eat(breakfast = 'トースト', lunch, dinner):     #デフォルト引数の制約「デフォルト引数が指定された仮引数より後ろに，デフォルト引数がない仮引数を定義してはならない」より，エラーとなる．
'''
'''
#code_5_17:夜がカレーじゃない日のeat関数の呼び出し(引数のキーワード指定)
def eat(breakfast, lunch = 'ラーメン', dinner = 'カレー'):
    print(f'{breakfast}を食べました')
    print(f'{lunch}を食べました')
    print(f'{dinner}を食べました')

eat('納豆ごはん', 'ラーメン', 'カレーうどん')      #ラーメンを省略したいところだが，省略すると昼がカレーうどん，夜がカレーとなってしまう．

#code_5_18:夜がカレーじゃない日のeat関数の呼び出し(キーワード指定のやり方)
#下記のようにキーワードを指定することで順不同でも意図した引数を渡すことが可能．キーワード指定なしの実引数は，前から順に仮引数に渡される．
eat(breakfast = '納豆ごはん', dinner = 'カレーうどん')
eat(dinner = 'カレーうどん', breakfast = '納豆ごはん')
eat('納豆ごはん', dinner = 'カレーうどん')
'''

#code_5_19:おやつも食べた日のeat関数の呼び出し
def eat(breakfast, lunch, dinner = 'カレー', desserts = ()):       #おやつはタプルで受けることを表明
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')
    for d in desserts:
        print(f'おやつに{d}を食べました')
        
eat('トースト', 'パスタ', 'カレー', ('アイス', 'チョコ', 'パフェ'))        #呼び出しでは丸かっこでタプルとすることが必要．


#code_5_20:おやつも食べた日のeat関数の呼び出し(可変長引数の利用)
def eat(breakfast, lunch, dinner = 'カレー', *desserts):       #dessertsは可変長引数を表明
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩が{dinner}を食べました')
    for d in desserts:
        print(f'おやつに{d}を食べました')
        
eat('トースト', 'パスタ', 'カレー', 'アイス', 'チョコ', 'カレー')      #後半３つがタプルとして仮引数dessertsに渡される．

'''
#column:ディクショナリを用いた可変長引数:仮引数の前につける「*」を2つにすると実引数をディクショナリとして受け取り可能．
def eat(**kwargs):
    for key in kwargs:
        print(f'{key}に{kwargs[key]}を食べました')
eat(朝食 = '納豆', 遅めの昼食 = 'パスタ', 夕方のおやつ = 'カレーパン')
'''