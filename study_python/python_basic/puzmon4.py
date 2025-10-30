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
    e_mon_name = e_mon['name']
    e_mon_element = e_mon['element']
    symbol = ELEMENT_SYMBOLS[e_mon_element]
    color  = ELEMENT_COLORS[e_mon_element]
    print(f'\033[3{color}m{symbol}{e_mon_name}{symbol}\033[0m', end='')       #カラー文字表示：\033[3色コードm出力文字列\033[0m  #カラー背景表示：\033[4色コードm出力文字列\033[0m  ※「0\33[0m」はカラー指示リセット．

def do_battle(e_monster):
    print_monster_name(e_monster)
    print(f'が現れた！')
    print_monster_name(e_monster)
    print(f'を倒した！')
    return 1

def show_party(party_inf):
    a_mon_list = party_inf['味方モンスター']
    print('<パーティ編成>----------------------')
    for a_mon_inf in a_mon_list:
        a_mon_name = a_mon_inf['name']
        a_mon_hp = a_mon_inf['hp']
        a_mon_ap = a_mon_inf['ap']
        a_mon_dp = a_mon_inf['dp']
        a_mon_element = a_mon_inf['element']
        symbol = ELEMENT_SYMBOLS[a_mon_element]
        color = ELEMENT_COLORS[a_mon_element]
        print(f'\033[3{color}m{symbol}{a_mon_name}{symbol}\033[0m HP = {a_mon_hp} 攻撃 = {a_mon_ap} 防御 = {a_mon_dp}')
    print('----------------------------------')
    return None

def go_dungeon(party, enemies):
    win_cnt = 0
    print(f'{party['プレイヤー名']}のパーティ(HP = {party['HP']})はダンジョンに到着した')
    show_party(party)
    #倒したモンスター数カウント
    for mon in enemies:
        is_win = do_battle(mon)
        if is_win == True:
            win_cnt += 1
        if party['HP'] <= 0:
            print(f'{party['プレイヤー名']}はダンジョンから逃げ出した')
            break
        else:
            print(f'{party['プレイヤー名']}はさらに奥へと進んだ')
            print('=======================')
    if win_cnt == 5:
        print(f'{party['プレイヤー名']}はダンジョンを制覇した')
    return win_cnt

def organize_party(player_name, allies):
    hp_list = list()
    max_hp_list = list()
    dp_list = list()
    for a_mon in allies:
        hp_list.append(a_mon['hp'])
        max_hp_list.append(a_mon['max_hp'])
        dp_list.append(a_mon['dp'])

    hp_all = sum(hp_list)
    max_hp_all = sum(max_hp_list)
    dp_all = sum(dp_list) / len(allies)
    party = {
        'プレイヤー名' : player_name,
        '味方モンスター' : allies,
        'HP' : hp_all,
        '最大HP' : max_hp_all,
        '防御力' : dp_all
    }
    return party

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
    #味方モンスターの作成
    bluedragon = {
        'name' : '青龍',
        'hp' : 150,
        'max_hp' : 150,
        'element' : '風',
        'ap' : 15,
        'dp' : 10
    }
    phoenix = {
        'name' : '朱雀',
        'hp' : 150,
        'max_hp' : 150,
        'element' : '火',
        'ap' : 25,
        'dp' : 10
    }
    whitetiger = {
        'name' : '白虎',
        'hp' : 150,
        'max_hp' : 150,
        'element' : '土',
        'ap' : 20,
        'dp' : 5
    }
    blacktortoise = {
        'name' : '玄武',
        'hp' : 150,
        'max_hp' : 150,
        'element' : '水',
        'ap' : 20,
        'dp' : 15
    }
    allies = [bluedragon, phoenix, whitetiger, blacktortoise]
    party = organize_party(player, allies)
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
    num_defeated = go_dungeon(party, enemies)
    if num_defeated == 5:
        print('*** GAME CLEARED!! ***')
    elif num_defeated < 5:
        print('*** GAME OVER!! ***')
    print(f'倒したモンスター数={num_defeated}')

#メイン関数の呼び出し
main()