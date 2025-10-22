#7_1_(1):×:組み込み関数が属するモジュールはインポートされている仕様のため．
#7_1_(2):〇
#7_1_(3):×：標準ライブラリから特定の関数の取り込みは可能．
#7_1_(4):〇
#7_1_(5):×：相当量の学習が必要．

#7_2_(1)
#A.func()
#7_2_(2)
#B.func()

#7_3
# from A import func
'''
#7_4_(1)
numbers = list()
for data in range(3):
    number = int(input('整数を入力してください．'))
    numbers.append(number)
#print(numbers)
print(max(numbers))
'''
from operator import truediv

'''
#7_4_(2)
pi = 3.141592
for data in range(5):
    r_pi = round(pi, data)  ##引数の渡し方で戻り値の型が変わる．この場合の引数で桁数を指定しているため，戻り値はfloat型．
    print(r_pi)

#7_4_(2)_解答(小数点第一位を四捨五入した際の答えを整数で表示)
pi = 3.141592
print(round(pi))        #引数の渡し方で戻り値の型が変わる．この場合の戻り値はint型．
for n in range(4):
    print(round(pi, n + 1))
'''

#7_5
'''
#【参考】読み込んだファイルを1行ずつ表示するプログラム
file = open('sample.txt', 'r')
for line in file:
    print(line)
file.close()
'''
'''
#ファイルの記述内容をコピーして転記するプログラム．(ファイルコピーとは違う？)
file = open('sample.txt', 'r', encoding = 'utf-8')          #コピー元ファイルopen(読み取りモード)
file2 = open('copy_sample.txt', 'a', encoding = 'utf-8')    #コピー先ファイルopen(追記モード)
for line in file:                                           #コピー元ファイルの行読み出し
    file2.write(line)                                       #コピー先ファイルに書き込み
file.close()                                                #コピー元ファイルclose
file2.close()                                               #コピー先ファイルclose
'''
'''
#7_6
import random

print('数当てゲームを始めます．3桁の数を当ててください!')
answer = list()
for ans in range(3):
    r_num = random.randint(0, 9)
    answer.append(r_num)
#print(answer)
q = 1
while q == 1:
    prediction = list()
    for num in range(3):
        input_ans = int(input(f'{num + 1}桁目の予想を入力(0 ~ 9)>>'))
        prediction.append(input_ans)

    hit = 0
    ball = 0
    i_cnt = 0
    j_cnt = 0
    for i in answer:
        for j in prediction:
            if i == j and i_cnt == j_cnt:
                hit += 1
            elif i == j and i_cnt != j_cnt:
                ball += 1
            j_cnt += 1
        i_cnt += 1
        j_cnt = 0
    print(f'{hit}ヒット! {ball}ボール!')
    if hit == 3:
        print('正解です!')
        hit = 0
        ball = 0
        break
    else:
        q = int(input('続けますか？ 1:続ける 2:終了 >>'))
'''

#7_6_解答
# randomモジュールのrandint関数を取り込む
from random import randint

print('数当てゲームを始めます．3桁の数を当ててください!')

#正解の作成
answer = list()
for n in range(3):
    answer.append(randint(0, 9))

is_continue = True
while is_continue == True:
    #予想の入力
    prediction = list()
    for n in range(3):
        data = int(input(f'{n + 1}桁目の予想入力(0 ~ 9) >>'))
        prediction.append(data)

    #答え合わせ
    hit = 0
    blow = 0
    for n in range(3):
        if prediction[n] == answer[n]:
            hit += 1
        else:
            for m in range(3):
                if prediction[n] == answer[m]:
                    blow += 1
                    break

    #結果発表
    print(f'{hit}ヒット! {blow}ボール!')
    if hit == 3:
        print('正解です!')
        is_continue = False
    else:
        if int(input('続けますか? 1:続ける 2:終了 >>')) == 2:
            print(f'正解は{answer[0]}{answer[1]}{answer[2]}でした')
            is_continue = False




