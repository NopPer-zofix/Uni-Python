import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier



df = pd.read_csv(r'D:\snake\Uni\Lab8\fraud.csv')


for i in range(5, 9):
    for j in range(5, 9):
        if i == j:
            continue
        one = 'V' + str(i)
        two = 'V' + str(j)
        x = np.array(df[one].tolist())
        y = np.array(df[two].tolist())
        plt.figure()
        plt.scatter(x, y,c = 'cyan', s=10)
        plt.title(one + " VS " + two)
        
        plt.show()








#ML part starts here
X_v1 = df.iloc[:, 1:2].values
y = df['Class'].values
X_train_v1, X_test_v1, y_train_v1, y_test_v1 = train_test_split(X_v1, y, test_size=0.2, random_state=0)

reg_v1 = LinearRegression().fit(X_train_v1, y_train_v1)
knn_v1 = KNeighborsClassifier().fit(X_train_v1, y_train_v1)

v1_lin_score = metrics.accuracy_score(y_test_v1, np.round(reg_v1.predict(X_test_v1)))
v1_knn_score = knn_v1.score(X_test_v1, y_test_v1)


X_v6 = df.iloc[:, 6:7].values
X_train_v6, X_test_v6, y_train_v6, y_test_v6 = train_test_split(X_v6, y, test_size=0.2, random_state=0)

reg_v6 = LinearRegression().fit(X_train_v6, y_train_v6)
knn_v6 = KNeighborsClassifier().fit(X_train_v6, y_train_v6)

y_pred_lin_v6 = reg_v6.predict(X_test_v6)
v6_lin_score = metrics.accuracy_score(y_test_v6, np.round(y_pred_lin_v6))
v6_knn_score = knn_v6.score(X_test_v6, y_test_v6)


plt.figure(figsize=(8, 4))
plt.scatter(X_test_v6, y_test_v6, color='gray', alpha=0.3)
plt.plot(X_test_v6, y_pred_lin_v6, color='red', linewidth=2)
plt.title('V6 vs Class - Linear Regression Function')
plt.show()

x_range = np.linspace(X_v6.min(), X_v6.max(), 1000).reshape(-1, 1)
knn_boundary = knn_v6.predict(x_range)

plt.figure(figsize=(8, 4))
plt.scatter(X_test_v6, y_test_v6, color='gray', alpha=0.3)
plt.plot(x_range, knn_boundary, color='blue', linewidth=2)
plt.title('V6 vs Class - KNN Classification Function (Boundary)')
plt.show()

labels = ['V1: Linear', 'V1: KNN', 'V6: Linear', 'V6: KNN']
scores = [v1_lin_score, v1_knn_score, v6_lin_score, v6_knn_score]

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, scores, color=['lightblue', 'blue', 'lightcoral', 'red'])

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f'{yval:.4f}', ha='center')

plt.ylim(0, 1.1)
plt.ylabel('Accuracy Score')
plt.title('Performance Comparison: V1 vs. V6 (Chosen Predictor)')
plt.show()

print(f"Final Results:\nV1 KNN Score: {v1_knn_score}\nV6 KNN Score: {v6_knn_score}")