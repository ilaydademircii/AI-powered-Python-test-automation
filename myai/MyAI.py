'''
Created on 7 Ağu 2024

@author: zehra
'''
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from flask import Flask, request, jsonify

# Veri oluşturma
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Modeli oluşturma
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Modeli derleme
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Modeli eğitme
model.fit(X, y, epochs=1000, verbose=0)

# Flask uygulaması
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(np.array(data['input']))
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
