'''
#5_1_(1)→〇
def weather():
    return None
#5_1_(2)→〇
def calc_circle_area():
    return float
#5_1_(3)→×(ディクショナリではなくstr型)
def nowstr():
    return dict
#5_1_(4)→〇(リスト，タプル，ディクショナリ)
def nowint():
    return list
#5_1_(5)→×(判定結果(0/1)を返すのでbool型)
def is_leapyear():
    return None
'''
'''
#5_2 → △(やりたいことはできているが表示までは関数でやらない．関数内では判定のみ実施が正答．)
def is_leapyear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f'西暦{year}年は，うるう年です')
    else:
        print(f'西暦{year}年は，うるう年ではありません')

input_year = int(input('西暦で年数を入力>>'))
is_leapyear(input_year)
'''
'''
#5_3 → 〇
def take_bus():
    print('バスに乗ります')
def run():
    print('走ります!')
    walk()              #walk関数をrun関数内で呼び出すよう変更．
def walk():
    print('ちょっと歩きます')

print('行ってきます!')
walk(); take_bus(); run(); run();
print('ただいま')
'''

#5_4(1):×(英語は不要) → 〇
#5_4(2):〇 → 〇
#5_4(3):×(int型の80，要素数1のタプルが渡される) → 〇
#5_4(4):〇 → 〇
#5_4(5):〇 → 〇
'''
#5_5
#元プログラム
amount = int(input('支払総額を入力してください'))
people = int(input('参加人数を入力してください'))

dnum = amount / people       #総額を人数で割る(端数も保持)
pay = dnum // 100 * 100
if dnum > pay:
    pay = int(pay + 100)

payorg = amount - pay * (people - 1)

print('***支払額***')
print(f'1人当たり{pay}円({people}人)，幹事は{payorg}円です')
'''

#再構成後 → 〇
def int_input(data):
    value = int(input(f'{data}を入力してください'))
    return value

def calc_payment(amount, people):
    dnum = amount / people      #1人あたりの支払額を計算
    pay = dnum // 100 * 100     #1人当たりの支払額を100円単位に丸めて切り上げる
    if dnum > pay:              #切り捨てた結果が切り捨て前より小さい場合は100円加算して切り上げ．
        pay = int(pay + 100)
    payorg = amount - pay * (people - 1)
    return pay, payorg

def show_payment(pay, people, payorg):
    print('***支払額***')
    print(f'1人当たり{pay}円({people}人)，幹事は{payorg}円です')
    return None

amount = int_input('支払総額')
people = int_input('参加人数')
(pay, payorg) = calc_payment(amount, people)
show_payment(pay, people, payorg)
