from flask import Flask, render_template, request
#from scipy.misc import imsave, imread, imresize
import numpy as np 
import keras.models
import re
import sys
import os
sys.path.append(os.path.abspath('./Traffic sign classification'))
from load import *
