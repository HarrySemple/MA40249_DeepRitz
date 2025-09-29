# Document containing all architectures

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim, autograd
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.cbook as cbook
import matplotlib.patches as patches
#from ipywidgets import IntProgress
#from IPython.display import display
#import time

class deep_ritz(nn.module):
    """
    
    """
    def __init__(self,in_N,m,out_N,depth=0):