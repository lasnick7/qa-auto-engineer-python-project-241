### Hexlet tests and linter status:
[![Actions Status](https://github.com/lasnick7/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/lasnick7/python-project-50/actions)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=lasnick7_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=lasnick7_python-project-50)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=lasnick7_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=lasnick7_python-project-50)
[![Python CI](https://github.com/lasnick7/python-project-50/actions/workflows/my-personal-check.yml/badge.svg)](https://github.com/lasnick7/python-project-50/actions/workflows/my-personal-check.yml)

# gendiff

gendiff - is a program that looks for the differences between the two files of json or yaml formats and displays the result on the screen

## Installation

- Сloning and installing
```
$ git clone git@github.com:lasnick7/python-project-50.git
$ make install
```
- Launching the program
```
$ make build 
$ make package-install
```
Output formats:
```
- gendiff -f stylish filepath1 filepath2 - shows clearly the differences in the two files;
- gendiff -f plain filepath1 filepath2 - shows the changes flatly.
- gendiff -f json filepath1 filepath2 - shows changes in the json format
```