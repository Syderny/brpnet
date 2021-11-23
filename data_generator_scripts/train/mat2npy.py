import numpy as np
from scipy import io


imgs = np.load('C:/Users/DELL/workspace/brpnet/data_generator_scripts/val/data_after_stain_norm_mm_ref1.npy')
bnds = np.load('C:/Users/DELL/workspace/brpnet/data_generator_scripts/val/val_bnd.npy')
segs = np.load('C:/Users/DELL/workspace/brpnet/data_generator_scripts/val/val_seg.npy')
