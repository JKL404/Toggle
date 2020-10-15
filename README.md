# Toggle
Toggle is a python package for string to toggle the given string.


[![version](https://img.shields.io/badge/version-1.1.1-yellow.svg)](https://pypi.org/project/Toggle/)
[![Build Status](https://travis-ci.org/AlexIoannides/py-package-template.svg?branch=master)](https://pypi.org/project/Toggle/)

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
pip install git+https://github.com/JKL404/Toggle.git
#or
pip install Toggle

```

**Running:**
```
from Toggle.Toggle import Toggle
Toggle("My StriNg",choice) #default choice is 0
```

**Syntax:**
```
Toggle(string, choice)
```
**Example:**
```
Toggle("JokER beautiful",0)
```
***Choice Option:***
__________________
* ***(0): Default***
   - **output:**  jOKer BEAUTIFUL

* ***(1): Toggle with lower_UPPER_lower_UPPER ..***
   - **output:** jOkEr BeAuTiFuL

* ***(2): Toggle with UPPER_lower_UPPER_lower ....***
  - **output:** JoKeR bEaUtIfUl

* ***(3): Toggle with lower_UPPER_UPPER  lower_UPPER_UPPER ....***
  - **output:** jOKER bEAUTIFUL

* ***(4): Toggle with UPPER_lower_lower  UPPER_lower_lower ....***
  - **output:** Joker Beautiful
  
  
  ____________________________
## ***Thanks :blush:***
  :heartbeat: Nakali :kissing_heart:
    PM  :heartpulse:
