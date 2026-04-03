from sklearn.linear_model import LinearRegression
X=[[10,20,30,40]]
y=[2,4,6,8]
model =LinearRegression()
model.fit(X,y)
print(model.predict([[5]]))