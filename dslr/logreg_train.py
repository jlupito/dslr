import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json, argparse
from sklearn.preprocessing import LabelBinarizer
from utils.load_csv import load
from utils.utils_logistic import log_loss, optimisation, initialisation, forward_propagation

def predict(X, W, b):
    A = forward_propagation(X, W, b)
    return A >= 0.5

def train(X, y, n_iter, learning_rate):
    W, b = initialisation(X)
    loss_history = []
    for i in range(n_iter):
        A = forward_propagation(X, W, b)
        loss_history.append(log_loss(y, A))
        W, b = optimisation(X, W, b, A, y, learning_rate)
    return W, b, loss_history

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


def main():
    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument('path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    features = ["Ancient Runes", "Astronomy", "Herbology", "Charms", "Defense Against the Dark Arts"]
    try:
        df = load(args.path)
        if df is None:
            return
        # features_col = df[features]
        # features_col.drop('Index', axis=1, inplace=True)

        # X = np.array(features_col.iloc[:, 1:].values)
        # y = np.array(features_col.iloc[:, 0].values).reshape(-1, 1)
        X = df[features].values
        lb = LabelBinarizer()
        y = lb.fit_transform(df['Hogwarts House'])
        print(X)
        print(y)
        print(X.shape)
        print(y.shape)
        # init du weight et du biais avec des val random
        W, b = initialisation(X)
        loss_history = []
        n_iter = 100
        learning_rate = 0.1
        models = []

        # model training
        for i in range(y.shape[1]):
            W, b, loss_history = train(X, y[:, i].reshape(-1, 1), n_iter, learning_rate)
            models.append((W, b, loss_history))
        
        # prediction
        predictions = np.zeros((X.shape[0], len(models)))
        for i, (W, b, _) in enumerate(models):
            predictions[:, i] = predict(X, W, b).flatten()

        final_predictions = lb.inverse_transform(predictions)

        print("Prédictions finales :", final_predictions)


        # visualisation(X, y, W, b)
        # plt.figure(figsize=(9, 6))
        # plt.plot(loss_history)
        # plt.xlabel('n_iteration')
        # plt.ylabel('Log_loss')
        # plt.title('Evolution des erreurs')
        # plt.show()


     

        # si on veut voir la courbe de coût sur le nb d iteration:
        # plt.plot(range(300), cost_history)
        # plt.show()

    except KeyboardInterrupt:
        print(" Keyboard interrupt detected.")
        return

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()