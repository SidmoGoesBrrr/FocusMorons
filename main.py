from flask import Flask, request, render_template
from flask_sock import Sock
app = Flask(__name__)
sock=Sock(app)

@app.route('/', methods=['GET', 'POST'])
def main():
    text = ""
    if request.method == 'POST':
        if request.form.get('bch') == 'bch':
            pass


    return render_template("index.html", text=text)
#yeet

@sock.route('/yo')
def reverse(ws):
  while True:
    text=ws.receive()
    ws.send(text[::-1])
if __name__ == '__main__':
    app.run()
