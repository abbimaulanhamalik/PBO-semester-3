###Import Python Standard Library Modules
# import standard math module 
import math

# use math.pi to get value of pi
print("The value of pi is", math.pi)

###Python import with Renaming
# import module by renaming it
import math as m

print(m.pi)

# Output: 3.141592653589793

###Python from...import statement
# import only pi from math module
from math import pi

print(pi)

# Output: 3.141592653589793

###Import all names
# import all names from the standard module math
from math import *

print("The value of pi is", pi)