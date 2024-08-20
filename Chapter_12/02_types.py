from typing import List, Union, Tuple, Dict

# ":" used with variable to specifies it type and uses it methods by (n.)
n: int = 5

name: str = "Mayank"


# "->" used with function to specifies it return type
def sum(a: int, b: int) -> int:
    print(a+b)


sum(3, 2)

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer person:
Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345  # Also valid

# These annotations help in making the code self-documenting and allow developers to understand the data structures used at a glance.
