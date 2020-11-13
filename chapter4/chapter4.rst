فصل 4
صفحه 45

.. code:: ipython3

    s = "GATTACA"

فصل 4
صفحه 46

.. code:: ipython3

    print ("Car "+str(5))


.. parsed-literal::

    Car 5
    

.. code:: ipython3

    len(s)




.. parsed-literal::

    7



فصل 4
صفحه 47

.. code:: ipython3

    s = "GATTACA"
    s[0]




.. parsed-literal::

    'G'



.. code:: ipython3

    s[1]




.. parsed-literal::

    'A'



.. code:: ipython3

    s[-1]




.. parsed-literal::

    'A'



.. code:: ipython3

    s[-2]




.. parsed-literal::

    'C'



.. code:: ipython3

    s[7]


::


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-8-b035325af127> in <module>
    ----> 1 s[7]
    

    IndexError: string index out of range


فصل 4
صفحه 48

.. code:: ipython3

    s = "GATTACA"
    s[1:3]
    




.. parsed-literal::

    'AT'



.. code:: ipython3

    s[:3]




.. parsed-literal::

    'GAT'



.. code:: ipython3

    s[4:]




.. parsed-literal::

    'ACA'



فصل 4
صفحه 49

.. code:: ipython3

    s[:]




.. parsed-literal::

    'GATTACA'



.. code:: ipython3

    s[::2]




.. parsed-literal::

    'GTAA'



.. code:: ipython3

    s[-2:2:-1]




.. parsed-literal::

    'CAT'



.. code:: ipython3

    s[::-1]




.. parsed-literal::

    'ACATTAG'



فصل 4
صفحه 50

.. code:: ipython3

    print ("Tab is here\t,New line\n is above")


.. parsed-literal::

    Tab is here	,New line
     is above
    

.. code:: ipython3

    s = 'Okay, there\'s a small one.'
    print(s)
    


.. parsed-literal::

    Okay, there's a small one.
    

.. code:: ipython3

     2\
       /5.
    




.. parsed-literal::

    0.4



.. code:: ipython3

    print ('C:\some\name')


.. parsed-literal::

    C:\some
    ame
    

فصل 4
صفحه 51

.. code:: ipython3

    print (r'C:\some\name')


.. parsed-literal::

    C:\some\name
    

.. code:: ipython3

    mystr = r"This is nochage \n"
    print (mystr)
    


.. parsed-literal::

    This is nochage \n
    

.. code:: ipython3

    s = "GATTACA"
    "G" in s
    
    




.. parsed-literal::

    True



.. code:: ipython3

    "GAT" in s
    




.. parsed-literal::

    True



.. code:: ipython3

    "AGT" in s 




.. parsed-literal::

    False



.. code:: ipython3

    len(s)




.. parsed-literal::

    7



فصل 4
صفحه 52

.. code:: ipython3

    s.count("T")




.. parsed-literal::

    2



.. code:: ipython3

    s.find("ATT")




.. parsed-literal::

    1



.. code:: ipython3

    s.find("T")




.. parsed-literal::

    2



.. code:: ipython3

    s.find("Q")




.. parsed-literal::

    -1



.. code:: ipython3

    s.rfind("A")




.. parsed-literal::

    6



فصل 4
صفحه 53

.. code:: ipython3

    path="/".join(("D:","tempt","test.tif"))
    print(path)
    


.. parsed-literal::

    D:/tempt/test.tif
    

.. code:: ipython3

    path.split("/")
    




.. parsed-literal::

    ['D:', 'tempt', 'test.tif']



.. code:: ipython3

    path.split(".")
    




.. parsed-literal::

    ['D:/tempt/test', 'tif']



.. code:: ipython3

    date="1392-12-25"
    date.split("-")
    




.. parsed-literal::

    ['1392', '12', '25']



.. code:: ipython3

    path="D:/tempt/test.tif"
    path_new=path.replace("D","C")
    print(path_new)
    


.. parsed-literal::

    C:/tempt/test.tif
    

.. code:: ipython3

    new=path.replace("tif","img")
    new
    




.. parsed-literal::

    'D:/tempt/test.img'



.. code:: ipython3

    path.startswith("C")




.. parsed-literal::

    False



.. code:: ipython3

    path.startswith("D")




.. parsed-literal::

    True



فصل 4
صفحه 54

.. code:: ipython3

    path.endswith("tif")




.. parsed-literal::

    True



.. code:: ipython3

    s.index("T")




.. parsed-literal::

    2



.. code:: ipython3

    s.rindex("T")




.. parsed-literal::

    3



.. code:: ipython3

    nums=(1,3,4)
    st="Numers are {0}, {1} and {2}".format(nums[0],nums[1],nums[2])
    print(st)
    
    


.. parsed-literal::

    Numers are 1, 3 and 4
    

.. code:: ipython3

    txt = "your score  is  {:d} ."
    txt.format(0b10001)
    




.. parsed-literal::

    'your score  is  17 .'



فصل 4
صفحه 55

.. code:: ipython3

    '{:6d}'.format(42)




.. parsed-literal::

    '    42'



.. code:: ipython3

    point="Lat:{y:0.3f},lon: {x:0.4f}".format(x=54.5,y=34.24)
    print(point)
    


.. parsed-literal::

    Lat:34.240,lon: 54.5000
    

.. code:: ipython3

    x,y=54.5,34.24
    print(f"Lat:{y},lon: {x}")


.. parsed-literal::

    Lat:34.24,lon: 54.5
    

.. code:: ipython3

    from math import pi
    '{:06.2f}'.format(pi)




.. parsed-literal::

    '003.14'



.. code:: ipython3

    txt = "You scored {:.2%}"     
    print(txt.format(0.252))     
    


.. parsed-literal::

    You scored 25.20%
    

.. code:: ipython3

    txt = "Your score {:%}"     
    print(txt.format(0.252))     
    


.. parsed-literal::

    Your score 25.200000%
    

.. code:: ipython3

    txt = "The temperature is between {:-} and {:-} degrees celsius."    
    print(txt.format(-3, 7))
    


.. parsed-literal::

    The temperature is between -3 and 7 degrees celsius.
    

.. code:: ipython3

    txt = "your score  is  {:,} ." 
    txt.format(1000000)
    




.. parsed-literal::

    'your score  is  1,000,000 .'



فصل 4
صفحه 56

.. code:: ipython3

    str(3).zfill(3)




.. parsed-literal::

    '003'



.. code:: ipython3

    y,m,d="2019","1","23"
    "-".join([y, m.zfill(2),d.zfill(2)])
    




.. parsed-literal::

    '2019-01-23'



.. code:: ipython3

    a=u"احمد"
    a
    




.. parsed-literal::

    'احمد'



.. code:: ipython3

    A="احمد"
    print(A)
    


.. parsed-literal::

    احمد
    

فصل 4
صفحه 57

.. code:: ipython3

    chr(97)




.. parsed-literal::

    'a'



.. code:: ipython3

    print (chr(216))


.. parsed-literal::

    Ø
    

.. code:: ipython3

    print (chr(955))


.. parsed-literal::

    λ
    

.. code:: ipython3

    print (chr(0x0D1))


.. parsed-literal::

    Ñ
    

.. code:: ipython3

    print (chr(209))


.. parsed-literal::

    Ñ
    

.. code:: ipython3

    ord("a")




.. parsed-literal::

    97



.. code:: ipython3

    ord(u"a")




.. parsed-literal::

    97



.. code:: ipython3

    for i in range(1568,1611,1):
        print (i,chr(i))
    


.. parsed-literal::

    1568 ؠ
    1569 ء
    1570 آ
    1571 أ
    1572 ؤ
    1573 إ
    1574 ئ
    1575 ا
    1576 ب
    1577 ة
    1578 ت
    1579 ث
    1580 ج
    1581 ح
    1582 خ
    1583 د
    1584 ذ
    1585 ر
    1586 ز
    1587 س
    1588 ش
    1589 ص
    1590 ض
    1591 ط
    1592 ظ
    1593 ع
    1594 غ
    1595 ػ
    1596 ؼ
    1597 ؽ
    1598 ؾ
    1599 ؿ
    1600 ـ
    1601 ف
    1602 ق
    1603 ك
    1604 ل
    1605 م
    1606 ن
    1607 ه
    1608 و
    1609 ى
    1610 ي
    

.. code:: ipython3

    'hello' + " " + '''world'''




.. parsed-literal::

    'hello world'



.. code:: ipython3

    print "Car"+1


::


      File "<ipython-input-70-7bfe08605718>", line 1
        print "Car"+1
                  ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Car"+1)?
    


فصل 4
صفحه 58

.. code:: ipython3

    print("Spam"*3)


.. parsed-literal::

    SpamSpamSpam
    

.. code:: ipython3

    5*"3"




.. parsed-literal::

    '33333'



.. code:: ipython3

    '17' * '87'


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-73-771cf903e209> in <module>
    ----> 1 '17' * '87'
    

    TypeError: can't multiply sequence by non-int of type 'str'


.. code:: ipython3

    'pythonisfun' * 7.0


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-74-968f35926313> in <module>
    ----> 1 'pythonisfun' * 7.0
    

    TypeError: can't multiply sequence by non-int of type 'float'


.. code:: ipython3

    "4"+"5"




.. parsed-literal::

    '45'



.. code:: ipython3

    int("4")+int("5")




.. parsed-literal::

    9



.. code:: ipython3

    float("3.14")




.. parsed-literal::

    3.14



.. code:: ipython3

    float(3)




.. parsed-literal::

    3.0



.. code:: ipython3

    float(input("Enter a value: "))+float(input("Enter another value: "))


.. parsed-literal::

    Enter a value: 13
    Enter another value: 9
    



.. parsed-literal::

    22.0



فصل 4
صفحه 59
تمرین عملی
1
