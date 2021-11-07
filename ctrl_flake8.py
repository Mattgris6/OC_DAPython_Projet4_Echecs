import os

os.system("flake8 controller.py --max-line-length 119 --format=html --htmldir=flake8_rapport")
os.system("flake8 model.py --max-line-length 119 --format=html --htmldir=flake8_rapport")
os.system("flake8 view_create_player.py --max-line-length 119 --format=html --htmldir=flake8_rapport")
os.system("flake8 view_create_tournament.py --max-line-length 119 --format=html --htmldir=flake8_rapport")
os.system("flake8 view_main_menu.py --max-line-length 119 --format=html --htmldir=flake8_rapport")
os.system("flake8 view_players.py --max-line-length 119 --format=html --htmldir=flake8_rapport")
os.system("flake8 view_rounds.py --max-line-length 119 --format=html --htmldir=flake8_rapport")
os.system("flake8 view_tournament_menu.py --max-line-length 119 --format=html --htmldir=flake8_rapport")
os.system("flake8 view_tournaments.py --max-line-length 119 --format=html --htmldir=flake8_rapport")