import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)


np.random.seed(321)
noise = np.random.normal(0, .5, 100)

y = np.sin(x) + noise

df = pd.DataFrame({'input': x, 'target':y})

plt.scatter(df.input, df.target)
plt.plot(df.input, np.sin(df.input), color = 'r')
plt.show()


mean_model = np.mean(df.target)
print(mean_model)

plt.scatter(df.input, df.target)
plt.plot(df.input, ([mean_model]*len(df.input)), 'r+')
plt.show()


from sklearn.linear_model import LinearRegression

lr = LinearRegression()

features = df.drop('target', axis = 1)
target = df.target

lr.fit(features, target)

print(lr.intercept_)
print(lr.coef_)

plt.scatter(df.input, df.target)
plt.plot(df.input, lr.predict(features), 'k-')

plt.show()