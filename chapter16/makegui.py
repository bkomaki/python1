# -*- coding: utf-8 -*-
# Run the build process by running the command 'python setup.py build'
from cx_Freeze import setup, Executable
buildOptions = dict(excludes = ["PyQt5 ","scipy", "numpy", "sqlite3"],
                    include_files  = ['data/Rain.csv'],
                    zip_include_packages=["."],
                    options = {"build_exe":{"includes": ["tkinter"]}},
                    
                    include_msvcr= True)
executables = [Executable('makegui.py')]

setup(name='spi',
      version='0.1',
      description='SPI Calculation',
      executables=executables,
      options=dict(build_exe=buildOptions))
