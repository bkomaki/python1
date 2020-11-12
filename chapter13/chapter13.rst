فصل 13
صفحه 210

.. code:: ipython3

     if True:


::


      File "<ipython-input-1-2c8a33b52dfb>", line 1
        if True:
                ^
    SyntaxError: unexpected EOF while parsing
    


.. code:: ipython3

     a=2

.. code:: ipython3

    if True: 
        print(3)
            print(5)


::


      File "<ipython-input-3-9b05da8dd734>", line 3
        print(5)
        ^
    IndentationError: unexpected indent
    


صفحه 211

.. code:: ipython3

    print( 2))
    
    


::


      File "<ipython-input-5-0d19e79d6874>", line 1
        print( 2))
                 ^
    SyntaxError: invalid syntax
    


.. code:: ipython3

    while True print ('Hello world')

.. code:: ipython3

    def add2


::


      File "<ipython-input-6-7cb696691d83>", line 1
        def add2
                ^
    SyntaxError: invalid syntax
    


.. code:: ipython3

    a=3+8

.. code:: ipython3

    s=3+(6


::


      File "<ipython-input-8-83a60fa5f587>", line 1
        s=3+(6
              ^
    SyntaxError: unexpected EOF while parsing
    


.. code:: ipython3

    print ("hello)


::


      File "<ipython-input-9-084b2836777e>", line 1
        print ("hello)
                      ^
    SyntaxError: EOL while scanning string literal
    


.. code:: ipython3

    11/0


::


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-10-5be670730087> in <module>
    ----> 1 11/0
    

    ZeroDivisionError: division by zero


.. code:: ipython3

    4 + spam*3


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-c98bb92cdcac> in <module>
    ----> 1 4 + spam*3
    

    NameError: name 'spam' is not defined


.. code:: ipython3

    '2' + 2


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-d2b23a1db757> in <module>
    ----> 1 '2' + 2
    

    TypeError: can only concatenate str (not "int") to str


فصل 13
صفحه 212

.. code:: ipython3

    x=15
    if x>10:
        raise Exception("x should not exceed than 10, The vale was is {}".format(x))
    


::


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-13-165b16d1a701> in <module>
          1 x=15
          2 if x>10:
    ----> 3     raise Exception("x should not exceed than 10, The vale was is {}".format(x))
    

    Exception: x should not exceed than 10, The vale was is 15


.. code:: ipython3

    x=20
    assert(x<10), "x must  be lower than 10"
    


::


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-14-b455e116922a> in <module>
          1 x=20
    ----> 2 assert(x<10), "x must  be lower than 10"
    

    AssertionError: x must  be lower than 10


فصل 13
صفحه 214

.. code:: ipython3

    try: 
        import Tkinter as tk
    except: 
        import tkinter as tk

.. code:: ipython3

    try: 
        from tkinter import  messagebox as message
    except: 
        import  tkMessageBox as message

.. code:: ipython3

    try:
        a=12/0
    except ZeroDivisionError: 
        print ("Error")
    


.. parsed-literal::

    Error
    

فصل 13
صفحه 215

.. code:: ipython3

    try:
        import numpy
    except ImportError:
        print("Please install numpy")
    else:
        print("numpy is imported")


.. parsed-literal::

    numpy is imported
    

فصل 13
صفحه 215
تمرین عملی
مسئله 1

.. code:: ipython3

    n=10
    assert(type(n)==str),"must be string"
    

فصل 13
صفحه 215
تمرین عملی
مسئله 2

.. code:: ipython3

    n=6
    class new(Exception):
        def __init__(self,text):
            self.text=text
    try:
        if n<5:
            raise new("Input is less than 5")
        else:
            raise new("Input is greater than 5")
    except new as ce:
        print(ce.text)
    


.. parsed-literal::

    Input is greater than 5
    

