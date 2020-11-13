فصل3
صفحه
38

.. code:: ipython3

    tup1 = ('physics', 'chemistry', 1997, 2000)
    

.. code:: ipython3

    tup2 = (1, 2, 3, 4, 5)

.. code:: ipython3

    tup3 = "a", "b", "c", "d"

.. code:: ipython3

    tup1 = ()
    type(tup1)
    




.. parsed-literal::

    tuple



فصل3
صفحه
39

.. code:: ipython3

    tup1 = (50)
    type(tup1)
    




.. parsed-literal::

    int



.. code:: ipython3

    tup2=(50,)
    type(tup2)
    




.. parsed-literal::

    tuple



.. code:: ipython3

    tuple ([1, 2, 'three', False])




.. parsed-literal::

    (1, 2, 'three', False)



.. code:: ipython3

    tuple('hello')




.. parsed-literal::

    ('h', 'e', 'l', 'l', 'o')



.. code:: ipython3

    tuple({1:'one',2:'two'})




.. parsed-literal::

    (1, 2)



.. code:: ipython3

    tup1[0] = 100


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-034a7a67b47e> in <module>
    ----> 1 tup1[0] = 100
    

    TypeError: 'int' object does not support item assignment


.. code:: ipython3

    del tup1[0]


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-13-5f962e1876e1> in <module>
    ----> 1 del tup1[0]
    

    TypeError: 'int' object does not support item deletion


.. code:: ipython3

    tup3 = (1,3) + tup2
    print (tup3)
    


.. parsed-literal::

    (1, 3, 50)
    

.. code:: ipython3

    del tup3

.. code:: ipython3

    print (tup3)
    


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-18-1b42f0d6c145> in <module>
    ----> 1 print (tup3)
    

    NameError: name 'tup3' is not defined


فصل3
صفحه
41

.. code:: ipython3

    L = ('spam', 'Spam', 'SPAM!')

.. code:: ipython3

    L[2]




.. parsed-literal::

    'SPAM!'



.. code:: ipython3

    L[-2]




.. parsed-literal::

    'Spam'



.. code:: ipython3

    L[1:]




.. parsed-literal::

    ('Spam', 'SPAM!')



.. code:: ipython3

    x, y = 1, 2

.. code:: ipython3

    print ("Value of  x, y : ", x, y)


.. parsed-literal::

    Value of  x, y :  1 2
    

.. code:: ipython3

    print (min(('a','b','c')))


.. parsed-literal::

    a
    

.. code:: ipython3

    print (max((1,3,4)))


.. parsed-literal::

    4
    

.. code:: ipython3

    t=('a','b','b','c')

.. code:: ipython3

    print (t.count("b"))


.. parsed-literal::

    2
    

فصل3
صفحه
42

.. code:: ipython3

    print (t.index("b"))


.. parsed-literal::

    1
    

.. code:: ipython3

    x,y=2,5
    y,x=x,y
    print (x)
    


.. parsed-literal::

    5
    

.. code:: ipython3

    a,b,*c,d=[1,2,3,5,4,5,7]
    print(c)


.. parsed-literal::

    [3, 5, 4, 5]
    

.. code:: ipython3

    print(d)


.. parsed-literal::

    7
    

.. code:: ipython3

    None == None
    




.. parsed-literal::

    True



.. code:: ipython3

    print(None)


.. parsed-literal::

    None
    

.. code:: ipython3

    def say(s):
    	print(s)
    

.. code:: ipython3

    a=say("Hi")


.. parsed-literal::

    Hi
    

.. code:: ipython3

    print(a)


.. parsed-literal::

    None
    

فصل3
صفحه
43
تمرین عملی

