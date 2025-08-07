'''
Created on 2 Ağu 2024

@author: zehra
'''

from runtheresponse import RunResponse
from openaiIslemleri import OpenAIIslem
from flask import Flask
import  time

app = Flask(__name__)

api_key = "*******"

# Dosya yollarını belirtin
input_dosya_yolu = 'C:/Users/zehra/demo/testler/hello2.py'
output_dosya_yolu = 'C:/Users/zehra/demo/Calistir.py'

# OpenAIIslemleri sınıfını kullanarak işlemleri gerçekleştirin

print("OpenAIIslemleri sınıfını kullanarak işlemleri gerçekleştirin")
openai_islemleri = OpenAIIslem.OpenAIIslemleri(api_key, input_dosya_yolu, output_dosya_yolu)
openai_islemleri.openai_cevapla()

run_response = RunResponse.RunResponseClass(output_dosya_yolu)

print("Calistir uygulamasına istek gönder")
# Wait for the server to start
time.sleep(5)

    
@app.route('/')
def home():
    # Execute the test code dynamically
    print("Home route accessed")
    return  run_response.calistir() + "  \n\nTest başarıyla geçildi" 


@app.route('/about')
def about():
    return 'About Page'

if __name__ == '__main__':
    app.run(port=5001)
