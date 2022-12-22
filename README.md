# ChNumber
Python module that formats Persian number to Latin

# clone
```bash
git clone https://github.com/Izolabela/ChNumber
```


# Usage
```python
from ChNumber import ChNumber

print(ChNumber.format("۰۹۱۴۴۱۲۳۵۱۲")) 
# Output: 
09144123512

help(ChNumber)
# Output:
Help on class ChNumber in module ChNumber:

class ChNumber(builtins.object)
 |  :: Converts Farsi numbers to Latin"
 |  
 |  Methods defined here:
 |  
 |  format(number)
 |      :: format method:
 |           -> Usage:
 |                  ChNumber.format(number)
 |           -> Example:
 |                  ChNumber.format("۰۹۱۴۶۵۷۹۸۱۴")
 |           -> Result:
 |                  "09146579814"
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


# You need to put this module to your working directory
```

> This is my first module! Hope you enjoy :)
