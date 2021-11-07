import os

os.system("flake8 controller.py --max-line-length 119 --format=html --htmldir=flake8_rapport\controller")
os.system("flake8 model.py --max-line-length 119 --format=html --htmldir=flake8_rapport\model")
os.system("flake8 view --max-line-length 119 --format=html --htmldir=flake8_rapport\view")