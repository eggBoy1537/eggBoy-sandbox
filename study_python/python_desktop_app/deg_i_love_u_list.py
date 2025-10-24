#リストの内包記法
#[式 for 変数 in イテラブル]

#リストの内包記法を使って100個の要素を作る
msg_list = [f'{'超' * i}大好き．' for i in range(1, 100 + 1)]
#リストを結合して表示
print(''.join(msg_list))