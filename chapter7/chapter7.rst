فصل 7 صفحه 85

.. code:: ipython3

    4 or 5 




.. parsed-literal::

    4



.. code:: ipython3

    5 or 4 




.. parsed-literal::

    5



.. code:: ipython3

    5 and 4




.. parsed-literal::

    4



فصل 7 صفحه 86

.. code:: ipython3

    1==1.




.. parsed-literal::

    False



.. code:: ipython3

    1<1.




.. parsed-literal::

    False



.. code:: ipython3

    1 is 1.




.. parsed-literal::

    False



.. code:: ipython3

    3<2

فصل 7 صفحه 87

.. code:: ipython3

    3<"2"


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-9-6be3297ba6bc> in <module>
    ----> 1 3<"2"
    

    TypeError: '<' not supported between instances of 'int' and 'str'


.. code:: ipython3

    c1=3
    c2=3+0j
    c1==c2




.. parsed-literal::

    True



.. code:: ipython3

    c1 is c2




.. parsed-literal::

    False



.. code:: ipython3

    0 or 0




.. parsed-literal::

    0



.. code:: ipython3

    0 or 23
    




.. parsed-literal::

    23



.. code:: ipython3

    11 or 23
    




.. parsed-literal::

    11



.. code:: ipython3

    23 or 11




.. parsed-literal::

    23



فصل 7 صفحه 88

.. code:: ipython3

    x=5
    x>0 and x<10
    




.. parsed-literal::

    True



.. code:: ipython3

    y=6
    not(x<y)
    




.. parsed-literal::

    False



فصل 7 صفحه 89

.. code:: ipython3

    12|50




.. parsed-literal::

    62



.. code:: ipython3

    bin(12)




.. parsed-literal::

    '0b1100'



.. code:: ipython3

    bin(50)




.. parsed-literal::

    '0b110010'



.. code:: ipython3

    bin(62)




.. parsed-literal::

    '0b111110'



فصل 7 صفحه 90

.. code:: ipython3

    60^50




.. parsed-literal::

    14



.. code:: ipython3

    60&50




.. parsed-literal::

    48



.. code:: ipython3

    bin(60) 
    




.. parsed-literal::

    '0b111100'



.. code:: ipython3

    bin(50)




.. parsed-literal::

    '0b110010'



.. code:: ipython3

    bin(48)




.. parsed-literal::

    '0b110000'



فصل 7 صفحه 91

.. code:: ipython3

    ~15




.. parsed-literal::

    -16



.. code:: ipython3

    bin(~15)




.. parsed-literal::

    '-0b10000'



.. code:: ipython3

    bin(15)




.. parsed-literal::

    '0b1111'



.. code:: ipython3

    int('01111',2)




.. parsed-literal::

    15



.. code:: ipython3

    int('10000',2)




.. parsed-literal::

    16



.. code:: ipython3

    a=5
    a<<3
    




.. parsed-literal::

    40



.. code:: ipython3

    bin(5)
    
    




.. parsed-literal::

    '0b101'



.. code:: ipython3

    bin(40)




.. parsed-literal::

    '0b101000'



فصل 7 صفحه 92

.. code:: ipython3

    a<<=1

.. code:: ipython3

    a




.. parsed-literal::

    24



.. code:: ipython3

    a<<=1

.. code:: ipython3

    a




.. parsed-literal::

    48



.. code:: ipython3

    a=96
    a>>=3
    a
    




.. parsed-literal::

    12



.. code:: ipython3

    a>>=3
    >>> a
    




.. parsed-literal::

    1



.. code:: ipython3

    bin(40)
    




.. parsed-literal::

    '0b101000'



.. code:: ipython3

    40>>2
    




.. parsed-literal::

    10



.. code:: ipython3

    bin(10)




.. parsed-literal::

    '0b1010'



.. code:: ipython3

    False == False or True




.. parsed-literal::

    True



.. code:: ipython3

    False == (False or True)




.. parsed-literal::

    False



.. code:: ipython3

    (False == False) or True




.. parsed-literal::

    True



فصل 7 صفحه 93 تمرین عملی 1

.. code:: ipython3

    n=84
    n%3==0 and n%7==0
    




.. parsed-literal::

    True



