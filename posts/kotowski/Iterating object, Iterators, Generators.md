## Iterables
An iterable is an object capable of **returning** its **members** **one by one**. Said in other words, an iterable is anything that you can loop over with a `for` loop in Python.
### Sequences
Sequences are a very common **type** of **iterable**. Built-in sequence types are:
- [**lists**](https://docs.python.org/3.3/library/stdtypes.html#list)
- [**strings**](https://docs.python.org/3.3/library/stdtypes.html#str)
- [**tuples**](https://docs.python.org/3.3/library/stdtypes.html#tuple)

Sequences support such magic methods as:
- `__getitem__(self, key)` used for notation `self[key]`
- `__setitem__(self, key, value)` used for notation `self[key] = value`
- `__len__()` method that returns the **length** of the sequence.

```python
class MyContainer(object):  
  
	def __init__(self):  
		self.storage = {}  

	def __setitem__(self, key, value):  
		self.storage[key] = value  

	def __getitem__(self, key):  
		return self.storage[key]
	
	def __len__(self):
		return len(self.storage)
```
### Other Iterables
Many things in Python are iterables, but not all of them are sequences. **Dictionaries**, **file objects**, **sets**, and **generators** are all iterables, but none of them is a sequence.

## Iterators

An iterator is an object representing a **stream of data**. You can create an iterator object by applying the `iter()` built-in function to an **iterable**.
```python
a = ["h","e","l","l","o"]
iterator = iter(a)  # <list_iterator object at 0x038ECCB0>
print(next(iterator)) # h
```
You can use an iterator to manually **loop over** the **iterable** it came from. A repeated passing of iterator to the built-in function `next()`returns **successive items** in the **stream**. Once, when you consumed an item from an iterator, it’s gone. When no more data are available a `StopIteration` exception is raised.
