'''
作成日：2025年10月28日
'''

#インポート

#グローバル変数の定義

#関数宣言
def main():
    player = input('プレイヤーを入力してください>')
    print('*** Puzzle & Monsters ***')
    num_defeated = go_dungeon(player)
    print('*** GAME CLEARED!! ***')
    print(f'倒したモンスター数={num_defeated}')

def go_dungeon(player_name):
    print(f'{player_name}はダンジョンに到着した')
    print(f'{player_name}はダンジョンを制覇した')
    return 5

#メイン関数の呼び出し
main()