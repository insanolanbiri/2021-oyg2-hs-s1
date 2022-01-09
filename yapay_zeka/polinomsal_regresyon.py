import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data=pd.read_csv("./veri_setleri/polinomsal_regresyon_veriseti.csv",sep=";")

plt.scatter(x=data.araba_fiyat,y=data.araba_max_hiz)
plt.show()

X=data.iloc[:,[0]].values
y=data.iloc[:,[1]].values

lr=LinearRegression()
lr.fit(X,y)
yTahmin=lr.predict(X)
plt.scatter(x=data.araba_fiyat,y=data.araba_max_hiz)
plt.plot(X,yTahmin,color="red")
plt.show()

pol_reg=PolynomialFeatures(degree=4)
x_pol=pol_reg.fit_transform(X)

lr2=LinearRegression()
lr2.fit(x_pol,y)

y_pol_tahmin=lr2.predict(x_pol)

plt.scatter(x=data.araba_fiyat,y=data.araba_max_hiz)
plt.plot(X,yTahmin,color="red")
plt.plot(X,y_pol_tahmin,color="green")
plt.show()



