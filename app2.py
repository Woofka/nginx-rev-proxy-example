from flask import Flask
from flask import request


app = Flask('app2')


@app.route('/', methods=['GET'])
def route_main():
    html = '<h3>app2</h3>'
    html += f'<br>path: {request.path}'
    html += f'<br>args: {request.args}'
    html += f'<br>remote_addr: {request.remote_addr}'
    html += f'<br>Host: {request.headers.get("Host")}'
    html += f'<br>X-Real-Ip: {request.headers.get("X-Real-Ip")}'
    html += f'<br>X-Forwarded-For: {request.headers.get("X-Forwarded-For")}'
    return html


@app.route('/api', methods=['GET'])
def route_api():
    html = '<h3>app2</h3>'
    html += f'<br>path: {request.path}'
    html += f'<br>args: {request.args}'
    html += f'<br>remote_addr: {request.remote_addr}'
    html += f'<br>Host: {request.headers.get("Host")}'
    html += f'<br>X-Real-Ip: {request.headers.get("X-Real-Ip")}'
    html += f'<br>X-Forwarded-For: {request.headers.get("X-Forwarded-For")}'
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
