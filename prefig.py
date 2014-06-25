#github.com/rjsmethurst/prefig
"""
    An awesome plotting object to make any plot poster or presentation ready in the colour of your choice!
    
    R. J. Smethurst 
"""


import numpy as np
import matplotlib.pyplot as plt

class Prefig(plt.Figure):
    """
        A class that can replace the 'plt.figure' python plotting command to create poster and presentaiton ready plots instantly. Plots will be initialised with a transparent background. The font colour and axes colour must be specified - e.g. 'white' for a black background poster. Font sizes will be increased in proportion to the figure size specified. 
        
        :axcol:
            The colour of the axes of the plot (optional). Default is 'black' or 'k'.
        
        :fontcol:
            The colour of the axes labels and tick labels of the plot (optional). Default is 'black' or 'k'.
        
        :rot: 
            Rotation angle of axes tick labels of the plot (optional). Default is 45 degrees.
        
        :figsize:
            tuple of integers (optional). (width, height) in inches. Default is (16,12).
        :font: 
            font family (optional). Default from rc.font file. Can be specified within plot commands instead. 
        
        """
    def __init__(self, axcol='k', fontcol='k', rot=45, size=(16,12), font='serif'):
        self.axcol = axcol
        self.fontcol = fontcol
        self.rot = rot
        self.size = size
        self.font = font
        plt.rc('figure', figsize=size, facecolor='none'), edgecolor='none')
        plt.rc('savefig', dpi=300, facecolor='none', edgecolor='none', frameon='False')
        f = {'family':font}
        plt.rc('font', **f)
        plt.rc('text', color=fontcol)
        plt.rc('axes', labelsize='x-large', edgecolor=axcol, labelcolor=fontcol, facecolor='none')
        plt.rc('xtick', labelsize='large', color=fontcol)
        plt.rc('yrick', labelsize='large', color=fontcol)
        




