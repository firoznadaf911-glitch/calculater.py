import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Parse inputs from command line arguments (e.g., python script.py 10 5)
# If not provided, default to x = 10, y = 5
if len(sys.argv) >= 3:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
else:
    x, y = 10, 5

print(f"Addition: {add(x, y)}")        # Output: 15.0 (or 15)
print(f"Subtraction: {subtract(x, y)}")  # Output: 5.0 (or 5)