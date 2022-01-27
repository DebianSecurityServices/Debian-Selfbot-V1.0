@echo off

color A

python -m pip install -r requirements.txt
cd slowloris
pyhon setup.py install || python3 setup.py install
cd ..

PAUSE