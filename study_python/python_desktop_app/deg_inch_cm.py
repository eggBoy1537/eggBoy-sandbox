import TkEasyGUI as eg

#ユーザに値を尋ねる
inch_str = eg.popup_get_text('インチからセンチに変換します．何インチですか？')
if inch_str == '' or inch_str is None:
    eg.popup('何も入力されていません')
    quit()
#数値に変換してインチからセンチへ変換
try:
    inch_val = float(inch_str)
except ValueError:
    inch_val = 0
cm_val = inch_val * 2.54
#答えを表示
eg.popup(f'答えは{cm_val}センチです．')
