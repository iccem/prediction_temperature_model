import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# с помощью модели Линейная регрессия 
# подгоним коэффициент при косинусе
# чтобы растянуть его в высоту до уровня наших данных
# z = a cos (dayofyear) + b

model = LinearRegression()
X_train, X_test, y_train, y_test = None

def get_feaches(data):
    data_train = data[data['date'] < '2020-01-01']
    data_test = data[data['date'] >= '2020-01-01']

    X_train = pd.DataFrame(data_train['cos_dayofyear'])
    X_test = pd.DataFrame(data_test['cos_dayofyear'])

    y_train = data_train['T']
    y_test = data_test['T']
    return (X_train, X_test, y_train, y_test)

# обучаем модель
model.fit(X_train, y_train)

# прогноз для данных, которые модель еще "не видела"
pred_test = model.predict(X_test) 

print('Средняя ошибка на тестовой выборке= ', mean_absolute_error(y_test, pred_test))

# Делаем прогноз

pred_train = model.predict(X_train)

print('Средняя ошибка на обучающей выборке= ', mean_absolute_error(y_train, pred_train))
print('Средняя ошибка на тестовой выборке= ', mean_absolute_error(y_test, pred_test))


