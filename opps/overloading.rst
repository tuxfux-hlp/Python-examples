Overloading in python
----------------------

Lets understand the overloading in python. Lets go with the example below.

::
  
  In [1]: def my_func(a,b):
   ...:     return a,b
   ...: 

  In [2]: def my_func(a,b,c):
   ...:     return a,b,c
   ...: 

  In [3]: my_func(1,2)
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  <ipython-input-3-97f1c12c1945> in <module>()
  ----> 1 my_func(1,2)

  TypeError: my_func() takes exactly 3 arguments (2 given)

  In [4]: 

If you notice we got a TypeError which makes when we tried to call our function - my_func with two arguments. Even though we have that defination it didn't work
for us. So we can say that the function overloading doesn't work.

Now lets try to go ahead with a more pythonic way :)

::
  
  In [4]: def my_func(IsInstanceOf,*args):
   ...:     value=IsInstanceOf
   ...:     if value == 'int':
   ...:         result = 0
   ...:     if value == 'str':
   ...:         result = ''
   ...:     for i in args:
   ...:         result = result + 1
   ...:     return result
 
Output

::
  
  In [6]: print my_func('int',1,2,3)
  6

  In [8]: print my_func('str','hello',' it',' works',' do',' you',' know')
  hello it works do you know

So we have a pythonic way of making sure that  function overloading works.


