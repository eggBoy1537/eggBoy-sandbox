import wx

def show_window():
    app = wx.App()          #GUI全体の基盤．
    frame = wx.Frame(None, wx.ID_ANY, '格言を表示するアプリ')     #トップレベルのウィンドウを作成．親ウィンドウは無しNone，wx.ID_ANYは自動でID割り当て，最後の引数はウィンドウのタイトル．
    panel = wx.Panel(frame, wx.ID_ANY)      #フレームの中に設置する部品をおくためのパネルを作成．
    #ラベルを作成
    wx.StaticText(panel, wx.ID_ANY,
                  '以下のボタンを押してください．', pos = (10, 10))    #パネル状に静的テキスト(変更しあいラベル)を作成．posは左上の座標からのオフセット量で設定．
    #ボタンを作成
    button = wx.Button(panel, wx.ID_ANY,
                       '格言を表示', pos = (10, 40))     #ボタンをパネル状に設置．
    button.Bind(wx.EVT_BUTTON, show_message)        #ボタンにイベントハンドラを結びつける．ボタンがクリックされたときにshow_message関数が呼ばれる．
    frame.Show()        #フレーム(ウィンドウ)に画面を表示．これがないとウィンドウは見えない．
    app.MainLoop()      #アプリケーションのイベントループ開始．GUI動作，ユーザの操作を待機する．

def show_message(e):        #イベントハンドラであるため引数e(イベントオブジェクト)を受け取る．
    #メッセージを表示する
    wx.MessageBox('良い言葉によって心が晴れる')      #メッセージボックスを表示．親ウィンドウを指定師弟愛ため，システムが適切に配置する．

if __name__ == '__main__':      #このファイルを直接実行したときのみ動作するよう設定．
    show_window()

    '''
    
    '''