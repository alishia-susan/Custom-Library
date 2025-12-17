def mean_absolute_percentage_error(y_true, y_pred):
    import numpy as np
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    z = np.abs((y_true - y_pred) / y_true)
    return np.mean(z) * 100
