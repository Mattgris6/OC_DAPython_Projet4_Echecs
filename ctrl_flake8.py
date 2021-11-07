import os

command = 'flake8 main.py ctrl_flake8.py view controller model'\
    ' --max-line-length 119 --format=html --htmldir=flake8_rapport'
os.system(command)
