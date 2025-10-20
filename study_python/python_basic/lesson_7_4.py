#code_7_9:httpパッケージのclientモジュールを取り込む
import http.client      #pythonがwebサーバと通信するためのもの

conn = http.client.HTTPConnection('www.python.org')

#code_7_10:httpパッケージのclientモジュールを取り込む(from利用)
from http import client

conn = client.HTTPConnection('www.python.org')

#code_7_11:httpパッケージのclientモジュールから関数だけを取り込む
from http.client import HTTPConnection

conn = HTTPConnection('www.python.org')

