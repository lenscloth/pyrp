import numpy as np
import os

params = {}
# Parameter specification:
params['approxFinalNBoxes'] = 10000  # Approximate number of proposals
params['rSeedForRun'] = -1 # Random seed to be used (-1 to generate it with a hashing function)
params['q'] = 10 # Parameter to eliminate near duplicates (raise it to eliminate more duplicates)

# LAB segmentation
params['colorspace'] = 'LAB'  # Colorspace: 'RGB', 'LAB', 'opponent', 'rg', 'HSV'

# superpixels
params['superpixels'] = {}
params['superpixels']['sigma'] = 0.8
params['superpixels']['c'] = 100
params['superpixels']['min_size'] = 100

# Parameters trained from VOC07:
params['simWeights'] = {}
params['simWeights']['wLABColorHist'] = -2.6864
params['simWeights']['wBias'] = 3.0017
params['simWeights']['wCommonBorder'] = -1.0029
params['simWeights']['wSizePer'] = -2.3655

# Size term alpha, as explained in the paper sec. 4.2.
# It is quantized to contain exactly 2^16 elements for speed

# The paper:
# S. Manen, M. Guillaumin, and L. Van Gool.
# Prime Object Proposals with Randomized Prim's Algorithm. In ICCV, 2013.

package_path = os.path.dirname(__file__)
params['alpha'] = np.load(os.path.join(package_path,'./data/alpha_voc07.npy'))
params['verbose'] = False # Set to true to display more information during execution

def get_params():
    return params