
# Kernel Vegetation Indices and the kNDVI

Empirical vegetation indices derived from spectral reflectance data are widely used in remote sensing of the biosphere, as they represent robust proxies for canopy structure, leaf pigment content and, subsequently, plant photosynthetic potential. Here we generalize the broad family of commonly used vegetation indices by exploiting all  higher-order relations between the spectral channels involved. This results in a higher sensitivity to vegetation biophysical and physiological parameters. While many kernel vegetation indices are possible, we focus here on the the nonlinear generalization of the Normalized Difference Vegetation Index (NDVI). 

Check the paper and (especially) the supplementary material for more details, parameter prescriptions, other examples of application and code snippets and demos. 

<a href="https://advances.sciencemag.org/content/7/9/eabc7447">Paper</a> | <a href="https://zenodo.org/record/4574349">Preprint+Supp.Mat. </a>

# Code snippets and demos

Here you find some basic implementations in several computer languages: Python, JavaScript for GEE, R, Julia, MATLAB, and IDL. 

Also, we give Google Earth Engine (GEE) examples in https://code.earthengine.google.com/?accept_repo=users/ispguv/kNDVI

## On the importance of the sigma parameter

Kernel methods require the definition of a kernel function and fixing the corresponding parameters. Many kernel functions are possible: the linear, polynomial or radial basis function (RBF) kernel being the most popular <a href="https://arxiv.org/pdf/math/0701907.pdf">[Hofmann et al 2007]</a>, <a href="https://arxiv.org/pdf/2007.14706.pdf">[Johnson et al 2020]</a>. The RBF kernel, k(a,b) = exp(-(a-b)^2/(2\sigma^2)), has a lengthscale parameter \sigma which controls the notion of similarty between *a* and *b*. For the kNDVI, the involved kernel is k(NIR,red) = exp(-(NIR-red)^2/(2\sigma^2)), and thus the lengthscale parameter \sigma controls the sensitivity to densely/sparsely vegetated pixel/region.

* In this work, we explored all three kernel functions (see supp.material S1-S2 of the paper), but decided to stick to the RBF kernel because (i) it largely simplifies the index, kndvi = tanh((NIR-red)^2/(2\sigma)^2), (ii) it captures all higher order moments of similarity between NIR and red reflectances, and (iii) good results are obtained in all applications. 

* The sigma parameter is typically learned by cross-validation in supervised kernel machines, but this is not possible in unsupervised cases like in kNDVI. Therefore, we suggest to estimate a reasonable value of sigma from the data itself. A common prescription in the kernel methods literature is to fix the sigma value to the average distance between all involved objects in the dataset, i.e. NIR and red values of all involved pixels in your problem. Several options exist to estimate sigma from data: (1) Estimate sigma independently for each pixel as a rpxy to pixel's albedo, sigma=0.5*(NIR+red); (2) estimate the sigma from the region/biome by the average distance between all pixels over a region of interest; or (3) when working with (nonstationary) time series one could estimate the lengthscale sigma from the temporal distances. We show specific examples for each approach in the <a href="https://code.earthengine.google.com/?accept_repo=users/ispguv/kNDVI">GEE demos here</a>

## Some other important notes
<ol> 
<li>Working with radiances or reflectances changes the value of sigma, so we strongly recommend to either (a) properly scale the data to reflectance values before fixing the sigma value (e.g. sigma=0.15), *or* (b) estimate the sigma value directly from data by the average distance criterion (see discussion above).

<li>In remote sensing of the vegetation, we are very often dealing with noise, clouds and water bodies that hamper the direct application of any vegetation index. Since kNDVI depends on sigma, one should carefully either remove those cases from the calculation of the mean heuristic, or alternatively replace the mean with the median, which worked fine in our case studies.

<li> Note that the value of the kNDVI is bounded to [0,1] by construction. It is recommended to apply kNDVI for vegetated pixels only, so it is advisable to mask water/snow pixels.
</ol>
Again, in the <a href="https://code.earthengine.google.com/?accept_repo=users/ispguv/kNDVI">GEE demos</a> we work with reflectances, and mask out water bodies when estimating a proper sigma lengthscale.

# How to cite our work

If you find this useful, consider citing our work:

><b>A Unified Vegetation Index for Quantifying the Terrestrial Biosphere</b>
Gustau Camps-Valls, Manuel Campos-Taberner, Álvaro Moreno-Martı́nez, Sophia Walther, Grégory Duveiller, Alessandro Cescatti, Miguel Mahecha, Jordi Muñoz-Marı́, Francisco Javier García-Haro, Luis Guanter, John Gamon, Martin Jung, Markus Reichstein, Steven W. Running. Science Advances, 26 Feb 2021: Vol. 7, no. 9, eabc7447. DOI: 10.1126/sciadv.abc7447

> <a href="https://advances.sciencemag.org/content/7/9/eabc7447">Paper</a> | <a href="https://zenodo.org/record/4574349">Preprint+Supp.Mat. </a>

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
## Acknowledgements
This work was supported by the European Research Council (ERC) Synergy Grant “Understanding and Modelling the Earth System with Machine Learning (USMILE)” under Grant Agreement No 855187.
