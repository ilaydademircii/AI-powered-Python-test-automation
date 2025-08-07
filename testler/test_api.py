'''
Created on 1 Ağu 2024

@author: zehra
'''
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'Test Scenario API is running.'


@app.route('/generate_tests', methods=['POST'])
def generate_tests():
    data = request.json
    if 'file_content' not in data:
        return jsonify({'status': 'error', 'message': 'No file content provided'})
    
    file_content = data['file_content']
    
    # Test senaryolarını oluştur
    test_scenarios = create_test_scenarios(file_content)
    
    return jsonify({'status': 'success', 'test_scenarios': test_scenarios})


def create_test_scenarios(file_content):
    # Basit bir örnek olarak, her satır için ters çevirme testi oluşturuyoruz
    lines = file_content.split('\n')
    test_scenarios = [{'input': line, 'expected_output': line[::-1]} for line in lines if line]
    return test_scenarios


if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Portu 5001 olarak ayarlıyoruz
