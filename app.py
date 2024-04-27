from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename.endswith('.txt'):
        return 'hello'
    else:
        return 'Invalid file format'

@app.route('/test')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run()