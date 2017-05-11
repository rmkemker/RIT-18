# RIT-18
High-Resolution Multispectral Dataset for Semantic Segmentation

## Description

This repository contains the RIT-18 dataset we built for the semantic segmentation of remote sensing imagery.  It was collected with the Tetracam Micro-MCA6 multispectral imaging sensor onboard a DJI-1000 octocopter.  The main contributions of this dataset include 1) very-high resolution imagery from a drone, 2) six-spectral VNIR bands, and 3) 18 object classes (plus background) with a severely unbalanced class distribution.  Details about its construction can be found [in our paper](https://arxiv.org/abs/1703.01918).  

If you use this dataset in a publication, please cite:

```
@article{kemker2017high,
  title={High-Resolution Multispectral Dataset for Semantic Segmentation},
  author={Kemker, Ronald and Salvaggio, Carl and Kanan, Christopher},
  journal={arXiv preprint arXiv:1703.01918},
  year={2017}
}
```

## Data Files

This repository contains the following files:

1. rit18_data_url: The URL to the current location of the data.
2. evaluate_rit18.py: The evaluation script used to score the predicition map

The data, once downloaded, is ~3.0GB.  It is a .mat file containing a dictionary of various elements including:
* 'train_data' : (7 x 9,393 x 5,642) numpy array containing the training ortho.  The first six bands are the VNIR spectral bands and the 7th band is the mask of the orthomosaic.
* 'train_labels': (9,393 x 5,642) numpy array containing the training labels. 
* 'val_data' : (7 x 8,833 x 6,918) numpy array containing the validation ortho.  The first six bands are the VNIR spectral bands and the 7th band is the mask of the orthomosaic.
* 'val_labels' : (8,833 x 6,918) numpy array containing the validation labels.  
* 'test_data' : (7 x 12,446 x 7,654) numpy array containing the testing ortho.  The first six bands are the VNIR spectral bands and the 7th band is the mask of the orthomosaic.
* 'band_centers' : Spectral band centers
* 'band_center_units' : Units for 'band_centers'
* 'sensor' : Information about the sensor
* 'classes' : List of object classes                          
* 'info' : Various information about the dataset

## Instructions

The dataset contain pixel-wise annotations for both the training and validation folds.  Both sets of labels can be used to train a classifier.  It is separated as a rough per-class split, but the validation fold does not contain the black and white wooden targets.  This is because we want to evaluate our model's ability to perform low-shot learning.

The goal is to have the test labels available on the IEEE GRSS server.  Until then, send me your prediction map of the test image (same spatial dimensions as the test image) in either .npy (Python) or .mat (MATLAB) format.  I will use your predicitions on the evaluate_rit18.py I provided here and send you the output file.  As soon as I get this up on the evaluation server, then the user will be able to do all of this themselves.

## Contact

Author: Ronald Kemker

E-mail: rmk6217@rit.edu

Website: [http://www.cis.rit.edu/~rmk6217/](http://www.cis.rit.edu/~rmk6217/)
