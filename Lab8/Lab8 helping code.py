import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

df = pd.read_csv(r'D:\snake\Uni\Lab8\fraud.csv')

# The plot of the "Time" column VS the "Amount column"
plt.title('Time vs Amount')
x = np.array(df['Time'].tolist())
y = np.array(df['Amount'].tolist())
plt.plot(x, y)
plt.show()

# ----------------------------------


# The relationship between the first 3 columns (V1, V2, V3)
for i in range(1, 4):
    for j in range(1, 4):
        one = 'V' + str(i)
        two = 'V' + str(j)
        x = np.array(df[one].tolist())
        y = np.array(df[two].tolist())
        plt.scatter(x, y, s=10)
        plt.title(one + " VS " + two)
        plt.show()


# ---------------------------------------

dataset = df

# Below are just some statistics about the dataset
print(dataset.shape)

print("--------------------------")

print(dataset.head())

print("--------------------------")

# prints the class (0/1) of each instance (row) based on Time.
# Time ranges from 0 up to about 180000

dataset.plot(x='Time', y='Class', style='o')
plt.title('Time vs Class')
plt.xlabel('Time')
plt.ylabel('Class')
plt.ylim([-1, 2])
plt.xlim([-30000, 200000])
plt.show()

# x = np.array(df['Time'].tolist())
# print(np.sort(x))

print("----------------------------------")

# Time to do machine learning! Linear regression = draw a line representing the graph that the data create

# First, our X-axis will be column "V1". But we want it in 2D array mode, not a simple array
# Here is how we declare that. 1:2 means take columns from 1 to 2 (which means only column 1)
X = dataset.iloc[:, 1:2].values
# Our Y-axis will be column "Class". We want it in 1D array mode, so we take it the normal way
y = dataset['Class'].values

from sklearn.model_selection import train_test_split

# Split data into training set, testing set. The testing set will be 20% of our data = 20% of the 175823 rows in our CSV
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier

# Train the model
regressor = LinearRegression()
#knn_classifier = KNeighborsClassifier()
regressor.fit(X_train, y_train)
# Have the model predict the test-values of y, based on the test-values of x, to see if it works correctly
y_pred = regressor.predict(X_test)
linear_regression_score = metrics.accuracy_score(y_test, np.round(y_pred))
print("Algorithm Scores:")
print("Linear Regression: ", linear_regression_score)

# Print array proving if it works correctly
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

# Print the line/graph created by linear regression. Looks accurate enough, for a line
plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title('V1 vs Class - The linear graph')
plt.show()

#from sklearn import metrics
# Error statistics
# print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
# print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
# print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
