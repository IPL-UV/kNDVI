#if (!require("raster")) install.packages("raster")
require(raster)

# Function to convert Sentinel-2 L2A into reflectance values
s2_surface_reflectance <- function(x){
  #@x: RasterLayer, RasterStack or RasterBrick containing Sentinel-2 L2A data
  return(x/10000)
}

# Function to compute kNDVI from two RasterLayers
kndvi <- function(nir, red, sigma=0.15, method="rbf", faster=FALSE){
  #@nir: RasterLayer containing reflectance values in the Near-Infrared band
  #@red: RasterLayer containing reflectance values in the Red band
  #@sigma: sigma value. This argument accept a single sigma value or a RasterLayer containing the pixel-wise
  # sigma value. By default sigma=0.15.
  #@mode: method used to compute kNDVI. Options: "rbf" or "tanh". Default="rbf"
  #@faster: Not implemented! If faster=TRUE non-evaluate range of values and make the function faster
  if(max(raster::values(nir))>1){message("The NIR band contains values greater than 1")}
  if(min(raster::values(nir))<0){message("The NIR band contains values lower than 0")}
  if(max(raster::values(red))>1){message("The Red band contains values greater than 1")}
  if(min(raster::values(red))<1){message("The Red band contains values lower than 0")}
  if(method=="rbf"){
    knr <- exp(-(nir-red)^2/(2*sigma^2))
    kndvi <- (1-knr) / (1+knr)
  }
  if(method=="tanh"){
    kndvi <- tanh(((nir-red)/(2*sigma))^2)
  }
  return(kndvi)
}

# Function to compute the pixel-wise sigma value
pixel_wise_sigma <- function(nir, red){
  #@nir: RasterLayer containing reflectance values in the Near-Infrared band
  #@red: RasterLayer containing reflectance values in the Red band
  sigma <- 0.5 * (nir + red)
  return(sigma)
}

# Function to compute the median pixel-wise sigma value of the scene
median_dist_sigma <- function(pixel_wise_sigma, nsamples=1000){
  #@nir: RasterLayer containing reflectance values in the Near-Infrared band
  #@red: RasterLayer containing reflectance values in the Red band
  #@nsamples: Not implemented! Number of random samples used to compute the median value
  set.seed(1234)
  return(median(raster::values(pixel_wise_sigma)))
}
