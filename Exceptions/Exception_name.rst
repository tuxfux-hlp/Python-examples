How to get the name of the exceptions being called ?
------------------------------------------------------

I want to use exceptions in my code , also i want to print out the name of the 
exception being called.

Let me take a very simple example.

::

    In [5]: try:
        print name
    except NameError as exception:
        print type(exception).__name__
        print "Please enter the valid string"
       ...:     
    NameError
    Please enter the valid string

    In [6]: try:
        print name
    except:
        print type(exception).__name__
        print "Please enter the valid string"
       ...:     
    NameError
    Please enter the valid string

