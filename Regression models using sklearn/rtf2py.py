import requests
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import timezone
import numpy as np

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression

url ="https://go-services.orbitalinsight.com/api/v2/go/projects/u8oXupXXYg-210510/versions/u8oXupXXYg-210510-1.0.0/results/40ba8836-4c83-436c-bdfc-833d82945c2f/timeseries/raw.count"
querystring = {"format":"json","offset":"0","limit":"100","token":"760db46e790dd06b5cba081adc7669cbc037dc51"}
headers = {"Accept": "text/csv","X-Orbitalinsight-Auth-Token": "760db46e790dd06b5cba081adc7669cbc037dc51"}
response = requests.request("GET", url, headers=headers,params=querystring)

txt = response.json()
x,y = [],[]

dto = datetime.strptime(txt['data'][0]['x_value']['obs_date'], txt['data'][0]['x_value']['field_format'])
dto = dto.astimezone(timezone('utc'))
fd = dto.date()

for d in txt['data']:
    y.append(d['y_value']['unique_count'])
    dto = datetime.strptime(d['x_value']['obs_date'], d['x_value']['field_format'])
    dto = dto.astimezone(timezone('utc'))
    ld = dto.date()
    delta = ld-fd
    x.append(delta.days)


plt.plot(x, y)
plt.title('Simple plotting')
plt.show()


linear_regressor = LinearRegression()  # create object for the class
X = np.array(x).reshape(-1,1)
Y = np.array(y).reshape(-1,1)

linear_regressor.fit(X, Y)
y_pred = linear_regressor.predict(X)  # make predictions
plt.scatter(X, Y)
plt.plot(X, y_pred, color='red')
plt.show()


X_seq = np.linspace(X.min(),X.max(),300).reshape(-1,1)




degree=20
polyreg=make_pipeline(PolynomialFeatures(degree),LinearRegression())
polyreg.fit(X,Y)

plt.figure()
plt.scatter(X,y)
plt.plot(X_seq,polyreg.predict(X_seq),color="black")
plt.title("Polynomial regression with degree "+str(degree))
plt.show()