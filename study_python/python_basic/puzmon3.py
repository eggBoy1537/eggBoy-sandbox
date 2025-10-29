'''
作成日：2025年10月30日
'''

#インポート

#グローバル変数の定義

#関数宣言
def do_battle(e_monster):
    print(f'{e_monster}が現れた！')
    print(f'{e_monster}を倒した！')
    return 1


def go_dungeon(player_name, enemy):
    e_monsters = ['スライム', 'ゴブリン', 'オオコウモリ', 'ウェアウルフ', 'ドラゴン']
    win_cnt = 0
    print(f'{player_name}はダンジョンに到着した')
    #倒したモンスター数カウント
    for mon in e_monsters:
        is_win = do_battle(mon)
        if is_win == True:
            win_cnt += 1
    print(f'{player_name}はダンジョンを制覇した')
    return 5

def main():
    is_player = False
    #プレイヤー名入力
    while is_player == False:
        player = input('プレイヤーを入力してください>')
        if player == '':
            print('エラー：プレイヤー名を入力してください．')
        else:
            is_player = True
    #ゲームスタート
    print('*** Puzzle & Monsters ***')
    #敵モンスターの作成


    num_defeated = go_dungeon(player)
    if num_defeated == 5:
        print('*** GAME CLEARED!! ***')
    elif num_defeated < 5:
        print('*** GAME OVER!! ***')
    print(f'倒したモンスター数={num_defeated}')

#メイン関数の呼び出し
main()