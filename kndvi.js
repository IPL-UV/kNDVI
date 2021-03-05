// Javacript for GEE
// kNDVI using the RBF kernel.
// nir and red are near-infrared and red bands, respectively.
// The example here assumes the values of these bands are *reflectances*.
// For instace, for MODIS you must divide the raw values by 10000.
// See the image collection documentation you use for specific instructions.

// We present two options:
// 1. Using the definition of RBF kernel: exp(-(nir-red)^2/(2*sigma^2))
// 2. Equivalent: tanh((nir-red)^2/(2*sigma)^2)
// Both obtain the same result, use the one you prefer!

var addKNDVI_RBF = function(image) {
  // Compute (nir-red)^2
  var D2 = nir.subtract(red).pow(2);
  // Sigma: you have to adjust this for your data.
  // Here we use a value sensible for MODIS reflectances.
  var sigma = ee.Number(0.15);
  // Compute kernel (k) and kNDVI
  var k = D2.divide(sigma.pow(2)).multiply(-1).exp();
  var kndvi = ee.Image.constant(1).subtract(k)
      .divide(ee.Image.constant(1).add(k));
  return image.addBands(kndvi.select([0], ['kndvi']));
}

var addKNDVI_tanh = function(image) {
  // Compute (nir-red)^2
  var D2 = nir.subtract(red).pow(2);
  var sigma = ee.Number(0.15);
  var kndvi = D2.divide(sigma.multiply(2.0).pow(2)).tanh();
  return image.addBands(kndvi.select([0], ['kndvi']));
}
