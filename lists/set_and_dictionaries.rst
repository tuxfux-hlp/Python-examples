
What are sets in python ?
--------------------------

A set is an unordered collection with no duplicate elements.
A set is simply a collection of unique keys.

How do i create a set of elements ?
-------------------------------------

Lets go over a very quick example to understand the sets. 

::

	
    In [1]: fruits = ['apple','banana','orange','apple','banana']

    In [2]: print fruits
    ['apple', 'banana', 'orange', 'apple', 'banana']

    In [3]: my_set_fruits = set(fruits)

    In [4]: type(my_set_fruits)
    Out[4]: set

    In [5]: my_set_fruits
    Out[5]: {'apple', 'banana', 'orange'}
    
How to create an empty set .
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now don't get confused with the `{}` as seen in the output above. See how we are creating a new `set` and a `dictionary`.

::
    
    In [8]: my_empty_set = set()

    In [9]: type(my_empty_set)
    Out[9]: set

    In [10]: my_empty_set
    Out[10]: set()

    In [11]: my_empty_dict = {}

    In [12]: type(my_empty_dict)
    Out[12]: dict
    
What else can sets do ?
------------------------

Sets objects also support mathematical operations like union,intersection,difference, and symmetric difference.

::
    
    In [13]: a = set('abracadabra')

    In [14]: b = set('alacazam')

    In [15]: a
    Out[15]: {'a', 'b', 'c', 'd', 'r'}

    In [16]: b
    Out[16]: {'a', 'c', 'l', 'm', 'z'}

    In [17]: # Letters in a but not in b

    In [18]: a - b
    Out[18]: {'b', 'd', 'r'}

    In [19]: # Letters in either a or b

    In [20]: a | b
    Out[20]: {'a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'}

    In [21]: # Letters in both a and b

    In [22]: a & b
    Out[22]: {'a', 'c'}

    In [23]: # Letters in a or b but not both

    In [24]: a ^ b
    Out[24]: {'b', 'd', 'l', 'm', 'r', 'z'}
    
    
References: 
https://docs.python.org/2/tutorial/datastructures.html#sets
https://docs.python.org/2/library/sets.html
https://www.safaribooksonline.com/library/view/high-performance-python/9781449361747/ch04.html
http://en.wikibooks.org/wiki/Python_Programming/Sets





