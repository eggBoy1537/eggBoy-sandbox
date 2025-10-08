#2_1
'''
(1)ディクショナリ
(2)リスト
(3)セット
(4)セット
(5)リスト× → ディクショナリ(座席番号をキーとする)
'''

'''

#2_2
subject = {'国語':0, '算数':0, '理科':0, '社会':0, '英語':0}
subject['国語'] = int(input('国語の点数を入力してください：'))
subject['算数'] = int(input('算数の点数を入力してください：'))
subject['理科'] = int(input('理科の点数を入力してください：'))
subject['社会'] = int(input('社会の点数を入力してください：'))
subject['英語'] = int(input('英語の点数を入力してください：'))
total   = sum(subject.values())
ave     = total / len(subject)
print(total,ave)

#2_2_解答(ディクショナリではなくリストでOK．出力処理は1行で記述可能．)
score = []
score.append(int(input('国語の点数>>>')))
score.append(int(input('算数の点数>>>')))
score.append(int(input('理科の点数>>>')))
score.append(int(input('社会の点数>>>')))
score.append(int(input('英語の点数>>>')))
print(f'合計{sum(score)}点 平均{sum(score)/len(score)}点')
'''

#2_3
A_hobbies = {'自転車','ランニング','キャンプ','ゲーム','犬'}
B_hobbies = {'キャンプ','サーフィン','スノボ―','ゲーム','猫'}
print('こころの準備ができたらEnterキーを押してください．')
input()
intersection_hobbies = A_hobbies & B_hobbies
union_hobbies = A_hobbies | B_hobbies
match_rate = (len(intersection_hobbies) / len(union_hobbies)) * 100
print(f'相性度：{match_rate}%')

#2_3_解答(入力待ちの仕方に無駄あり．それ以外は同じ処理を実現できている．)
player_1 = {'読書', '昼寝', '映画鑑賞', '散歩', '料理'}
player_2 = {'テニス', '将棋', '料理', '読書', '旅行'}
input('心の準備ができたらEnterキーを押してください')
common = player_1 & player_2
total = player_1 | player_2
compatibility_rate = len(common) / len(total) * 100
print(f'相性度は{compatibility_rate}パーセントでした')