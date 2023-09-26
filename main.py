from bottle import Bottle, static_file,request,response
import json
import base64

app = Bottle()

STATIC_PATH = "./static"

@app.get('/')
def index():
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return static_file("./xiaoyin.txt", root='./')

@app.get('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root=STATIC_PATH)

@app.get('/admin')
def get_admin():
    return static_file("index.html", root=STATIC_PATH)

@app.post('/admin')
def post_admin():
    body = request.body.read()
    links = json.loads(body.decode('utf-8'))["links"]
    with open("./xiaoyin.txt","wb") as txt:
        txt.write(base64.b64encode(links.encode('utf-8')))
    return "success"

app.run(host='0.0.0.0', port=8035,server="paste")