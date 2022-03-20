# 手順
# $ mkdir file-server
# $ cd file-server
# $ pip install flask
# $ pwd
# (このfile-server.pyファイルをこの↑ディレクトリに置く)
# (test1.csv ファイルをこの↑ディレクトリに置く)(EXCELからエクスポートするとき、UTF-8形式を選んでください)
# $ python3 file-server.py
# ↑これで起動するので、ブラウザで http://localhost:5000/file を開く
# ↑m5stackで開くには ifconfig|grep inet コマンドで表示されるIPアドレスのどれかを指定して
# http://<どれか>:5000/file とすればいいはず



from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Server is Ready"
    return name

@app.route('/hello')
def good():
    name = "Hello World"
    return name

@app.route('/file')
def file():
    path = './test1.csv'  # ← ここにファイルを指定
    out = ''
    with open(path) as f:
        out = f.read()
    return out

@app.route('/file_by_json', methods=['POST'])
def file_by_json():
    json = request.get_json()
    return json.get('path')

@app.route('/question')
def question():
    return request.args.get('value', '')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
