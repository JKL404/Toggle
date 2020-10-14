# Toggle
Toggle is a python package for string to toggle the string

[![image](https://img.shields.io/pypi/v/py-package-template.svg)](https://pypi.org/project/py-package-template/)
[![Build Status](https://travis-ci.org/AlexIoannides/py-package-template.svg?branch=master)](https://travis-ci.org/AlexIoannides/py-package-template)

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
pip install git+https://github.com/JKL404/Toggle.git

```

#Running 
```
from Toggle import Toggle
Toggle("My StriNg")
```

Syntax:
```
Toggle(string, choice)
```
Example:
```
Toggle("JokER beautiful",choice)
```
Added Choice Option:
__________________
0: Default 
output:  jOKer BEAUTIFUL

1: Toggle with <lower><UPPER><lower><UPPER>....
output: jOkEr BeAuTiFuL

2: Toggle with <UPPER><lower><UPPER><lower>....
output: JoKeR bEaUtIfUl

3: Toggle with <lower><UPPER><UPPER>  <lower><UPPER><UPPER>....
output: jOKER bEAUTIFUL

4: Toggle with <UPPER><lower><lower>  <UPPER><lower><lower>....
output: Joker Beautiful
