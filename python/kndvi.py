# kNDVI with RBF kernel.
# nir: near infrared (pixel) value
# red: red value

import numpy as np
from scipy.spatial.distance import pdist

# Fix or estimate a reasonable sigma value
sigma = 0.15


def median_dist_sigma(X: np.ndarray) -> float:
    """standard median distance estimation for sigma
    Args: 
        X (np.ndarray): input data
    Returns:
        sigma (float): sigma value
    """
    sigma = np.median(pdist(X))

    return sigma


def pixel_wise_sigma(nir: np.ndarray, red: np.ndarray) -> float:
    """Calculate sigma pixel-wise
    Estimate sigma independently for each pixel as sigma=0.5*(NIR+red).
    
    Args:
        nir (np.ndarray): near infrared band
        red (np.ndarray): red band
        sigma (float): length scale for the kernel method
    Returns:
        sigma (float): sigma value
        """
    sigma = 0.5 * (nir + red)

    return sigma


def calculate_kndvi(nir: np.ndarray, red: np.ndarray, sigma: float) -> float:
    """calculate kernel NDVI method
    
    Args:
        nir (np.ndarray): near infrared band
        red (np.ndarray): red band
        sigma (float): length scale for the kernel method
    Returns:
        kndvi (np.ndarray): kernel ndvi
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
    n_samples = 100
    nir = np.random.randn(n_samples)
    red = 0.1 * np.random.randn(n_samples)

    # estimate kernel ndvi
    k_indice = calculate_kndvi(nir, red, sigma)


if __name__ == "__main__":
    main()
