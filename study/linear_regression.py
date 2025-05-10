import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

# Cargar datos desde un archivo .csv
data = pd.read_csv('datos.csv')  # Cambia 'datos.csv' por el nombre de tu archivo

# Selección de características y variable objetivo
X = data[['feature']].values  # Suponiendo que 'feature' es la columna de características
y = data['target'].values     # 'target' es la columna objetivo

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Ajustar el modelo a los datos de entrenamiento
model.fit(X_train, y_train)

# Parámetros del modelo
print(f'Coeficiente: {model.coef_[0]}')      # Pendiente
print(f'Intercepción: {model.intercept_}')   # Intercepto

# Predecir usando el modelo ajustado
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Evaluar el modelo
train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)
train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)

print(f'MSE de entrenamiento: {train_mse}')
print(f'MSE de prueba: {test_mse}')
print(f'R² de entrenamiento: {train_r2}')
print(f'R² de prueba: {test_r2}')

# Plotear los datos de prueba y la línea de regresión
plt.scatter(X_test, y_test, color='blue', label='Datos de prueba')
plt.plot(X_test, y_pred_test, color='red', label='Regresión lineal')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.show()