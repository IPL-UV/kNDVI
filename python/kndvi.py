# kNDVI with RBF kernel.
# nir: near infrared (pixel) value
# red: red value

import numpy as np
from scipy.spatial.distance import pdist


def median_dist_sigma(X: np.ndarray, subsample: int=None, seed: int=123) -> float:
    """standard median distance estimation for sigma
    Args: 
        X (np.ndarray): input data, shape=(n_samples, n_features)
        subsample (int): subsample of the data, optional
            recommended value of 1_000 for very large datasets
        seed (int): for reproducibility on the random subsample
    Returns:
        sigma (float): sigma value
    """

    # ensure 1D for pdist function
    if X.ndim == 1:
        X = np.atleast_2d(X).T
    
    # only subsample if asked for or less than number of samples
    if subsample is not None and subsample < X.shape[0]:
        # random seed for reproducibility
        rng = np.random.RandomState(seed)

        # permute samples and take a subset
        X = rng.permutation(X)[:subsample]

    # get the median distance
    sigma = np.median(pdist(X, "euclidean"))

    return sigma


def pixel_wise_sigma(nir: np.ndarray, red: np.ndarray) -> float:
    """Calculate sigma pixel-wise
    Estimate sigma independently for each pixel as sigma=0.5*(NIR+red).
    
    Args:
        nir (np.ndarray): near infrared band, shape=(n_samples)
        red (np.ndarray): red band, shape=(n_samples)
    Returns:
        sigma (float): sigma value
        """
    sigma = 0.5 * (nir + red)

    return sigma


def calculate_kndvi(nir: np.ndarray, red: np.ndarray, sigma: float=0.15) -> np.ndarray:
    """calculate kernel NDVI method
    
    Args:
        nir (np.ndarray): near infrared band, shape=(n_samples)
        red (np.ndarray): red band, shape=(n_samples)
        sigma (float): length scale for the kernel method
    Returns:
        kndvi (np.ndarray): kernel ndvi, shape=(n_samples)
    """
    # calculate knr
    knr = np.exp(-((nir - red) ** 2) / (2 * sigma ** 2))

    # calculate kndvi

    kndvi = (1 - knr) / (1 + knr)
    # An equivalent form to compute it is
    # kndvi = np.tanh(((nir-red)/(2*sigma))**2)

    return kndvi


def main():

    # estimate sigma
    n_samples = 10
    nir = np.random.randn(n_samples)
    red = 0.1 * np.random.randn(n_samples)

    sigma = pixel_wise_sigma(nir, red)

    # estimate kernel ndvi
    k_indice = calculate_kndvi(nir, red, sigma)


if __name__ == "__main__":
    main()
