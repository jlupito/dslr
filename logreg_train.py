import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json, argparse
from utils.load_csv import load
from utils.utils_logistic import sigmoid, log_loss, gradients, initialisation, forward_propagation

def predict(X, W, b):
    A = forward_propagation(X, W, b)
    return A >= 0.5
     

def visualisation(X, y, W, b):
    resolution = 300
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(X[:, 0], X[:, 1], c=y, s=50, edgecolor='k')

    #limites du graphique
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # meshgrid
    x1 = np.linspace(xlim[0], xlim[1], resolution)
    x2 = np.linspace(ylim[0], ylim[1], resolution)
    X1, X2 = np.meshgrid(x1, x2)

    # assembler les 2 variables
    XX = np.vstack((X1.ravel(), X2.ravel())).T

    # Prédictions
    Z = predict(XX, W, b)
    Z = Z.reshape((resolution, resolution))

    ax.pcolormesh(X1, X2, Z, zorder=0, alpha=0.1)
    ax.contour(X1, X2, Z, colors='g')

# def normalize_matrices(df):
#     x = np.array(df.iloc[:, 0].values).reshape(-1, 1)
#     Y = np.array(df.iloc[:, 1].values).reshape(-1, 1)
#     nx = np.zeros(len(x), dtype=float).reshape(-1, 1)

#     xmin = np.min(x)
#     xmax = np.max(x)
#     for i in range(len(x)):
#         nx[i] = (x[i] - xmin) / (xmax - xmin)
#     X = np.hstack((nx, np.ones(nx.shape)))

#     return x, Y, X

# def train_model(X, Y):
#     learning_rate = 0.5
#     n_iterations = 300

#     theta = np.random.randn(2, 1)
#     theta_final, cost_history = gradient_descent(X, Y, theta, learning_rate, n_iterations)
#     thetas = {
#         'Theta0': theta_final[0, 0].item(),
#         'Theta1': theta_final[1, 0].item()
#     }
#     with open('thetas.json', 'w') as file:
#         json.dump(thetas, file)

#     predictions = model(X, theta_final)
#     coef = coef_determination(Y, predictions)

#     return coef, predictions, cost_history

def main():
    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument('path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    features = ["Hogwarts House", "Ancient Runes", "Astronomy", 
                "Herbology", "Charms", "Defense Against the Dark Arts"]
    try:
        df = load(args.path)
        if df is None:
            return
        features_col = df[features]
        # features_col.drop('Index', axis=1, inplace=True)

        X = np.array(features_col.iloc[:, 1:].values)
        Y = np.array(features_col.iloc[:, 0].values).reshape(-1, 1)
        print(X)
        print(Y)
        print(X.shape)
        print(Y.shape)
        # Initialisation
        W, b = initialisation(X)
        loss_history = []

        # # Entrainement
        # for i in range(n_iter):
        #     A = forward_propagation(X, W, b)
        #     loss_history.append(log_loss(y, A))
        #     W, b = optimisation(X, W, b, A, y, learning_rate=0.1)

        # # Prediction
        # visualisation(X, y, W, b)
        # plt.figure(figsize=(9, 6))
        # plt.plot(loss_history)
        # plt.xlabel('n_iteration')
        # plt.ylabel('Log_loss')
        # plt.title('Evolution des erreurs')


     

        # si on veut voir la courbe de coût sur le nb d iteration:
        # plt.plot(range(300), cost_history)
        # plt.show()

    except KeyboardInterrupt:
        print(" Keyboard interrupt detected.")
        return

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()