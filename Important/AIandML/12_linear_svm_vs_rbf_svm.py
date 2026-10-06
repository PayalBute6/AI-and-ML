"""
Question: Write a program or report to compare Linear SVM and Non-Linear SVM (RBF Kernel). X = [ [1, 2], [2, 3], [3, 1], [4, 2], [5, 5], [6, 6], [7, 4], [8, 5] ] Y = [0, 0, 0, 0, 1, 1, 1, 1]
"""

from sklearn.svm import SVC

# Training data
X = [
    [1, 2],
    [2, 3],
    [3, 1],
    [4, 2],
    [5, 5],
    [6, 6],
    [7, 4],
    [8, 5]
]

Y = [0, 0, 0, 0, 1, 1, 1, 1]


# Linear SVM
linear_model = SVC(kernel='linear')
linear_model.fit(X, Y)

linear_prediction = linear_model.predict(X)


# Non-Linear SVM using RBF Kernel
rbf_model = SVC(kernel='rbf')
rbf_model.fit(X, Y)

rbf_prediction = rbf_model.predict(X)


# Display results
print("Actual Values:     ", Y)
print("Linear SVM:        ", linear_prediction)
print("RBF SVM:           ", rbf_prediction)

print("\nLinear SVM Accuracy:",
      linear_model.score(X, Y))

print("RBF SVM Accuracy:",
      rbf_model.score(X, Y))
