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

1. rit18_data.mat: The dataset files
2. evaluate_rit18.py: The evaluation script used to score the predicition map

## Instructions

The dataset contain pixel-wise annotations for both the training and validation folds.  Both sets of labels can be used to train a classifier.  It is separated as a rough per-class split, but the validation fold does not contain the black and white wooden targets.  This is because we want to evaluate our model's ability to perform low-shot learning.

## Contact

Author: Ronald Kemker

E-mail: rmk6217@rit.edu

Website: [http://www.cis.rit.edu/~rmk6217/](http://www.cis.rit.edu/~rmk6217/)
