from keras.datasets import mnist

(x_train, y_train),(x_test,y_test)=mnist.load_data()

import matplotlib.pyplot as plt

print(x_train.shape)

# single_image = x_train[0]
# plt.imshow(single_image, cmap='gray_r')

print(y_train)

#->čudna pretvorba 2 v [0 0 1 0 0 0 0 0 0 0]; 5 v [0 0 0 0 0 1 0 0 0 0]; 4 v [0 0 0 0 1 0 0 0 0 0]
from keras.utils.np_utils import to_categorical
y_cat_test=to_categorical(y_test, 10) #->čudna pretvorba 2 v [0 0 1 0 0 0 0 0 0 0]; 5 v [0 0 0 0 0 1 0 0 0 0]
y_cat_train=to_categorical(y_train, 10)


# noramlize vhodne x podatke
x_train=x_train/x_train.max()
x_test=x_test/x_test.max()
plt.imshow(x_train[0], cmap='gray_r')

# x_train in x_test dodaj še dimenzijo baru
x_train=x_train.reshape(60000,28,28,1)
print(x_train.shape)

x_test=x_test.reshape(10000,28,28,1)
print(x_test.shape)

#*********************************************************************************************************
# BUILD A MODEL
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten

model=Sequential()

# CONVOLUTION LAYER
model.add(Conv2D(filters=32, kernel_size=(4,4),input_shape=(28, 28, 1), activation='relu'))
# POOLING LAYER
model.add(MaxPool2D(pool_size=(2,2)))
# adding a layer for flattening
model.add(Flatten()) # 2d -> 1d
# add a dense Layer
model.add(Dense(128, activation='relu'))
# Output layer
model.add(Dense(10, activation='softmax')) # 0 -> [1 0 0 0 0 0 0 0 0 0]; 1 -> [0 1 0 0 0 0 0 0 0 0 0]; 2 -> [0 0 1 0 0 0 0 0 0 0]
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
print(model.summary()) # Izpiši podatke o modelu

model.fit(x_train,y_cat_train, epochs=6)

model.save('cnnModel.h5')

print("Konec")