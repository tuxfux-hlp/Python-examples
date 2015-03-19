How do i switch between python 2.x and python 3.x versions using ipython ?

First i installed the python2 and python3 versions

::
    
    sudo apt-get install python
    sudo apt-get install python3
    
Later i installed ipython and tried to work it on both python2 and python3. 

ipython only works with python2.
So we need to install ipython3 to get working with python 3 versions.

::
    
    sudo apt-get install ipython
    sudo apt-get install ipython3
    
Verification that its working as expected

::

    santosh@santosh-key2gyaan:~$ ipython
    Python 2.7.8 (default, Oct 20 2014, 15:05:19) 
    Type "copyright", "credits" or "license" for more information.

    IPython 2.3.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: quit()


    santosh@santosh-key2gyaan:~$ ipython3
    Python 3.4.2 (default, Oct  8 2014, 13:08:17) 
    Type "copyright", "credits" or "license" for more information.

    IPython 2.3.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: quit()

    


