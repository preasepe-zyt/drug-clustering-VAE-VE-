import tensorflow as tf
import tensorflow.keras as tfk
import tensorflow.keras.layers as tfkl
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras import regularizers
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.initializers import glorot_uniform
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend as K


def ae(n):
    tf.random.set_seed(54)
    data = pd.read_csv('cleaned.csv').dropna(axis=1)
    data = data.drop('Unnamed: 0', axis=1)
    # data = data.drop("descriptors", axis=1).dropna()
    n_col = data.shape[1]  # .drop('descriptors', axis=1).transpose()
    x_train, x_test = train_test_split(data, test_size=0.3, random_state=1)

    # x_train = x_train/10.66  #
    # x_test = x_test/10.66

    x_train = np.array(x_train)
    #x_train = tf.convert_to_tensor(x_train, dtype=tf.float64)
    x_test = np.array(x_test)
    #x_test = tf.convert_to_tensor(x_test, dtype=tf.float64)

    # Set random seed
    tf.random.set_seed(54)  #

    # Encoder
    inputs = tfkl.Input(shape=(n_col))
    x = inputs
    # x = tfkl.Dense(512,'relu')(x)
    # x = tfkl.Dense(64,'relu')(x)
    x = tfkl.Dense(n, 'relu')(x)
    # x = tfkl.Dense(16, 'relu')(x)
    encoder = tfk.Model(inputs=inputs, outputs=x)

    # Decoder
    inputs = tfkl.Input(shape=(n))
    x = inputs
    # x = tfkl.Dense(32,'relu')(x)
    # x = tfkl.Dense(128,'relu')(x)
    # x = tfkl.Dense(512,'relu')(x)
    x = tfkl.Dense(n_col * 1, 'relu')(x)
    decoder = tfk.Model(inputs=inputs, outputs=x)

    # Autoencoder
    inputs = tfkl.Input(shape=(n_col))
    x = encoder(inputs)
    x = decoder(x)
    model = tfk.Model(inputs=inputs, outputs=x)

    # Train the Autoencoder
    # optimizer = Adam(clipvalue=1.0)  # 梯度裁剪
    # optimizer = Adam(learning_rate=0.01)  # 调整学习率、
    model.compile(loss='mse', optimizer="Adam")
    model.fit(x_train, x_train, epochs=15,
              batch_size=n_col,
              validation_data=(x_test, x_test))

    latent = encoder.predict(data)
    latent = pd.DataFrame(latent)

    latent2 = decoder.predict(latent)
    latent2 = pd.DataFrame(latent2)

    #latent.to_csv(str(n) +"ae.csv", index=False)
    latent2.to_csv(str(n) +"ae(decoder).csv", index=False)
    # encoder.save('pca50_encoder32_10epoch.h5')
if __name__ == "__main__":
    for i in [16, 32, 64]:
        ae(i)







