'''
#code_4_7:for文でリストの全要素を参照する
scores = [80, 20, 75, 60]
for data in scores:     #変数dataにリストscoresの値を順に代入して以降の処理に流れる．
    if data >= 60:
        print('合格')
    else:
        print('不合格')
'''
#code_4_8:for文で決まった回数を繰り返す
for num in range(3):    #range()関数は0から指定した数より1小さい数までの要素をもつ整数列を作成する．3の場合，0,1,2となる．numは記述しているが使用していない．
    print('python')


'''
while文：繰り返し回数の目処がたたないときに使用．
for文：繰り返し回数の目処がたつときに使用．
'''