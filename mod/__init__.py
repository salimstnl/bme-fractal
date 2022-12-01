import sys, os.path as path
from inspect import getsourcefile

parent_dir = path.dirname(path.dirname(path.abspath(getsourcefile(lambda: 0))))
sys.path.append(path.join(parent_dir, 'RepositoryName'))

# make sure to hack the sys.path
# before importing your own modules

from . import module
from .module import *
