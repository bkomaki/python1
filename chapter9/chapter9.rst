فصل 9
صفحه
127

.. code:: ipython3

    import math

فصل 9
صفحه
128

.. code:: ipython3

    math.e




.. parsed-literal::

    2.718281828459045



.. code:: ipython3

    math.pi




.. parsed-literal::

    3.141592653589793



.. code:: ipython3

    math.ceil(2.4)




.. parsed-literal::

    3



.. code:: ipython3

    math.ceil(-2.4)




.. parsed-literal::

    -2



.. code:: ipython3

    math.floor(2.4)




.. parsed-literal::

    2



.. code:: ipython3

    math.floor(-2.4)




.. parsed-literal::

    -3



.. code:: ipython3

    math.exp(3)
    




.. parsed-literal::

    20.085536923187668



.. code:: ipython3

    math.exp(1)




.. parsed-literal::

    2.718281828459045



.. code:: ipython3

    math.log(20)




.. parsed-literal::

    2.995732273553991



.. code:: ipython3

    math.log10(20)




.. parsed-literal::

    1.3010299956639813



.. code:: ipython3

    math.pow(2,3)




.. parsed-literal::

    8.0



.. code:: ipython3

    math.sqrt(16)




.. parsed-literal::

    4.0



.. code:: ipython3

    math.hypot(2, 3)




.. parsed-literal::

    3.605551275463989



.. code:: ipython3

    math.radians(180)




.. parsed-literal::

    3.141592653589793



.. code:: ipython3

    math.degrees(math.pi/2)




.. parsed-literal::

    90.0



.. code:: ipython3

    math.cos(math.pi/4)




.. parsed-literal::

    0.7071067811865476



.. code:: ipython3

    math.acos(1)




.. parsed-literal::

    0.0



.. code:: ipython3

    math.acos(0.5)




.. parsed-literal::

    1.0471975511965979



فصل 9
صفحه
129

.. code:: ipython3

    math.acos(2)


::


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-21-2895e95f8689> in <module>
    ----> 1 math.acos(2)
    

    ValueError: math domain error


.. code:: ipython3

    math.sin(math.pi/2)




.. parsed-literal::

    1.0



.. code:: ipython3

    math.asin(1)




.. parsed-literal::

    1.5707963267948966



.. code:: ipython3

    math.tan(1)




.. parsed-literal::

    1.5574077246549023



.. code:: ipython3

    math.atan(2)




.. parsed-literal::

    1.1071487177940904



فصل 9
صفحه
130

.. code:: ipython3

    xd,xm,xs=54,23,50
    yd,ym,ys=36,54,34.8
    r = 6378137.00
    

.. code:: ipython3

    lat=yd+ym/60+ys/3600
    lon=xd+xm/60+xs/3600
    

.. code:: ipython3

    from math import radians,pi,log,tan, degrees

.. code:: ipython3

    x=r*radians(lon)

.. code:: ipython3

    phi=radians(lat)
    y=r*log((tan(pi/4+phi/2)))
    print(x,y)
    #6054883.07296385,   4428095.96908917


.. parsed-literal::

    6055471.078346323 4426522.954042474
    

فصل 9
صفحه
131

.. code:: ipython3

    from math import atan, sinh,degrees	
    degrees(x/r)
    phi_r=atan(sinh(y/r))
    phi_d=degrees(phi_r)
    phi_d
    




.. parsed-literal::

    36.90966666666667



فصل 9
صفحه
131

.. code:: ipython3

    import cmath

.. code:: ipython3

    cmath.sqrt(-1)




.. parsed-literal::

    1j



.. code:: ipython3

    2+cmath.sqrt(-66)




.. parsed-literal::

    (2+8.12403840463596j)



.. code:: ipython3

    cmath.pi




.. parsed-literal::

    3.141592653589793



.. code:: ipython3

    cmath.e




.. parsed-literal::

    2.718281828459045



.. code:: ipython3

    cmath.exp(2+4j)




.. parsed-literal::

    (-4.829809383269385-5.5920560936409816j)



.. code:: ipython3

    cmath.log(2+5j)




.. parsed-literal::

    (1.6836479149932368+1.1902899496825317j)



.. code:: ipython3

    cmath.log10(2+5j)




.. parsed-literal::

    (0.7311989989494779+0.5169363570120227j)



فصل 9
صفحه
132

.. code:: ipython3

    cmath.phase(complex(-1.0, 0.0))




.. parsed-literal::

    3.141592653589793



.. code:: ipython3

    cmath.phase(complex(-1.0, -0.0))




.. parsed-literal::

    -3.141592653589793



.. code:: ipython3

    r,p=cmath.polar(12+6j)
    r,p




.. parsed-literal::

    (13.416407864998739, 0.4636476090008061)



.. code:: ipython3

    (12**2+6**2)**0.5




.. parsed-literal::

    13.416407864998739



فصل 9
صفحه
133

.. code:: ipython3

    cmath.rect(r,p)




.. parsed-literal::

    (12+6j)



.. code:: ipython3

    cmath.cos(cmath.pi/2)




.. parsed-literal::

    (6.123233995736766e-17-0j)



.. code:: ipython3

    cmath.acos(2)




.. parsed-literal::

    -1.3169578969248166j



.. code:: ipython3

    cmath.sin(cmath.pi/2)




.. parsed-literal::

    (1+0j)



.. code:: ipython3

    cmath.asin(1)




.. parsed-literal::

    (1.5707963267948966+0j)



.. code:: ipython3

    cmath.asin(0j)




.. parsed-literal::

    0j



.. code:: ipython3

    cmath.asin(1+0j)




.. parsed-literal::

    (1.5707963267948966+0j)



.. code:: ipython3

    cmath.tan(1)




.. parsed-literal::

    (1.5574077246549023+0j)



.. code:: ipython3

    cmath.atan(2)




.. parsed-literal::

    (1.1071487177940904+0j)



فصل 9
صفحه
134
تمرین عملی
1

.. code:: ipython3

    #1
    from math import tan , pi,radians
    rad=radians(45)
    slope=tan(rad)*100
    print(slope)


.. parsed-literal::

    99.99999999999999
    

.. code:: ipython3

    #2
    from math import pi,atan,degrees
    slope=25
    rad=atan(25/100.)
    deg=degrees(rad)
    print(deg)
    


.. parsed-literal::

    14.036243467926479
    

.. code:: ipython3

    #3  
    a,b,c=4,13,15
    s=1/2.* (a+b+c)
    A=(s*(s-a)*(s-b)*(s-c))**0.5
    A
    




.. parsed-literal::

    24.0



.. code:: ipython3

    #3
    from math import sin,acos
    C_cos=(a**2+b**2-c**2)/(2*a*b)
    sin(acos(C_cos))*a*b/2




.. parsed-literal::

    24.0



.. code:: ipython3

    #4
    area=24
    from math import pi,sqrt
    sqrt(area/pi)
    




.. parsed-literal::

    2.763953195770684



