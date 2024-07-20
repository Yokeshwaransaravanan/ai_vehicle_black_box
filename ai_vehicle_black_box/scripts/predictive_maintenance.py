import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    X = data.drop('fault', axis=1)
    y = data['fault']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def preprocess_data(X_train, X_test):
    scaler = StandardScaler()
    return scaler.fit_transform(X_train), scaler.transform(X_test)

def build_and_train_model(X_train, y_train, input_shape):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)
    return model

def main():
    X_train, X_test, y_train, y_test = load_data('data/maintenance_data.csv')
    X_train, X_test = preprocess_data(X_train, X_test)
    model = build_and_train_model(X_train, y_train, X_train.shape[1])
    model.save('models/predictive_maintenance_model.h5')

if __name__ == "__main__":
    main()

