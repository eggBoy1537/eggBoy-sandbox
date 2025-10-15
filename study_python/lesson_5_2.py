'''
#code_5_6:hello関数に引数を受け渡す
def hello(name):
    print(f'こんにちは．{name}です．')

hello('浅木')
hello('松田')
'''
'''
#code_5_7:複数の引数を受け渡す
def profile(name, age, hobby):
    print(f'私の名前は{name}です．')
    print(f'年齢は{age}歳です.')
    print(f'趣味は{hobby}です．')

profile('浅木', 24, 'カフェ巡り')
'''
'''
#code_5_8:リストの平均を求めるcalc_average関数
def calc_average(scores):
    avg = sum(scores) / len(scores)
    print(f'平均点は{avg}です')

#code_5_9:input_scores関数とcalc_average関数
def inpu_scores(name):
    print(f'{name}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点?>>'))
    database = int(input('データベースの得点?>>'))
    security = int(input('セキュリティの得点?>>'))
    scores = [network, database, security]

def calc_averagae(scores):
    avg = sum(scores) / len(scores)
    print(f'平均点は{avg}点です')    

#code_5_10:code_5_9の呼び出し
input_scores('浅木')
calc_average(scores)        #input_scores関数内で導出したscoresが関数外に出てきていないため変数scoresが未定義としてエラーとなる．
'''
'''
#code_5_11:足し算結果を返すplus関数
def plus(x, y):
    answer = x + y
    return answer

answer = plus(100, 50)      #変数answerに関数が入る→×，呼び出したplus関数からの戻り値が変数answerに代入される→〇．()は関数呼び出し演算子とよばれる．
print(f'足し算の答えは{answer}です')
'''
'''
#column
def print_name():
    print('名前は工藤です．')
    return None             #戻り値が存在しない関数については明示的に'return None'と表記することもある．
'''

#code_5_12:関数を利用して試験結果を計算する
def input_scores(name):
    print(f'{name}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点?>>'))
    database = int(input('データベースの得点?>>'))
    security = int(input('セキュリティの得点?>>'))
    scores = [network, database, security]
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    return avg

def output_result(name, avg):
    print(f'{name}さんの平均点は{avg}点です．')

asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')

asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)

output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)
