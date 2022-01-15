import pandas as pd, matplotlib.pyplot as plt, numpy as np
from sklearn.linear_model import LinearRegression as lr

df=pd.read_csv("./veri_setleri/coklu_dogrusal_regresyon_veriseti.csv",sep=";")
print(df.head(3))
plt.scatter(df.deneyim,df.maas)
plt.show()

lr=lr()
X=df.deneyim.values.reshape(-1,1)
y=df.maas.values.reshape(-1,1)
lr.fit(X,y)
a=lr.coef_
b=lr.intercept_

print(f"{a}x+{b}")
