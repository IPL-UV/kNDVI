
# On Kernel Vegetation Indices

Empirical vegetation indices derived from spectral reflectance data are widely used in remote sensing of the biosphere, as they represent robust proxies for canopy structure, leaf pigment content and, subsequently, plant photosynthetic potential. Here we generalize the broad family of commonly used vegetation indices by exploiting all  higher-order relations between the spectral channels involved. This results in a higher sensitivity to vegetation biophysical and physiological parameters. While many kernel vegetation indices are possible, we focus here on the the nonlinear generalization of the Normalized Difference Vegetation Index (NDVI). 

Check the paper and (especially) the supplementary material for more details, parameter prescriptions, other examples of application and code snippets and demos. 

<a href="https://advances.sciencemag.org/content/7/9/eabc7447">Paper</a> | <a href="https://zenodo.org/record/4574349">Preprint+Supp.Mat. </a>

# Code snippets and demos

Here you find some basic implementations in several computer languages: Python, JavaScript for GEE, R, Julia, MATLAB, and IDL. 

Also, we give Google Earth Engine (GEE) examples in https://code.earthengine.google.com/?accept_repo=users/belmanip/kNDVI

# On the (importance) of the sigma parameter

Kernel methods require the definition of a kernel function and fixing the corresponding parameters. Many kernel functions are possible: the linear, polynomial or radial basis function (RBF) kernel being the most popular <a href="https://arxiv.org/pdf/math/0701907.pdf">[Hofmann et al 2007]</a>, <a href="https://arxiv.org/pdf/2007.14706.pdf">[Johnson et al 2020]</a>. The RBF kernel, k(a,b) = exp(-(a-b)^2/(2\sigma^2)), has a lengthscale parameter \sigma which controls the notion of similarty between a and b. For the kNDVI, the involved kernel is k(NIR,red) = exp(-(NIR-red)^2/(2\sigma^2)), and thus the lengthscale parameter sigma controls the sensitivity to densely/sparsely vegetated pixel/region.

* In this work, we explored all three (see supp.material S1-S2 of the paper), but decided to stick to the RBF kernel because (i) it largely simplifies the index, kNDVI=tanh(((NIR-red)/(s*sigma))^2), (ii) it captures all higher order moments of similarity between NIR and red reflectances, and (iii) good results were obtained in all applications. 

* The sigma parameter is typically learned by cross-validation in supervised settings, but this is not possible in unsupervised cases like in kNDVI. Therefore, we suggest to estimate a reasonable value from the data itself. A common prescription in the kernel methods literature is to fix the sigma value to the average distance between all involved objects in the dataset, i.e. NIR and red values of all involved pixels in your problem. Several options exist:
/* 
1- Pixel-wise sigma. Estimate sigma independently for each pixel as sigma=0.5*(NIR+red).
2- Region/biome specific. Compute the average distance over a region of interest. 
3- 
*/
We show specific examples in the GEE code (demo2) on how to do this. 


A reasonable choice is taking the average value sigma = 0.5(NIR+red). See S1 and S2 for mathematical and 
ecophysiological justifications, which leads to a simplified operational index version expressed as 

kNDVI = tanh(NDVI^2)

The average of NIR and red can be computed in different ways, depending on the application:

1) Pixel-based. You just average NIR and red for the pixel. This choice can be interpreted as 
         a rough estimation of the pixel’s albedo (see supp. mat. S1.4 for more info)
2) Time series analysis. Remember that in kernel methods, the sigma value should reflect 
         the 'average distance' between the objects you compare (here NIR and red reflectances), so
         when dealing with time series, it is advised to average the mean distance between NIR and red
         over all pixels in the time series. 
3) Regions/biomes. When applying the index to a particular biome or region of interest, the scale sigma of 
         NIR and red relations should be estimated from that particular region by taking for example the 
         average distance between NIR and red of all pixels in the area.

# Some more (important) notes

* Working with radiances or reflectances changes the value of sigma, so we strongly recommend to either 
a) normalize the data before fixing the sigma value of your choice
b) estimate the sigma value directly from data by the average distance criterion (see discussion above)

* In remote sensing of the vegetation, we are very often dealing with noise, clouds and water bodies that hamper the 
direct application of any vegetation index. And since kNDVI operation depends on sigma, one should carefully 
either remove those cases from the calculation of the mean heuristic, or alternatively replace the mean with the median, 
which worked fine in our case studies.




# Cite our work

If you find this useful, consider citing our work:

<b>A Unified Vegetation Index for Quantifying the Terrestrial Biosphere</b>
Gustau Camps-Valls, Manuel Campos-Taberner, Álvaro Moreno-Martı́nez, Sophia Walther, Grégory Duveiller, Alessandro Cescatti, Miguel Mahecha, Jordi Muñoz-Marı́, Francisco Javier García-Haro, Luis Guanter, John Gamon, Martin Jung, Markus Reichstein, Steven W. Running. Science Advances, 26 Feb 2021: Vol. 7, no. 9, eabc7447. DOI: 10.1126/sciadv.abc7447

<a href="https://advances.sciencemag.org/content/7/9/eabc7447">Paper</a> | <a href="https://zenodo.org/record/4574349">Preprint+Supp.Mat. </a>

```
@article {Camps-Vallseabc7447,
  author = {Camps-Valls, Gustau and Campos-Taberner, Manuel and Moreno-Mart{\'\i}nez, {\'A}lvaro and
    Walther, Sophia and Duveiller, Gr{\'e}gory and Cescatti, Alessandro and Mahecha, Miguel D. and
    Mu{\~n}oz-Mar{\'\i}, Jordi and Garc{\'\i}a-Haro, Francisco Javier and Guanter, Luis and
    Jung, Martin and Gamon, John A. and Reichstein, Markus and Running, Steven W.},
  title = {A unified vegetation index for quantifying the terrestrial biosphere},
  volume = {7},
  number = {9},
  elocation-id = {eabc7447},
  year = {2021},
  doi = {10.1126/sciadv.abc7447},
  publisher = {American Association for the Advancement of Science},
  URL = {https://advances.sciencemag.org/content/7/9/eabc7447},
  eprint = {https://advances.sciencemag.org/content/7/9/eabc7447.full.pdf},
  journal = {Science Advances}
}
```
