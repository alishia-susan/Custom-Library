def StandardScaler(x):
    import numpy as np
    # Standard scaling formula
    return (x - np.mean(x)) / np.std(x)
