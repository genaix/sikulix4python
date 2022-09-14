#!/bin/bash

echo "Проверка flake8..."
flake8 --max-complexity 10 --max-line-length=120 --inline-quotes=double --exclude=venv --exclude=Lib --exclude=Scrupts --exclude=share sikulix4python
flake_result=$?

echo "Проверка vulture..."
vulture --min-confidence 70 --exclude=venv --exclude=Lib --exclude=Scrupts --exclude=share sikulix4python
vulture_result=$?

echo "Проверка pydocstyle..."
pydocstyle --convention=google sikulix4python
pydocstyle_result=$?

echo "Проверка pylint..."
pylint ./sikulix4python/*
pylint_result=$?

echo "Проверка mypy..."
mypy --python-version=3.10 --ignore-missing-imports sikulix4python
mypy_result=$?

#if [ $flake_result != 0 ] ||
#  [ $vulture_result != 0 ] ||
#  [ $pydocstyle_result != 0 ] ||
#  [ $pylint_result != 0 ] ||
#  [ $mypy_result != 0 ];
#then exit 1;
#else exit 0;
#fi
read -n 1
