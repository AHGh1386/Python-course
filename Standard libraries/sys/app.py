import sys

# Get the command line arguments
arguments = sys.argv
print("Command Line Arguments:", arguments)

# Get the Python version
version = sys.version
print("Python Version:", version)

# Get the maximum integer size
max_int = sys.maxsize
print("Maximum Integer Size:", max_int)

# Get the platform information
platform = sys.platform
print("Platform:", platform)

# Get the current recursion limit
recursion_limit = sys.getrecursionlimit()
print("Current Recursion Limit:", recursion_limit)

# Set a new recursion limit
new_limit = 2000
sys.setrecursionlimit(new_limit)
print("New Recursion Limit:", sys.getrecursionlimit())
