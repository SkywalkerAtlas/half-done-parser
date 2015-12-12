# -*- encoding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

from distutils.core import setup
import py2exe
from os import path
here = path.abspath(path.dirname(__file__))
setup(console=["run.py"],data_files=[("grammer",[path.join(here,'grammer',"grammer.txt"),path.join(here, 'grammer',"grammer2.txt"),path.join(here, 'grammer',"grammer3.txt")]),])