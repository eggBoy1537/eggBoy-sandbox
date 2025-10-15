'''
#code_5_1:見通しの悪いプログラム
student_list = ['浅木', '松田']
for student in student_list:
    print(f'{student}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点?>>'))
    database = int (input('データベースの得点?>>'))
    security = int(input('セキュリティの得点?>>'))
    if student == '浅木':
        asagi_scores = [network, database, security]
        asagi_avg = sum(asagi_scores)/ len(asagi_scores)
    else:
        matsuda_scores = [network, database, security]
        matsuda_avg = sum(matsuda_scores) / len(matsuda_scores)
print(f'浅木さんの平均点は{asagi_avg}点です')
print(f'松田さんの平均点は{matsuda_avg}点です')
'''
'''
#code_5_2:見通しが良くなったプログラム(関数の定義なし，呼び出しの例のみ)
#関数定義(参考資料には記載なし)
#得点入力
def input_scores(student):
    print(f'{student}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点?>>'))
    database = int(input('データベースの得点?>>'))
    security = int(input('セキュリティの得点?>>'))
    scores = [network, database, security]
    return scores
#平均点算出
def calc_average(scores):
    avg_score = sum(scores) / len(scores)
    return avg_score
#結果の出力
def output_result(student, avg_score):
    print(f'{student}さんの平均点は{avg_score}点です')

#得点を入力
asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')
#平均点を計算
asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)
#結果を出力
output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)
'''
'''
#code_5_3:hello関数の定義
def hello():                    #※pythonで既に定義されている関数と同名の関数定義をしてしまうと上書きされてしまい元の関数が使用不可となる．
    print('こんにちは．工藤です')

#code_5_4:hello関数の定義と呼び出し
def hello():
    print('こんにちは．工藤です．')

hello()             #自作関数の呼び出し
'''
'''
#code_5_5:input_scores関数の変数nameに代入するつもり(ローカル変数の独立性)
def input_scores():
    name = ''       #関数内の変数nameは関数の外から独立しており関数の外から変数にアクセスできない．
    print(f'{name}の試験結果を入力してください')

name = '浅木'
input_scores()
name = '松田'
input_scores()
'''