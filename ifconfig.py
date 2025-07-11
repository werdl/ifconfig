from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_headers():
    headers = dict(request.headers)
    ip = request.remote_addr
    method = request.method
    agent = request.user_agent
    remote_port = request.environ.get('REMOTE_PORT')
#    scheme = request.headers['nginx-scheme']
    mime = request.content_type
    language = request.accept_languages

    return render_template("index.html", headers=headers, ip=ip, method=method, scheme='http', mime=mime, language=language, agent = agent)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
