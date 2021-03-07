# kNDVI with RBF kernel.
# nir: near infrared (pixel) value
# red: red value

# Fix or estimate a reasonable sigma value
sigma = 0.15
knr = exp(-(nir-red)^2 / (2*sigma^2))
kndvi = (1-knr) / (1+knr)

# An equivalent way to compute it
kndvi = tanh(((nir-red)/(2*sigma))^2)
