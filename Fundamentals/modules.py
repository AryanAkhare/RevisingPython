import math
import random
from enum import Enum

# Math module
print(math.pi)  # Prints value of pi

# List all attributes/methods in random module
for item in dir(random):
    print(item)

# Special __name__ attribute
print(__name__)        # Returns "__main__" when run directly
print(math.__name__)   # Returns module name: "math"
