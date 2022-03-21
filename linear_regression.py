import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# с помощью модели Линейная регрессия 
# подгоним коэффициент при косинусе
# чтобы растянуть его в высоту до уровня наших данных
# z = a cos (dayofyear) + b

file_name = 'weather.xls'
data = pd.read_excel(file_name, skiprows=6)

data = data[data['T'].notna()]
data['date'] = pd.to_datetime(data['Местное время в Москве (ВДНХ)'], dayfirst=True)
data_short = data[data['date'].between('2016-10-01', '2017-03-01')]

data = data[data['Po'].notna()] # давление
data = data[data['Pa'].notna()] # барические тенденции
data = data[data['U'].notna()] # влажность
data = data[data['Td'].notna()] # температура точки росы

data['dayofyear'] = data['date'].dt.dayofyear

model = LinearRegression()

data_train = data[data['date'] < '2020-01-01']
data_test = data[data['date'] >= '2020-01-01']

X_train = pd.DataFrame()
X_test = pd.DataFrame()

X_train['dayofyear'] = pd.DataFrame(data_train['dayofyear'])
X_train['Po'] = pd.DataFrame(data_train['Po'])
X_train['Pa'] = pd.DataFrame(data_train['Pa'])
X_train['U'] = pd.DataFrame(data_train['U'])
X_train['Td'] = pd.DataFrame(data_train['Td'])

X_test['dayofyear'] = pd.DataFrame(data_test['dayofyear'])
X_test['Po'] = pd.DataFrame(data_test['Po'])
X_test['Pa'] = pd.DataFrame(data_test['Pa'])
X_test['U'] = pd.DataFrame(data_test['U'])
X_test['Td'] = pd.DataFrame(data_test['Td'])

y_train = data_train['T']
y_test = data_test['T']

# обучаем модель
model.fit(X_train, y_train)

# прогноз для данных, которые модель еще "не видела"
pred_test = model.predict(X_test) 

# print('Средняя ошибка на тестовой выборке= ', mean_absolute_error(y_test, pred_test))

# Делаем прогноз

pred_train = model.predict(X_train)

print('Средняя ошибка на обучающей выборке= ', mean_absolute_error(y_train, pred_train))
print('Средняя ошибка на тестовой выборке= ', mean_absolute_error(y_test, pred_test))


