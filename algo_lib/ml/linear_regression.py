
import numpy as np


class LinearRegression:

    def __init__(
            self,
            learning_rate=0.001,
            n_iters=1000,
            regularization=None,
            alpha=0.1
            ):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        self.regularization = regularization  # None, 'l1', or 'l2'
        self.alpha = alpha  # Regularization strength
        self.losses = []  # To track loss during training

    def fit(self, X, y):
        # Input validation
        if not isinstance(X, np.ndarray) or not isinstance(y, np.ndarray):
            raise ValueError("X and y must be numpy arrays.")
        if X.shape[0] != y.shape[0]:
            raise ValueError("Number of samples in X and y must match.")
        if np.isnan(X).any() or np.isnan(y).any():
            raise ValueError("Input contains NaN values.")

        # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Gradient Descent
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            residuals = y_predicted - y

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, residuals)
            db = (1 / n_samples) * np.sum(residuals)

            # Add regularization if specified
            if self.regularization == 'l2':  # Ridge
                dw += (self.alpha / n_samples) * self.weights
            elif self.regularization == 'l1':  # Lasso
                dw += (self.alpha / n_samples) * np.sign(self.weights)

            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            # Compute and store loss
            loss = (1 / (2 * n_samples)) * np.sum(residuals ** 2)
            self.losses.append(loss)

    def predict(self, X):
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not fitted yet. Call 'fit' first.")
        return np.dot(X, self.weights) + self.bias

    def score(self, X, y):
        y_mean = np.mean(y)
        ss_total = np.sum((y - y_mean) ** 2)
        ss_residual = np.sum((y - self.predict(X)) ** 2)
        return 1 - (ss_residual / ss_total)
