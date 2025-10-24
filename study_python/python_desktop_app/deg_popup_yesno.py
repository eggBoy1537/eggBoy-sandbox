import TkEasyGUI as eg
#YesかNoを選択するダイアログを表示する．
result = eg.popup_yes_no('猫は好きですか?')
#結果に応じたメッセージを表示
if result == 'Yes':
    eg.popup('猫が好きなんですね')
elif result == 'No':
    eg.popup('猫が好きではないんですね')
