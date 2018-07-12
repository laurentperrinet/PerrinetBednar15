# -*- coding: utf8 -*-
{
# CRITICAL     50
# ERROR   40
# WARNING     30
# INFO    20
# DEBUG   10
# NOTSET  0
'verbose': 30,
# Image
    'N_image': None, # use all images in the folder
#'N_image': 100, # use 100 images in the folder
# 'N_image': 10, # use 4 images in the folder
    'seed': 42, # a seed for the Random Number Generator (RNG) for picking images in databases, set to None xor set to a given number to freeze the RNG
    'N_X': 256, # size of images
    'N_Y': 256, # size of images
# 'N_X': 64, # size of images
# 'N_Y': 64, # size of images
    'noise': 0.33, # level of noise when we use some
    'do_mask': True, # used in SLIP
	'mask_exponent': 3., #sharpness of the mask
# whitening parameters:
    'do_whitening' : True, # = self.pe.do_whitening
    'white_name_database' : 'kodakdb',
    'white_n_learning': 0,
    'white_N': .07,
    'white_N_0': .0, # olshausen = 0.
    'white_f_0': .4, # olshausen = 0.2
    'white_alpha': 1.4,
    'white_steepness': 4.,
    'white_recompute': False,
# Log-Gabor
#'base_levels': 2.,
    'base_levels': 1.618,
    'n_theta': 24, # number of (unoriented) angles between 0. radians (included) and np.pi radians (excluded)
    'B_sf': .4, # 1.5 in Geisler
    'B_theta': 3.14159/18.,
# Matching Pursuit
# 'N': 32, # number of edges extracted
    'N': 2**11,
# 'N': 2**8,
    'MP_alpha': .7, # ratio of inhibition in alpha-Matching Pursuit
# parameters for computing the histograms
    'd_width': 45., # Geisler 1.23 deg (full image = 45deg)
    'd_min': .5, # Geisler 1.23 deg (full image = 45deg)
    'd_max': 2., # Geisler 1.23 deg (full image = 45deg)
    'N_r': 6, #
    'N_Dtheta': 24, # equal to n_theta: 24 to avoid artifacts
    'N_phi': 12, #
    'N_scale': 5, #
    'loglevel_max': 7, # used for the statistics
# doing the computation on a circular mask
    'edge_mask': False, # should we use a circular mask to exclude some edges when computing statistics (first- and second-order). True in Geisler et al, 2001.
    'do_rank': False,
    'scale_invariant': True,
    'multiscale': True,
    'kappa_phase': 0.,
    'weight_by_distance': True,
# SVM PARAMETERS
# 'svm_n_jobs': 1, # stops after one job so that we do not squat the cluster
# use n_jobs=-1 to occupy all CPUs from a SMP see http: //scikit-learn.org/0.13/modules/generated/sklearn.grid_search.GridSearchCV.html
    'svm_n_jobs': 1, #
    'svm_test_size': 0.2, # represents the proportion of the dataset to include in the test split.
# http: //scikit-learn.org/stable/modules/svm.html says 3.2.6.1.3. Parameters of the RBF Kernel
# When training an SVM with the Radial Basis Function (RBF) kernel, two parameters must be considered: C and gamma. The parameter C, common to all SVM kernels, trades off misclassification of training examples against simplicity of the decision surface. A low C makes the decision surface smooth, while a high C aims at classifying all training examples correctly. gamma defines how much influence a single training example has. The larger gamma is, the closer other examples must be to be affected.
#     'N_svm_grid': 3, #   grid search scaling in SVM
    'N_svm_grid': 32, #   grid search scaling in SVM
#     'N_svm_grid': 55, # grid search scaling in SVM
    'N_svm_cv': 50, # number of cross-validations
    'C_range_begin': -5, #recommended by libsvm
    'C_range_end': 10., #recommended by libsvm
    'gamma_range_begin': -14, # recommended by libsvm
    'gamma_range_end': 3, # recommended by libsvm
    'svm_KL_m': .34, #
#     'svm_tol': 1e-9, #
#     'svm_tol': 1e-6, #
    'svm_tol': 1e-3, #
    'svm_max_iter': -1,
    'svm_log': False, #
    'svm_norm': False, #
# PATHS
    'figpath': 'results',
    'do_edgedir': False,
    'edgefigpath': 'results/edges',
    'matpath': 'cache_dir',
    'edgematpath': 'cache_dir/edges',
    'datapath': '../database',
    'figsize': 14.,
    'figsize_hist': 8, # width of a column in inches
    'figsize_cohist': 8, #
    'formats': ['png', 'pdf', 'jpg'],
    'dpi': 450,
    'use_cache' : True,
    'verbose': 0,
    'scale': .8,
    'scale_circle': 0.08, # relativesize of segments and pivot
    'scale_chevrons': 2.5,
    'line_width': 1.,
    'line_width_chevrons': .75,
    'edge_scale_chevrons': 180.,
}
