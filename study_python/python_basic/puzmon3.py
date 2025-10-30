'''
作成日：2025年10月30日
'''

#インポート

#グローバル変数の定義
#属性定義
ELEMENT_SYMBOLS = {
    '火' : '$',
    '水' : '~',
    '風' : '@',
    '土' : '#',
    '命' : '&',
    '無' : ' ',
}
ELEMENT_COLORS = {
    '火' : '1',
    '水' : '6',
    '風' : '2',
    '土' : '3',
    '命' : '5',
    '無' : '7',
}

#関数宣言
def print_monster_name(e_mon):
    monster_name = e_mon['name']
    monster_element = e_mon['element']
    symbol = ELEMENT_SYMBOLS[monster_element]
    color  = ELEMENT_COLORS[monster_element]
    print(f'\033[3{color}m{symbol}{monster_name}{symbol}\033[0m', end='')       #カラー文字表示：\033[3色コードm出力文字列\033[0m  #カラー背景表示：\033[4色コードm出力文字列\033[0m  ※「0\33[0m」はカラー指示リセット．

def do_battle(e_monster):
    print_monster_name(e_monster)
    print(f'が現れた！')
    print_monster_name(e_monster)
    print(f'を倒した！')
    return 1

def go_dungeon(player_name, enemies):
    #e_monsters = ['スライム', 'ゴブリン', 'オオコウモリ', 'ウェアウルフ', 'ドラゴン']
    e_monsters = enemies
    win_cnt = 0
    print(f'{player_name}はダンジョンに到着した')
    #倒したモンスター数カウント
    for mon in e_monsters:
        is_win = do_battle(mon)
        if is_win == True:
            win_cnt += 1
    print(f'{player_name}はダンジョンを制覇した')
    return win_cnt

def main():
    is_player = False
    #プレイヤー名入力および入力確認
    while is_player == False:
        player = input('プレイヤーを入力してください>')
        if player == '':
            print('エラー：プレイヤー名を入力してください．')
        else:
            is_player = True
    #ゲームスタート
    print('*** Puzzle & Monsters ***')
    #敵モンスターの作成
    slime = {
        'name' : 'スライム',
        'hp' : 100,
        'max_hp' : 100,
        'element' : '水',
        'ap' : 10,
        'dp' : 1
    }
    goblin = {
        'name' : 'ゴブリン',
        'hp' : 200,
        'max_hp' : 200,
        'element' : '土',
        'ap' : 20,
        'dp': 5
    }
    giantbat = {
        'name' : 'オオコウモリ',
        'hp' : 300,
        'max_hp' : 300,
        'element' : '風',
        'ap' : 30,
        'dp' : 10
    }
    werewolf = {
        'name' : 'ウェアウルフ',
        'hp' : 400,
        'max_hp' :400,
        'element' : '風',
        'ap' : 40,
        'dp' : 15
    }
    dragon = {
        'name' : 'ドラゴン',
        'hp' : 600,
        'max_hp' : 600,
        'element' : '火',
        'ap' : 50,
        'dp' : 20
    }
    enemies = [slime, goblin, giantbat, werewolf, dragon]
    #倒したモンスター数のカウントおよび表示
    num_defeated = go_dungeon(player, enemies)
    if num_defeated == 5:
        print('*** GAME CLEARED!! ***')
    elif num_defeated < 5:
        print('*** GAME OVER!! ***')
    print(f'倒したモンスター数={num_defeated}')

#メイン関数の呼び出し
main()