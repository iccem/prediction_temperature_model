import pandas as pd
from sklearn.tree import DecisionTreeRegressor

data['dayofyear'] = data['date'].dt.dayofyear

data_train = data[data['date'] < '2020-01-01']
data_test = data[data['date'] >= '2020-01-01']

X_train = pd.DataFrame(data_train['dayofyear'])
X_test = pd.DataFrame(data_test['dayofyear'])

y_train = data_train['T']
y_test = data_test['T']

model = DecisionTreeRegressor(max_depth = 6)
model.fit(X_train, y_train)

pred_train = model.predict(X_train)
pred_test = model.predict(X_test)

print('Средняя ошибка на обучающей выборке= ', mean_absolute_error(y_train, pred_train))
print('Средняя ошибка на тестовой выборке= ', mean_absolute_error(y_test, pred_test))