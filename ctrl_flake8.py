import os

os.system("flake8 view controller.py model.py --max-line-length 119 --format=html --htmldir=flake8_rapport")