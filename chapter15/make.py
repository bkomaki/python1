# -*- coding: utf-8 -*-
from cx_Freeze import setup, Executable
buildOptions = dict(excludes = ['tkinter' ,"PyQt5 ","PIL""scipy", "numpy",
                                "sqlite3", "IPython"],
                    include_files  = ['data/Rain.csv'],
                    zip_include_packages=["."],
                    include_msvcr= True)
executables = [Executable('spi.py')]
setup(name='spi',, 
      version='0.2',
      description='SPI Calculation',
      executables=executables,
      options=dict(build_exe=buildOptions))
# Run the build process by running the command 'python setup.py build'
