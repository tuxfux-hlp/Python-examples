Differences between python2 and python3
------------------------------------------

change 1: print
^^^^^^^^^^^^^^^^^

``print`` is a key word in python2

::
    
    In [5]: print "print in python 2.x"
    print in python 2.x
    
``print`` in a function in python3

::

    In [3]: print?
    Type:        builtin_function_or_method
    String form: <built-in function print>
    Namespace:   Python builtin
    Docstring:
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    
    In [4]: print("print in python 3.x")
    print in python 3.x






