from flask import Flask, request
from machinelearning import *

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file.save()
        zcr_features = extract_zcr('file.mp3')
        prediction = loaded_rf.predict(np.array([zcr_features]))[0]
        return f'Prediction: {prediction}'
    else:
        return 'Invalid file format'

@app.route('/test')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run()