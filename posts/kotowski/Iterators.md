# Iterators
_Iterators_ are such object which iterates over _itarables_. For one _iterable_ there could be created few iterators.

When _iterable_ is passed to `for ... in ` loop, actually the _iterator_ is being passed in it.

Iterables
   - Sequences
      - lists
      - tuples
	  - strings
   - Other
      - sets
      - dict
	  - file objects
	  - generators
# Iterator Protocol
The iterator objects are required to support the following **two methods**, which together form the **iterator protocol**:

-   iterator.__iter__()  
    Return the **iterator object itself**. This is required to allow both containers (also called collections) and iterators to be used with the `for` and `in` statements.
-   iterator.__next__()  
    Return the **next item** from the container. If there are no more items, raise the **StopIteration** exception.

Iterators are such object which are created to be used in `for ... in` loops.
```python
a = [1, 2, 3]

for i in a: print(i)
```
is equivalent to:
```python
a = [1, 2, 3]

iterator = iter(a)  # <list_iterator object at 0x038ECCB0>
while True:
	try:
		print(next(iterator))
	except StopIteration:
		break
	
```