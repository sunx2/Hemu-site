from flask import Flask,render_template, send_from_directory
app = Flask(__name__,static_folder="templates")
import json 

a = json.load(open("channel.json",'r'))
b = json.load(open("video.json",'r'))

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)



    

@app.route('/')
def hello_world():



    return render_template("index.html",items = b,channel=a)

if __name__ == '__main__':
    app.run(debug=True)