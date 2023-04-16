from keras.datasets import mnist
import matplotlib.pyplot as plt

(x_train, y_train),(x_test,y_test)=mnist.load_data()

#->čudna pretvorba 2 v [0 0 1 0 0 0 0 0 0 0]; 5 v [0 0 0 0 0 1 0 0 0 0]; 4 v [0 0 0 0 1 0 0 0 0 0]
from keras.utils.np_utils import to_categorical
y_cat_test=to_categorical(y_test, 10) #->čudna pretvorba 2 v [0 0 1 0 0 0 0 0 0 0]; 5 v [0 0 0 0 0 1 0 0 0 0]
x_test=x_test/x_test.max()
x_test=x_test.reshape(10000,28,28,1)


# Naloži modul
from keras.models import load_model
model=load_model('cnnModel.h5')

# Začni testirati model
model.evaluate(x_test, y_cat_test)

# Now make a prediction
from sklearn.metrics import classification_report
import numpy as np

predictions = model.predict(x_test)

for i in range(len(predictions)):
    for j in range(len(predictions[i])):
       if predictions[i][j] > 0.5:
          predictions[i][j]=1 
       else:
          predictions[i][j]=0

print(classification_report(y_cat_test, predictions))