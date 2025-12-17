def MinMaxScaler(x):
    import numpy as np
    # Min-Max scaling formula
    return (x - np.min(x)) / (np.max(x) - np.min(x))
