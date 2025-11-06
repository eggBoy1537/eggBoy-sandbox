'''
作成日：2025年11月6日
'''

#インポート
import random

#グローバル変数の定義
#属性定義
ELEMENT_SYMBOLS = {
    '火' : '$',      #$🔥
    '水' : '~',      #~💧
    '風' : '@',      #@🌀
    '土' : '#',      ##🏜
    '命' : '&',      #&🧡
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
#ユーティリティ関数
def print_monster_name(mon):
    global ELEMENT_SYMBOLS, ELEMENT_COLORS
    mon_name = mon['name']
    mon_element = mon['element']
    symbol = ELEMENT_SYMBOLS[mon_element]
    color  = ELEMENT_COLORS[mon_element]
    print(f'\033[4{color}m{symbol}{mon_name}{symbol}\033[0m ', end='')       #カラー背景表示：\033[4色コードm出力文字列\033[0m  #カラー背景表示：\033[4色コードm出力文字列\033[0m  ※「0\33[0m」はカラー指示リセット．
    return None

def fill_gems():
    global ELEMENT_SYMBOLS, ELEMENT_COLORS

    return None

#メイン関数
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
    bluedragon = {'name' : '青龍', 'hp' : 150, 'max_hp' : 150, 'element' : '風', 'ap' : 15, 'dp' : 10}
    phoenix = {'name' : '朱雀', 'hp' : 150, 'max_hp' : 150, 'element' : '火', 'ap' : 25, 'dp' : 10}
    whitetiger = {'name' : '白虎', 'hp' : 150, 'max_hp' : 150, 'element' : '土', 'ap' : 20, 'dp' : 5}
    blacktortoise = {'name' : '玄武', 'hp' : 150, 'max_hp' : 150, 'element' : '水', 'ap' : 20, 'dp' : 15}
    allies = [bluedragon, phoenix, whitetiger, blacktortoise]
    party = organize_party(player, allies)
    #敵モンスターの作成
    slime = {'name' : 'スライム', 'hp' : 100, 'max_hp' : 100, 'element' : '水', 'ap' : 10, 'dp' : 1}
    goblin = {'name' : 'ゴブリン', 'hp' : 200, 'max_hp' : 200, 'element' : '土', 'ap' : 20, 'dp': 5}
    giantbat = {'name' : 'オオコウモリ', 'hp' : 300, 'max_hp' : 300, 'element' : '風', 'ap' : 30, 'dp' : 10}
    werewolf = {'name' : 'ウェアウルフ', 'hp' : 400, 'max_hp' :400, 'element' : '風', 'ap' : 40, 'dp' : 15}
    dragon = {'name' : 'ドラゴン', 'hp' : 600, 'max_hp' : 600, 'element' : '火', 'ap' : 50, 'dp' : 20}
    enemies = [slime, goblin, giantbat, werewolf, dragon]
    #倒したモンスター数のカウントおよび表示
    num_defeated = go_dungeon(party, enemies)
    if num_defeated == 5:
        print('*** GAME CLEARED!! ***')
    else:
        print('*** GAME OVER!! ***')
    print(f'倒したモンスター数={num_defeated}')

#ビジネスロジック関数
def organize_party(player_name, allies):
    hp_all = sum([a_mon['hp'] for a_mon in allies])
    max_hp_all = sum([a_mon['max_hp'] for a_mon in allies])
    dp_all = sum([a_mon['dp'] for a_mon in allies]) / len(allies)
    party = {'プレイヤー名' : player_name, '味方モンスター' : allies, 'HP' : hp_all, '最大HP' : max_hp_all, '防御力' : dp_all}
    return party

def go_dungeon(party, enemies):
    win_cnt = 0
    print(f'{party['プレイヤー名']}のパーティ(HP = {party['最大HP']})はダンジョンに到着した')
    show_party(party)
    #倒したモンスター数カウント
    for mon in enemies:
        win_cnt += do_battle(party, mon)
        if party['HP'] <= 0:
            print(f'{party['プレイヤー名']}はダンジョンから逃げ出した')
            return win_cnt
        else:
            print(f'{party['プレイヤー名']}はさらに奥へと進んだ')
            print('=======================')
    print(f'{party['プレイヤー名']}はダンジョンを制覇した')
    return win_cnt

def show_party(party_inf):
    a_mon_list = party_inf['味方モンスター']
    print('<パーティ編成>----------------------')
    for a_mon in a_mon_list:
        print_monster_name(a_mon)
        print(f'HP = {a_mon['hp']} 攻撃 = {a_mon['ap']} 防御 = {a_mon['dp']}')
    print('----------------------------------')
    return None

def do_battle(party, e_mon):
    print_monster_name(e_mon)
    print(f'が現れた！')
    #バトルフィールドの作成
    bf = {'A' : ' ', 'B' : ' ', 'C' : ' ', 'D' : ' ', 'E' : ' ', 'F' : ' ', 'G' : ' ',
                    'H' : ' ', 'I' : ' ', 'J' : ' ', 'K' : ' ', 'L' : ' ', 'M' : ' ', 'N' : ' ', }
    while True:
        on_player_turn(party, e_mon)
        if e_mon['hp'] <= 0:
            break
        on_enemy_turn(party, e_mon)
        if party['HP'] <= 0:
            print(f'パーティのHPは0になった')
            return 0                            #パーティが負けた時は倒した敵の数をカウントアップしないため0を返して即関数から抜ける．
    print_monster_name(e_mon)
    print(f'を倒した！')
    return 1

def on_player_turn(party, e_mon):
    print(f'【{party['プレイヤー名']}のターン】（HP = {party['HP']} / {party['最大HP']}）')
    print('バトルフィールド')
    print_monster_name(e_mon)
    print(f'HP = {e_mon['hp']} / {e_mon['max_hp']}\n')
    a_mon_list = party['味方モンスター']
    for a_mon_name in a_mon_list:
        print_monster_name(a_mon_name)
    print(f'\nHP = {party['HP']} / {party['最大HP']}')
    show_battle_field()
    cmd = input('コマンド? >> ')
    do_attack(e_mon, cmd)
    return None

def show_battle_field():
    print_gems()
    return None

def print_gems():
    print('---------------------------')

    print('---------------------------')
    return None

def do_attack(e_mon, command):
    base_dmg = hash(command) % 50                                   #入力コマンドをハッシュ関数で変換し基準ダメージを計算．
    dmg = int(random.uniform(base_dmg * 0.9, base_dmg * 1.1))       #実際に敵に与えるダメージは基準ダメージの±10%．小数点以下切り捨て．
    e_mon['hp'] -= dmg
    print(f'ダミー攻撃で相手に{dmg}のダメージを与えた\n')
    return None

def on_enemy_turn(party, e_mon):
    print(f'【', end = '')
    print_monster_name(e_mon)
    print(f'のターン】（HP = {e_mon['hp']} / {e_mon['max_hp']}）')
    do_enemy_attack(party)
    return None

def do_enemy_attack(party):
    dmg = 200
    party['HP'] -= dmg
    print(f'{dmg}のダメージを受けた\n')
    return None

#メイン関数の呼び出し
main()