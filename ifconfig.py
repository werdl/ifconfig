from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_headers():
    info = {}
    info['headers'] = dict(request.headers)
    info['ip'] = request.remote_addr
    info['method'] = request.method
    info['form'] = request.form
    info['port'] = request.environ.get('REMOTE_PORT')
    info['scheme'] = request.scheme
    info['cookies'] = request.cookies
    info['query'] = request.query_string.decode('utf-8')

    strout = json.dumps(info, indent=4)
    print(strout)
    return strout

if __name__ == '__main__':
    app.run(host='0.0.0.0')
