from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import numpy as np

iris = load_iris()

# Obtenir les données et leurs classifications:
dims = iris.feature_names
classes = iris.target_names
x = iris.data
y = iris.target

# Découper les données en ensembles d'entrainement et de test:
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# Standardisation:
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Créer le réseau de neurones:
mlp_classifier = MLPClassifier(hidden_layer_sizes = (50, 25), max_iter = 1000, random_state = 42)

# Entrainer le MLP:
mlp_classifier.fit(x_train, y_train)

# Prédire et évaluer la performance:
predictions = mlp_classifier.predict(x_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy}')

# Nouvelle prédiction:
#nouveau_prediction = np.array([[5.1, 3.5, 1.4, 0.2]])
nouveau_prediction = np.array([[5.9, 3.,  5.1, 1.8]])

nouveau_prediction = scaler.transform(nouveau_prediction)
res = mlp_classifier.predict(nouveau_prediction)
print(res)
print(classes[res[0]])