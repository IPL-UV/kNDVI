
# On Kernel Vegetation Indices

Empirical vegetation indices derived from spectral reflectance data are widely used in remote sensing of the biosphere, as they represent robust proxies for canopy structure, leaf pigment content and, subsequently, plant photosynthetic potential. Here we generalize the broad family of commonly used vegetation indices by exploiting all  higher-order relations between the spectral channels involved. This results in a higher sensitivity to vegetation biophysical and physiological parameters. While many kernel vegetation indices are possible, we focus here on the the nonlinear generalization of the Normalized Difference Vegetation Index (NDVI). Check the paper and (especially) the supplementary material for more details, parameter prescriptions, other examples of application and code snippets and demos. 

# On the kNDVI code

Here you find some basic implementations in several computer languages: Python, JavaScript for GEE, R, Julia, MATLAB, and IDL. Also, we give Google Earth Engine (GEE) examples in https://code.earthengine.google.com/?accept_repo=users/belmanip/kNDVI

Being a kernel method, the kNDVI also has a kernel parameter to be selected. We use the RBF kernel and the corresponding lengthscale parameter sigma is typically fixed to the average distance between NIR and red, either in the same pixel as simply sigma=0.5(NIR+red), or computing the average distance over a region of interest or a time series. We show a particular example in the GEE code on how to do this.

# Cite our work

If you find this useful, consider citing our work:

<b>A Unified Vegetation Index for Quantifying the Terrestrial Biosphere</b>
Gustau Camps-Valls, Manuel Campos-Taberner, Álvaro Moreno-Martı́nez, Sophia Walther, Grégory Duveiller, Alessandro Cescatti, Miguel Mahecha, Jordi Muñoz-Marı́, Francisco Javier García-Haro, Luis Guanter, John Gamon, Martin Jung, Markus Reichstein, Steven W. Running. Science Advances, 26 Feb 2021: Vol. 7, no. 9, eabc7447. DOI: 10.1126/sciadv.abc7447
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
<br><br>
&nbsp;&nbsp;&nbsp;<a href="https://advances.sciencemag.org/content/7/9/eabc7447"> Science Advances (open access, no hyperlinks) </a> <br>
&nbsp;&nbsp;&nbsp;<a href="https://zenodo.org/record/4574349"> Preprint paper+supplementary material in one file (with hyperlinks) </a> <br>

