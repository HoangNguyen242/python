>>> def a(*args, **kargs):
...   print args[0]
...   print args[1]
...   print kargs['a']
...   print kargs['b']
... 
>>> a()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in a
IndexError: tuple index out of range
>>> a(1, 2, a=3, b=4)
1
2
3
4
>>> def a(a=0, *args, **kargs):
...   print args[0]
...   print args[1]
...   print kargs['a']
...   print kargs['b']
... 
>>> a(1, 2, a=3, b=4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: a() got multiple values for keyword argument 'a'
>>> a(1, 2, b=4)
2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in a
IndexError: tuple index out of range
>>> a(1, 2, 3, b=4)
2
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in a
KeyError: 'a'