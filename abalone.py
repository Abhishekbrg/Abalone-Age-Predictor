import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
names=['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight','Rings']
data=pd.read_csv("abalone.csv",names=names)  #load dataset
X=data.iloc[:,:-1]

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import cross_val_score
 
data['age']=data['Rings']+1.5     # a process to compute abalone age
data.drop('Rings', axis=1, inplace=True)
y=data.iloc[:,-1]

from sklearn.preprocessing import LabelEncoder
labl=LabelEncoder()
X['Sex']=labl.fit_transform(X['Sex'])


from sklearn.preprocessing import StandardScaler
standardScale = StandardScaler()
X=standardScale.fit_transform(X)


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25, random_state=None)
print(data.info())
print(data.describe())
data.hist(figsize=(20,10),grid=False,layout=(2,4), bins=40)
plt.show()


#-converting all the feature to object
numerical=data.select_dtypes(include=np.number).columns
categorical=data.select_dtypes(include=np.object).columns
regr = RandomForestRegressor(max_depth=2, random_state=0,n_estimators=3)
regr.fit(X_train,y_train)
y_pred=regr.predict(X_test)
y_demo=list(y_pred)
from sklearn.metrics import mean_squared_error
from math import sqrt
rms = sqrt(mean_squared_error(y_test, y_pred))
print(100 - rms)

error = 1000
error_index = 0
for i in range(1, 100):
    regr = RandomForestRegressor(max_depth=2, random_state=0,n_estimators=i)
    regr.fit(X_train,y_train)
    y_pred=regr.predict(X_test)
    y_demo=list(y_pred)
    rms = sqrt(mean_squared_error(y_test, y_pred))
    if rms < error:
        error = rms
        error_index = i
print(100 - error, " with best value of estimator is ", error_index)

