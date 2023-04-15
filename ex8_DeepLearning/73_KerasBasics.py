import numpy as np
from numpy import genfromtxt

data=genfromtxt('../DATA/bank_note_data.txt',delimiter=",")

labels=data[:,4]
features=data[:,0:4]

X = features
y= labels

####################**************************************************************************************
#           s pomočjo sklearn.model_selection razdeli podatke na testne in učne, nato normaliziraj podatke
####################**************************************************************************************
# radzeli X vhodne podatke in y izhod (rezultat) v testne in učne
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Standardize or scale your data
from sklearn.preprocessing import MinMaxScaler

scaler_object = MinMaxScaler()
scaler_object.fit(X_train)

scaled_X_train=scaler_object.transform(X_train)
scaled_X_test=scaler_object.transform(X_test)

# print("Učni izhodi", y_train)
# print("Učni vhodi", scaled_X_train)
# print("**************** testni *************************************")
# print("Učni izhodi", y_test)
# print("Učni vhodi", scaled_X_test)

####################**************************************************************************************
#          Build neuron network model
####################**************************************************************************************

from keras.models import Sequential
from keras.layers import Dense

model = Sequential() # Build a model

model.add(Dense(4, input_dim=4,activation='relu'))  # Imamo 4 stolpce-dimenzije za input. Kao imamo 4 nevrone ZGLEDA da je to vhodni layer
model.add(Dense(8, activation='relu')) # vmesni layer Hidden Layer
model.add(Dense(1,activation='sigmoid')) #IZHODNI Layer -Samo eno stanje

####################**************************************************************************************
#          Compile the model, Train it and testing it

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Train data
model.fit(scaled_X_train, y_train, epochs=50, verbose=2) # verbose=2 --> pomeni, da bom med treningom izpisovalo na ekranu poročilo

def Probability_to_Values(x):
    lRez = x.copy()
    for index, value in enumerate(x):
        if value < 0.5:
            lRez[index]=0
        else:
            lRez[index]=1
    lRez64 = lRez.astype(np.float64)
    return lRez64

probability_rez=model.predict(scaled_X_test)
predictions = Probability_to_Values(probability_rez)
print(predictions)



#************************************************************************************
#       Evaluate model

print(model.metrics_names)

from sklearn.metrics import confusion_matrix, classification_report

print(classification_report(y_test,predictions))


#**************************************************************************************
# Shrani modul, in ga nato naloži

model.save('mysupwrmodel.h5')  # Shrani modul

# Naloži modul
from keras.models import load_model
newmodel=load_model('mysupwrmodel.h5')

# na novo naredi predikcije
# newmodel.predict(scaled_X_test)
# predictions2 = Probability_to_Values(newmodel.predict(scaled_X_test))
# print(predictions2)