# ML-programs
For beginners
Detecting diabetes in indians 
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
X = dataset[:,0:8]
y = dataset[:,8]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=5, batch_size=10)
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Saved model to disk")

from numpy import loadtxt
from keras.models import model_from_json
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
X = dataset[:,0:8]
y = dataset[:,8]

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.h5")
print("Loaded model from disk")

predictions = model.predict_classes(X)
for i in range(5,10):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
![image](https://github.com/soumyaDev9515/ML-programs/assets/104708894/b29620e6-1a1a-4481-8bf8-ebcaa1361987)

