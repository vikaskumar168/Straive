# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# import pandas as pd
#
#
# data = {
#     "sqft": [1000, 1500, 2000, 2500, 3000],
#     "bedrooms": [2, 3, 3, 4, 5],
#     "price": [200000, 250000, 300000, 400000, 500000]
# }
# df = pd.DataFrame(data)
#
# X = df[["sqft", "bedrooms"]]
# y = df["price"]
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# model = LinearRegression()
# model.fit(X_train, y_train)
#
# pred = model.predict(X_test)
# print("Predicted Prices:", pred)


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "sqft": [1000, 1500, 2000, 2500, 3000],
    "bedrooms": [2, 3, 3, 4, 5],
    "price": [200000, 250000, 300000, 400000, 500000]
}
df = pd.DataFrame(data)

X = df[["sqft", "bedrooms"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

try:
    sqft_input = float(input("Enter the square footage of the house: "))
    bedrooms_input = int(input("Enter the number of bedrooms: "))

    predicted_price = model.predict([[sqft_input, bedrooms_input]])[0]

    print(f"\nEstimated Price: ₹{predicted_price:,.2f}")
    if predicted_price < 250000:
        print("This seems like a budget-friendly option.")
    elif predicted_price < 400000:
        print("This is a mid-range property with decent features.")
    else:
        print("This looks like a premium listing!")

except ValueError:
    print("Invalid input. Please enter numeric values for both fields.")
