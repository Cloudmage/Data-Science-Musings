# Array

An Array is a data structure that stores data in a one dimensional/linear way.

A simple array in Python can be created using the numpy function library.

To create an array of 40 numbers the following program lines can be used in Python.

```python
import numpy as np
array = np.arange(40)
array
```

This results in an array of numbers 0 to 39 (40 numbers)

```python
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39])
```

## Array Pros

- Arrays are simple structure and can be fast and efficient.
- Arrays can be fast for adding and reading elements.
- Data stored can be for a single type and name with multiple data elements.

## Array Cons

- An array can have a fixed size (static) and may be immutable.
- Linear Complexity at the time of insertion and deletion as elements of an array are stored in consecutive memory locations.

## Array Use Cases

A search engine may use an array to store data from a search to display a number of pages via a list of URLs.

Output from a query may use an array to store the results and display them.

### Reference Links

- [Array](https://en.wikipedia.org/wiki/Array_data_structure)
- [A Comprehensive Guide For Array Data Structure](https://medium.com/codeconvention/learn-array-data-structure-2fa01edd21c2)
- [Python Array](https://www.tutorialspoint.com/python_data_structure/python_arrays.htm)
