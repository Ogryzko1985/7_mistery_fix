# Quadratic Equations Solver

1) Чтобы сделать неотслеживаемыми файлы  на винчестере в папке, имеющие расширение .py или .pyc и удалить из репозитория 
нужно выполнить команду
find . | grep -E "(__pycache__|\.pyc$)" | xargs rm -rf -для файлов c расщирением *pyc или
find . | grep -E "(7_mistery_fix|\.py$)" | xargs rm -rf  - для файлов с расширением *.py в папке 7_mistery_fix.
2) выполнить команду git rm --cached --__pycache__/ - для папки
или git rm --cached -- quadratic_equation.cpython-36.pyc - для файла
3) git push origin master



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
