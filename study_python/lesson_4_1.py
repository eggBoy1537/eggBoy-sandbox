'''
#code_4_1:羊を数えて寝る(繰り返し不使用)
print('さあ，寝ようかしら')
count = 0
count += 1
print(f'羊が{count}匹')
count += 1
print(f'羊が{count}匹')
count += 1
print(f'羊が{count}匹')
print('おやすみなさい\n')

#code_4_2:羊を数えるのを3回繰り返す(while文を使用)
count = 0
while count < 3:
    count += 1                  #while文の中身に入れる内容はインデントに注意．
    print(f'羊が{count}匹')
print('おやすみなさい/n')

#code_4_3:無限ループ
count = 0
while count < 3:
    print(f'羊が{count}匹')
print('おやすみなさい\n')

#code_4_4:眠るまで羊を数えるのをくり返す．(状態で繰り返し実施要否を判定)
is_awake = True                                 #bool型のフラグを意味する変数名は「is_xxx」とするのが一般的．
count = 0
while is_awake == True:
    count += 1
    print(f'羊が{count}匹')
    key = input('もう眠りそうですか？(y/n)>>')
    if key == 'y':
        is_awake = False
print('おやすみなさい/n')

#code_4_5:繰り返いしを使用したリスト作成
count = 0
student_num = int(input('学生の数を入力>>'))
score_list = list()                                         #空のリストを作成．学生の点数を格納する用．
while count < student_num:                                  #入力された学生の数より小さければ繰り返す．
    count += 1
    score = int(input(f'{count}人目の試験の得点を入力>>'))         #1人目から順に点数を入力させる．
    score_list.append(score)                                #リストに点数を追加．
print(score_list)                                           #繰り返し終了後，格納された学生の点数をすべて表示．
total = sum(score_list)                                     #学生の得点の合計を計算．
print(f'平均点は{total / student_num}点です\n')                  #学生の得点の平均点を表示．
'''

#code_4_6:リストの全要素を繰り返し参照する
scores = [80, 20, 75, 60]
count = 0
while count < len(scores):
    if scores[count] >= 60:     #カウンタ変数countを使用してリストをすべてチェックする
        print('合格')
    else:
        print('不合格')
    count += 1



