def accuracy_score(y_true, y_pred):
    import numpy as np
    n1 = np.array(y_true)
    n2 = np.array(y_pred)
    return np.sum(n1 == n2) / len(n1)
