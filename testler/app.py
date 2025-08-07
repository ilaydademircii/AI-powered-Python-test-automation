'''
Created on 1 Ağu 2024

@author: zehra
'''
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

YOUR_API_URL = 'https://example.com/generate_tests'  # Buraya API URL'inizi girin


@app.route('/')
def home():
    return 'Flask API is running.'


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'})

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    
    # Dosya içeriğini oku
    file_content = file.read().decode('utf-8')
    
    # Dosya içeriğini belirttiğiniz API'ye gönder
    response = send_file_content_to_api(file_content)
    
    return jsonify(response)


def send_file_content_to_api(file_content):
    # API'ye dosya içeriğini gönder
    data = {'file_content': file_content}
    response = requests.post(YOUR_API_URL, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'error', 'message': 'Failed to communicate with the API'}


if __name__ == '__main__':
    app.run(debug=True)
