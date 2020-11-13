فصل2
صفحه
14

.. code:: ipython3

    type(10)




.. parsed-literal::

    int



.. code:: ipython3

    id(10)




.. parsed-literal::

    140707439157936



.. code:: ipython3

    10 is 10.0




.. parsed-literal::

    False



.. code:: ipython3

    myNumber=23
    mynumber=54
    

فصل2
صفحه
15

.. code:: ipython3

    #dir(__builtins__)

.. code:: ipython3

    if=2


::


      File "<ipython-input-9-59fb53b11f09>", line 1
        if=2
          ^
    SyntaxError: invalid syntax
    


.. code:: ipython3

    type(str)




.. parsed-literal::

    type



.. code:: ipython3

    str=12

.. code:: ipython3

    type(str)




.. parsed-literal::

    int



.. code:: ipython3

    type(str)




.. parsed-literal::

    int



فصل2
صفحه
16


.. code:: ipython3

    pi_Value = 3.14
    ftrChanged = True
    fcName = "Streets"
    lstFC = ["Street", "Parcels", "Streams"]
    dictFC = {0:"Streetsv",1:"Parcels"}
    spatialExt = map.extent
    


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-16-c7cd42d8f283> in <module>
          4 lstFC = ["Street", "Parcels", "Streams"]
          5 dictFC = {0:"Streetsv",1:"Parcels"}
    ----> 6 spatialExt = map.extent
    

    AttributeError: type object 'map' has no attribute 'extent'


.. code:: ipython3

     repr(1==2)




.. parsed-literal::

    'False'



.. code:: ipython3

    3+7
    




.. parsed-literal::

    10



.. code:: ipython3

    5+2-4




.. parsed-literal::

    3



.. code:: ipython3

    10/5                                                                               




.. parsed-literal::

    2.0



.. code:: ipython3

    15/5




.. parsed-literal::

    3.0



.. code:: ipython3

    10/2




.. parsed-literal::

    5.0



.. code:: ipython3

    2**3




.. parsed-literal::

    8



.. code:: ipython3

    x=True
    type(x)




.. parsed-literal::

    bool



.. code:: ipython3

    3==2+1




.. parsed-literal::

    True



.. code:: ipython3

    "Seven"=="seven"




.. parsed-literal::

    False



.. code:: ipython3

    "Seven"!="seven"




.. parsed-literal::

    True



.. code:: ipython3

    1!=2




.. parsed-literal::

    True



.. code:: ipython3

     0b111111




.. parsed-literal::

    63



.. code:: ipython3

    0b11111111




.. parsed-literal::

    255



.. code:: ipython3

    bin(255)




.. parsed-literal::

    '0b11111111'



.. code:: ipython3

    type(-23)




.. parsed-literal::

    int



.. code:: ipython3

    b=-435
    type(b)




.. parsed-literal::

    int



فصل2
صفحه
19

.. code:: ipython3

    2147483648




.. parsed-literal::

    2147483648



.. code:: ipython3

    int(2**31)
    




.. parsed-literal::

    2147483648



.. code:: ipython3

    int(2**31-1)




.. parsed-literal::

    2147483647



.. code:: ipython3

    int(2**32/2.-1)




.. parsed-literal::

    2147483647



.. code:: ipython3

    int("234")




.. parsed-literal::

    234



.. code:: ipython3

    int("234.4")


::


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-39-14b8fd673a45> in <module>
    ----> 1 int("234.4")
    

    ValueError: invalid literal for int() with base 10: '234.4'


.. code:: ipython3

    f=50.6
    type(f)
    




.. parsed-literal::

    float



.. code:: ipython3

    1.3/0.4
    




.. parsed-literal::

    3.25



.. code:: ipython3

    1 / 2.0




.. parsed-literal::

    0.5



.. code:: ipython3

    1/3.




.. parsed-literal::

    0.3333333333333333



.. code:: ipython3

    k=12E-2
    k
    




.. parsed-literal::

    0.12



.. code:: ipython3

    type(k)




.. parsed-literal::

    float



.. code:: ipython3

    1.234565e4




.. parsed-literal::

    12345.65



.. code:: ipython3

    1.23e-7




.. parsed-literal::

    1.23e-07



فصل2
صفحه
21

.. code:: ipython3

    float(123)




.. parsed-literal::

    123.0



.. code:: ipython3

    float("12.4")




.. parsed-literal::

    12.4



.. code:: ipython3

    2+3j




.. parsed-literal::

    (2+3j)



.. code:: ipython3

    1j+1




.. parsed-literal::

    (1+1j)



.. code:: ipython3

    1j+1j




.. parsed-literal::

    2j



.. code:: ipython3

    1j*1j




.. parsed-literal::

    (-1+0j)



.. code:: ipython3

     complex(2,14)




.. parsed-literal::

    (2+14j)



.. code:: ipython3

    bin(23)




.. parsed-literal::

    '0b10111'



فصل2
صفحه
22

.. code:: ipython3

    0b10111




.. parsed-literal::

    23



.. code:: ipython3

    int("10111",2)




.. parsed-literal::

    23



.. code:: ipython3

    n=-32
    n.bit_length()
    




.. parsed-literal::

    6



.. code:: ipython3

    bin(n)




.. parsed-literal::

    '-0b100000'



.. code:: ipython3

    (0).bit_length()




.. parsed-literal::

    0



.. code:: ipython3

     hex(23)




.. parsed-literal::

    '0x17'



.. code:: ipython3

    int("0x17",16)




.. parsed-literal::

    23



.. code:: ipython3

    hex(3740)




.. parsed-literal::

    '0xe9c'



.. code:: ipython3

    f=23.0
    f.hex()




.. parsed-literal::

    '0x1.7000000000000p+4'



.. code:: ipython3

    f=3740.0
    f.hex()




.. parsed-literal::

    '0x1.d380000000000p+11'



فصل2
صفحه
23

.. code:: ipython3

    h=f.hex()
    float.fromhex(h)
    




.. parsed-literal::

    3740.0



.. code:: ipython3

    a=1+2

فصل2
صفحه
24

.. code:: ipython3

    12/2




.. parsed-literal::

    6.0



.. code:: ipython3

    12./2




.. parsed-literal::

    6.0



.. code:: ipython3

    (12+0j)/2




.. parsed-literal::

    (6+0j)



.. code:: ipython3

    var1=2
    var2=5
    var3=5.
    var1/var2




.. parsed-literal::

    0.4



.. code:: ipython3

    var1/var3




.. parsed-literal::

    0.4



.. code:: ipython3

    1.3%0.5




.. parsed-literal::

    0.30000000000000004



فصل2
صفحه
25

.. code:: ipython3

    50%7




.. parsed-literal::

    1



.. code:: ipython3

    -50%7




.. parsed-literal::

    6



.. code:: ipython3

    50//7




.. parsed-literal::

    7



.. code:: ipython3

    -50//7




.. parsed-literal::

    -8



.. code:: ipython3

    7%(5//2)




.. parsed-literal::

    1



.. code:: ipython3

    divmod(10, 3)




.. parsed-literal::

    (3, 1)



.. code:: ipython3

    from  __future__  import division
    2/4




.. parsed-literal::

    0.5



.. code:: ipython3

    4**2




.. parsed-literal::

    16



.. code:: ipython3

    1/4.**2 




.. parsed-literal::

    0.0625



.. code:: ipython3

    0.25**2




.. parsed-literal::

    0.0625



.. code:: ipython3

    4**(1/2)




.. parsed-literal::

    2.0



فصل2
صفحه
26

.. code:: ipython3

    4**(1/2)




.. parsed-literal::

    2.0



.. code:: ipython3

    pow(3,2)




.. parsed-literal::

    9



.. code:: ipython3

    pow(7,2,5)




.. parsed-literal::

    4



.. code:: ipython3

    7**2%5




.. parsed-literal::

    4



.. code:: ipython3

    pow(0,4)




.. parsed-literal::

    0



.. code:: ipython3

    pow(4,0)




.. parsed-literal::

    1



.. code:: ipython3

    pow(0,0)




.. parsed-literal::

    1



.. code:: ipython3

    2**0.5




.. parsed-literal::

    1.4142135623730951



.. code:: ipython3

    16**(1/2.)




.. parsed-literal::

    4.0



فصل2
صفحه
27

.. code:: ipython3

    from math import sqrt
    sqrt(16)
    




.. parsed-literal::

    4.0



.. code:: ipython3

    16**-2




.. parsed-literal::

    0.00390625



.. code:: ipython3

    8**(1/4.)




.. parsed-literal::

    1.681792830507429



.. code:: ipython3

    7**(2/5)




.. parsed-literal::

    2.17790642448278



.. code:: ipython3

    (-4)**0.5




.. parsed-literal::

    (1.2246467991473532e-16+2j)



.. code:: ipython3

    max(2,6)




.. parsed-literal::

    6



.. code:: ipython3

    min(2,6,7,-1)




.. parsed-literal::

    -1



.. code:: ipython3

    round(3.141592,4)




.. parsed-literal::

    3.1416



.. code:: ipython3

    round(12.1)




.. parsed-literal::

    12



.. code:: ipython3

    round(12.1231, 2)




.. parsed-literal::

    12.12



.. code:: ipython3

    (3.0).is_integer()




.. parsed-literal::

    True



.. code:: ipython3

    (3.14).is_integer()




.. parsed-literal::

    False



فصل2
صفحه
29

.. code:: ipython3

    x=12
    y=9
    y+=x
    

.. code:: ipython3

    print (y)


.. parsed-literal::

    21
    

.. code:: ipython3

    a=5
    a**=2
    print(a)
    


.. parsed-literal::

    25
    

فصل2
صفحه
30

.. code:: ipython3

    2+3*4+1




.. parsed-literal::

    15



.. code:: ipython3

    8/(1+1)




.. parsed-literal::

    4.0



.. code:: ipython3

    2**3/2+3




.. parsed-literal::

    7.0



فصل2
صفحه
31

.. code:: ipython3

    abs((-3) ** 3 - 20)




.. parsed-literal::

    47



.. code:: ipython3

    abs(-3 ** 3 - 20)




.. parsed-literal::

    47



.. code:: ipython3

    False==False or True




.. parsed-literal::

    True



.. code:: ipython3

    False==(False or True)




.. parsed-literal::

    False



.. code:: ipython3

    (False==False) or True




.. parsed-literal::

    True



.. code:: ipython3

    (-4)**(1/2)




.. parsed-literal::

    (1.2246467991473532e-16+2j)



.. code:: ipython3

    (-8)**(1/3)




.. parsed-literal::

    (1.0000000000000002+1.7320508075688772j)



.. code:: ipython3

    2+4j+4+7j




.. parsed-literal::

    (6+11j)



.. code:: ipython3

    2+4j*4+7j




.. parsed-literal::

    (2+23j)



.. code:: ipython3

    2+4j/4+7j




.. parsed-literal::

    (2+8j)



.. code:: ipython3

    (2.+4j)/(4.+7j)




.. parsed-literal::

    (0.5538461538461539+0.03076923076923076j)



فصل2
صفحه
32

.. code:: ipython3

    from fractions import Fraction

.. code:: ipython3

    Fraction(18,12)




.. parsed-literal::

    Fraction(3, 2)



.. code:: ipython3

    Fraction("5/6")+4




.. parsed-literal::

    Fraction(9, 4)



.. code:: ipython3

    Fraction()




.. parsed-literal::

    Fraction(0, 1)



.. code:: ipython3

    Fraction('3/7')




.. parsed-literal::

    Fraction(3, 7)



.. code:: ipython3

    Fraction('1.414213 \t\n')




.. parsed-literal::

    Fraction(1414213, 1000000)



.. code:: ipython3

    Fraction('-.125')




.. parsed-literal::

    Fraction(-1, 8)



.. code:: ipython3

    Fraction('7e-6')




.. parsed-literal::

    Fraction(7, 1000000)



.. code:: ipython3

    Fraction(2.25)




.. parsed-literal::

    Fraction(9, 4)



.. code:: ipython3

    a=Fraction(1.1)

.. code:: ipython3

    a.limit_denominator()




.. parsed-literal::

    Fraction(11, 10)



فصل2
صفحه
33

.. code:: ipython3

    from math import pi
    Fraction(pi)
    
    
    


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-139-adf8ef3c368e> in <module>
          2 Fraction(pi)
          3 
    ----> 4 p.limit_denominator(100000)
    

    NameError: name 'p' is not defined


.. code:: ipython3

    p=Fraction(pi)
    p.limit_denominator(100)




.. parsed-literal::

    Fraction(311, 99)



.. code:: ipython3

    p.limit_denominator(100000)




.. parsed-literal::

    Fraction(312689, 99532)



.. code:: ipython3

    Fraction(12,8)+Fraction(3,5)




.. parsed-literal::

    Fraction(21, 10)



.. code:: ipython3

    from decimal import Decimal

.. code:: ipython3

    print(Fraction(Decimal('1.2')))


.. parsed-literal::

    6/5
    

.. code:: ipython3

    print(Fraction(Decimal('1.5')))


.. parsed-literal::

    3/2
    

.. code:: ipython3

    6/5




.. parsed-literal::

    1.2



.. code:: ipython3

    3/2




.. parsed-literal::

    1.5



.. code:: ipython3

    d=Decimal(1/2)+Decimal(2/3)
    f=Fraction(d)
    f.limit_denominator()
    




.. parsed-literal::

    Fraction(7, 6)



فصل2
صفحه
34
تمرین عملی
1

