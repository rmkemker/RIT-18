"""
Name: evaluate_rit18.py
Author: Ronald Kemker
Description: Evaluate performance on the RIT-18 dataset.

Note:
See paper for details: https://arxiv.org/abs/1703.01918
"""

import numpy as np
from scipy.io import loadmat, savemat
from sklearn.metrics import confusion_matrix

def Evaluate_RIT18(y_true, y_pred, mask, file_name=None):
    """Standardized evaluation metrics for the RIT-18 dataset.
    
    Parameters
    ----------
    y_true : numpy array or string.  If array, this contains the pixel-wise
        truth map.  If string, this contains a filepath to the truth map.
        File formats supported include .npy (Python) and .mat (MATLAB).
    y_pred : numpy array or string.  If array, this contains the pixel-wise
        prediction map.  If string, this contains a filepath to the 
        prediction map. File formats supported include .npy (Python) and 
        .mat (MATLAB).
    mask : numpy array (int), contains mask where predictions are valid
    file_name: string (optional), file path to store the metrics.  This is
        stored as a dictionary in a .mat file.
    
    Returns
    -------
    metrics : Dictionary with the following keys: 'confusion_matrix',
        'overall_accuracy', 'mean-class_accuracy', and 
        'kappa_statistic'        
    """
        
    if type(y_true) == str:
        
        if y_true[-3:] == 'npy':
            y_true = np.load(y_true)[mask>0].ravel()
        elif y_true[-3:] == 'mat':
            y_true = loadmat(y_true)['test_labels'][mask>0].ravel()
        else:
            raise IOError('Unrecognized filetype for y_true.')
    elif type(y_true) == np.ndarray:
        y_true = y_true[mask>0].ravel()
    else:
        raise IOError('Unrecognized datatype for y_true.')
        
        
    if type(y_pred) == str:
        if y_pred[-3:] == 'npy':
            y_pred = np.load(y_pred)[mask>0].ravel()
        elif y_pred[-3:] == 'mat':
            y_pred = loadmat(y_pred)[mask>0].ravel()
        else:
            raise IOError('Unrecognized filetype fir y_pred.')        
    elif type(y_pred) == np.ndarray:
        y_pred = y_pred[mask>0].ravel()
    else:
        raise IOError('Unrecognized datatype for y_pred.')    
    
    c = confusion_matrix(y_true, y_pred)
    oa = np.sum(np.diag(c))/np.sum(c)
    aa = np.mean(np.diag(c)/np.sum(c, axis=1))
    e = np.sum(np.sum(c,axis=1)*np.sum(c,axis=0))/np.sum(c)**2             
    kappa = (oa-e)/(1-e)

    metrics = {'confusion_matrix':c,
               'overall_accuracy':oa,
               'mean_class_accuracy':aa,
               'kappa_statistic':kappa}
    
    if file_name is not None:
        savemat(file_name , metrics)
    
    return metrics


    
    
