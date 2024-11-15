
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from algo_lib.ml.linear_regression import LinearRegression


def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def main():
    # Example dataset
    np.random.seed(0)
    X = np.random.rand(100, 1) * 10  # 100 samples, 1 feature
    y = 3 * X.squeeze() + 7 + np.random.randn(100) * 2  # y = 3x + 7 + noise

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
        )

    # Initialize and train model
    regressor = LinearRegression(learning_rate=0.01, n_iters=1000)
    regressor.fit(X_train, y_train)

    # Predictions
    predictions = regressor.predict(X_test)

    # Evaluate model
    mse = mean_squared_error(y_test, predictions)
    r2 = regressor.score(X_test, y_test)
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.2f}")

    # Visualize predictions vs. actual data
    plt.figure(figsize=(8, 6))
    plt.scatter(X_train, y_train, color="blue", s=10, label="Train data")
    plt.scatter(X_test, y_test, color="green", s=10, label="Test data")
    plt.plot(
        X,
        regressor.predict(X),
        color="black",
        linewidth=2,
        label="Prediction"
        )
    plt.legend()
    plt.title("Linear Regression Predictions")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.show()

    # Plot loss curve
    plt.figure(figsize=(8, 6))
    plt.plot(
        range(len(regressor.losses)),
        regressor.losses,
        color='red',
        label='Training Loss'
        )
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title("Loss Curve")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
