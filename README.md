## About

PythonVectors is a simple package for Python >= 3.6 which contains classes for Vector2 and Vector3, complete with overloads for almost all operators.

## Installation

```shell
python -m pip install git+https://github.com/evs-dev/PythonVectors#egg=PythonVectors
```

## Usage

Vector2 and Vector3 have identical functionality, the only difference being that Vector3 has a `z` attribute.

```python
from python-vectors import Vector2, Vector3

>>> Vector2()
Vector2(0, 0)

>>> Vector3()
Vector3(0, 0, 0)

a = Vector2(2, 4)
b = Vector2(-3, 6)

'''Functions for getting normali[s/z]ed vector and magnitude'''

>>> a.get_normalised()
Vector2(~0.447, ~0.89)

>>> a.get_normalized()
Vector2(~0.447, ~0.89)

>>> a.get_magnitude()
4.4721359549995

>>> a.get_square_magnitude()
20

>>> a.get_normalised().get_magnitude()
1.0

'''Most common arithmetic operators are supported'''

# +, -, *, /, //, %

>>> a + b
Vector2(-1, 10)

>>> a - b
Vector2(5, -2)

>>> a * b
Vector2(-6, 24)

>>> b / a
Vector2(-1.5, 1.5)

>>> a // b
Vector2(-1, 10)

>>> a % b
Vector2(-1, 4)

'''All comparison operators are supported for both vector types'''

# ==, !=, >, >=, <, <=

>>> Vector2(14, 5) == Vector3(14, 5, 0)
True
```
