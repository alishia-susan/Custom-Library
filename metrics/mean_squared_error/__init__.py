def mean_squared_error(y_true, y_pred):
    import numpy as np
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    z = (y_true - y_pred) ** 2
    return np.mean(z)
