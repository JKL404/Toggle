# Toggle
Toggle is a python package for string to toggle the string

[![image](https://img.shields.io/pypi/v/py-package-template.svg)](https://pypi.org/project/py-package-template/)
[![Build Status](https://travis-ci.org/AlexIoannides/py-package-template.svg?branch=master)](https://travis-ci.org/AlexIoannides/py-package-template)

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
pip install git+https://github.com/JKL404/Toggle.git
#or
pip install Toggle

```

#Running 
```
from Toggle.Toggle import Toggle
Toggle("My StriNg",choice) #default choice is 0
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
(0): Default 
output:  jOKer BEAUTIFUL

(1): Toggle with lowerUPPERlowerUPPER ....
output: jOkEr BeAuTiFuL

(2): Toggle with UPPERlowerUPPERlower ....
output: JoKeR bEaUtIfUl

(3): Toggle with lowerUPPERUPPER  lowerUPPERUPPER ....
output: jOKER bEAUTIFUL

(4): Toggle with UPPERlowerlower  UPPERlowerlower ....
output: Joker Beautiful
