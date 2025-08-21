import numpy as np
def val(prices,shares):
    stvls = np.multiply(prices,shares)
    total = np.sum(stvls)
    return stvls, total