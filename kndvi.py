# kNDVI with RBF kernel.
# nir: near infrared (pixel) value
# red: red value

import numpy as np
sigma = 1.0
knr = np.exp(-(nir-red)**2/(2*sigma**2))
kndvi = (1-knr) / (1+knr)

# An equivalent form to compute it is
# kndvi = np.tanh(((nir-red)/(2*sigma))**2)
