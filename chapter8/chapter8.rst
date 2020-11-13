فصل 8
صفحه
94

.. code:: ipython3

    if 6<10:
        print("6 is lower than 10")
    


.. parsed-literal::

    6 is lower than 10
    

.. code:: ipython3

    no=6
    if no <5:
        print (no,"is lower than 5")
    

فصل 8
صفحه
95

.. code:: ipython3

    a=9
    if a<10:
        print ("Value of a is less than 10")
    else:
        print ("Value of a is greater than 10")
    


.. parsed-literal::

    Value of a is less than 10
    

.. code:: ipython3

    a=3
    b=6
    
    if a>b:
        print (a)
    else:
        print (b)
        


.. parsed-literal::

    6
    

فصل 8
صفحه
96

.. code:: ipython3

    a=5
    if a==6:
        print("Yes")
    else:
        print ("No")
    


.. parsed-literal::

    No
    

.. code:: ipython3

    from datetime import datetime
    hour = datetime.now().hour
    if hour < 12:
        time_of_day = 'morning'
    else:
         time_of_day = 'afternoon'
    print ('Good %s, world!' % time_of_day)
    


.. parsed-literal::

    Good afternoon, world!
    

فصل 8
صفحه
97

.. code:: ipython3

    a=9
    >>> if a<10:
    	print ("a is less than ten.")
    elif a< 9:
    	print ("a is less than nine ")
    elif a<2:
    	print ("a is less than two")
    else:
    	print ("a is more than 10 or more")
    


.. parsed-literal::

    a is less than ten.
    

.. code:: ipython3

    a=7
    if a<2:
    	print ("a is lower than 2")
    elif  2<a<8:
    	print (" a is between 2 and 8")
    elif a==9:
    	print  ("a equals 9")
    elif a>9:
    	print ("a is greater than 9")
    


.. parsed-literal::

     a is between 2 and 8
    

.. code:: ipython3

    if 3>2 and 2!=2:
    	print ("two")
    elif 3!=3 or 3==3:
    	print ("three")
    


.. parsed-literal::

    three
    

.. code:: ipython3

    #NestedIF.py
    age = int(input("Please enter your age: "))
    if (age >= 12):
        print ("You are eligible to see the Football match.")
        if (age <= 20 or age >= 60):
            print("Ticket price is $15")
        else:
          print("Ticket price is $20")
    else:
        print ("You're not eligible to buy a ticket.")
    


.. parsed-literal::

    Please enter your age: 20
    You are eligible to see the Football match.
    Ticket price is $15
    

فصل 8
صفحه
100

.. code:: ipython3

    colors=["Red","Blue","Green", "Black"]
    >>> for c in colors:
    	print (c)
    


.. parsed-literal::

    Red
    Blue
    Green
    Black
    

.. code:: ipython3

    odd=0
    even=0
    for a in range(1,10):
    	if a%2:
    		odd+=1
    		print(a, "is odd")
    	else: 
    		even+=1
    


.. parsed-literal::

    1 is odd
    3 is odd
    5 is odd
    7 is odd
    9 is odd
    

فصل 8
صفحه
101

.. code:: ipython3

    print("Number of even numbers :",even)


.. parsed-literal::

    Number of even numbers : 4
    

.. code:: ipython3

    print("Number of odd numbers :",odd)


.. parsed-literal::

    Number of odd numbers : 5
    

.. code:: ipython3

    a = ["Mary", "had", "a", "little", "lamb"]
    for i in range(len(a)):
        print (i, a[i])
    


.. parsed-literal::

    0 Mary
    1 had
    2 a
    3 little
    4 lamb
    

.. code:: ipython3

    >>> list(enumerate(a))




.. parsed-literal::

    [(0, 'Mary'), (1, 'had'), (2, 'a'), (3, 'little'), (4, 'lamb')]



.. code:: ipython3

    #FOR_IN_break.py
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print (n, 'equals', x, '*', n/x)
                break
            else:
                pass
        print (n, 'is a prime number')


.. parsed-literal::

    2 is a prime number
    3 is a prime number
    4 equals 2 * 2.0
    4 is a prime number
    5 is a prime number
    6 equals 2 * 3.0
    6 is a prime number
    7 is a prime number
    8 equals 2 * 4.0
    8 is a prime number
    9 equals 3 * 3.0
    9 is a prime number
    

فصل 8
صفحه
102

.. code:: ipython3

    nums=[11,13,14,5,7,9,6]
    >>> if any([i%2==0 for i in nums]):
    	print ("At least one is even")
    


.. parsed-literal::

    At least one is even
    

.. code:: ipython3

    if all([i>4 for i in nums]):
    	print ("All values are more than 4")
    


.. parsed-literal::

    All values are more than 4
    


فصل 8
صفحه
103

.. code:: ipython3

    x=0
    while (x < 5):
         print(x)
         x += 1
    


.. parsed-literal::

    0
    1
    2
    3
    4
    

.. code:: ipython3

    x = 10;
    while (x < 5):
        print(x)
        x += 1
    else:
        print (" x is ",x, ",nochange ")
    


.. parsed-literal::

     x is  10 ,nochange 
    

فصل 8
صفحه
104

.. code:: ipython3

    x=0
    s=0
    while (x < 10):  
        s = s + x  
        x = x + 1  
    else :  
        print('The sum of first 9 integers : ',s)
    


.. parsed-literal::

    The sum of first 9 integers :  45
    

.. code:: ipython3

    x = 1
    s = 0  
    while (x < 10):
        s = s + x
        x = x + 1
        print("x",x)
        if (x == 5):
            break
        else :print('The sum of first 9 integers : ',s)
    
    


.. parsed-literal::

    x 2
    The sum of first 9 integers :  1
    x 3
    The sum of first 9 integers :  3
    x 4
    The sum of first 9 integers :  6
    x 5
    

فصل 8
صفحه
105

i=0
while True:
    i+1
    if i==2:
        print("skiping")
        continue
    elif i==5:
        print("breaking")
        break
    print(i)
    
    

while True:
      pass


.. code:: ipython3

    x=3
    y=6
    if not 2+2==x or y==6 and 8==9:
        print ( "Yes")
    else:
        print ("No")
    


.. parsed-literal::

    Yes
    

فصل 8
صفحه
106

.. code:: ipython3

    for i in range(5):
        if i==3:
            print(i,"Broken")
            break
        else:
            print(i,"Unbroken")
    


.. parsed-literal::

    0 Unbroken
    1 Unbroken
    2 Unbroken
    3 Broken
    

فصل 8
صفحه
107

.. code:: ipython3

    #NestedIF2.py
    c= int(input("Please enter a number betwwen 0-360: "))
    while c<0 or c>360:
        c= int(input("Please enter a number betwwen 0-360: "))
    else:
        if c==0:
            print("Surface is flat")
        elif c < 45.:
            print("Aspet is north.")
        elif c < 135:
             print("Aspet is east.")
        elif c < 225:
             print("Aspet is south.")
        elif c<315:
            print ("Aspect is west")
        elif  c<=360:
             print("Aspet is north.")
             


.. parsed-literal::

    Please enter a number betwwen 0-360: 389
    Please enter a number betwwen 0-360: -1
    Please enter a number betwwen 0-360: 0
    Surface is flat
    

.. code:: ipython3

    colors = ['red', 'yellow', 'blue']
    >>> color_lines = []
    >>> for color in colors:
         color_lines.append('{0}\n'.format(color))
    

فصل 8
صفحه
108

.. code:: ipython3

    color_lines




.. parsed-literal::

    ['red\n', 'yellow\n', 'blue\n']



.. code:: ipython3

    color_lines = ['{0}\n'.format(color) for color in colors if 'l' in color]
    color_lines
    




.. parsed-literal::

    ['yellow\n', 'blue\n']



.. code:: ipython3

    colors = ['red', 'yellow', 'blue']
    clothes = ['hat', 'shirt', 'pants']
    colored_clothes = ['{0} {1}'.format(color, garment) for color in colors for garment in clothes]
    

.. code:: ipython3

    colored_clothes




.. parsed-literal::

    ['red hat',
     'red shirt',
     'red pants',
     'yellow hat',
     'yellow shirt',
     'yellow pants',
     'blue hat',
     'blue shirt',
     'blue pants']



.. code:: ipython3

    for i in range(0,10,2):
    	print(i)
    


.. parsed-literal::

    0
    2
    4
    6
    8
    

.. code:: ipython3

    for i in range(-1, -5, -1):
    	print(i)
    


.. parsed-literal::

    -1
    -2
    -3
    -4
    

.. code:: ipython3

    for i in range(70, 60):
        print(i)
    

فصل 8
صفحه
109

.. code:: ipython3

    for i in range(10, 60, 70):
        print(i)
    


.. parsed-literal::

    10
    

.. code:: ipython3

    words=["hello", "world","spam","egss"]
    for i in range(len(words)):
        print(words[i])
    


.. parsed-literal::

    hello
    world
    spam
    egss
    

.. code:: ipython3

    k1=[ str(i) for  i in range(12)]
    k1
    




.. parsed-literal::

    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']



.. code:: ipython3

    k2=[ (str(i),str(i+k) )for  i,k in zip(range(6),range(6))]
    k2

.. code:: ipython3

    squares=[i **2 for i in range(5)]
    print(squares)
    


.. parsed-literal::

    [0, 1, 4, 9, 16]
    

فصل 8
صفحه
110

.. code:: ipython3

    evenSq=[i **2 for i in range(5) if i%2==0]
    print(evenSq)
    


.. parsed-literal::

    [0, 4, 16]
    

even=[i*2 for i in range(10**100)]

.. code:: ipython3

    even=(i*2 for i in range(10**2))

.. code:: ipython3

    print(even)


.. parsed-literal::

    <generator object <genexpr> at 0x0000026BD63D6948>
    

.. code:: ipython3

    from itertools import count
    counter = count(10)
    nums= list(next(counter) for  i in range(11))
    nums




.. parsed-literal::

    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]



.. code:: ipython3

    nums2= list(next(counter) for i in range(11))
    nums2
    




.. parsed-literal::

    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]



.. code:: ipython3

    cn5=count(10, .5)
    n5= list(next(cn5) for i in range(11))
    n5
    




.. parsed-literal::

    [10, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0]



.. code:: ipython3

    from itertools import cycle
    c=cycle("abc")
    [next(c) for i in range(10)]
    




.. parsed-literal::

    ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a']



.. code:: ipython3

    from itertools import repeat
    repeat(2, 5)




.. parsed-literal::

    repeat(2, 5)



.. code:: ipython3

    list(repeat(2, 5))




.. parsed-literal::

    [2, 2, 2, 2, 2]



.. code:: ipython3

    from itertools import chain
    L1 = ['a', 'b', 'c']
    L2 = ['d', 'e', 'f']
    
    

فصل 8
صفحه
112

.. code:: ipython3

    chained = chain(L1, L2)
    

.. code:: ipython3

    chained




.. parsed-literal::

    <itertools.chain at 0x26bd6496dc8>



.. code:: ipython3

    list(chained)




.. parsed-literal::

    ['a', 'b', 'c', 'd', 'e', 'f']



.. code:: ipython3

    L1 = ['a', 'b', 'c']
    L2 = ['d', 'e', 'f']
    L1.extend(l2)
    L1
    




.. parsed-literal::

    ['a', 'b', 'c', 'd', 'e', 'f']



.. code:: ipython3

    from itertools import takewhile
    nums=range(10)
    print(list(takewhile(lambda x:x<=6,nums)))
    


.. parsed-literal::

    [0, 1, 2, 3, 4, 5, 6]
    

.. code:: ipython3

    from itertools import accumulate
    ac=accumulate([1, 2, 3,4,5])
    list(ac)
    




.. parsed-literal::

    [1, 3, 6, 10, 15]



.. code:: ipython3

    import operator
    ac=accumulate([1, 2, 3, 4,5], operator.add)
    list(ac)
    




.. parsed-literal::

    [1, 3, 6, 10, 15]



فصل 8
صفحه
113

.. code:: ipython3

    ac=accumulate([1, 2, 3, 4,5], operator.mul)
    list(ac)
    




.. parsed-literal::

    [1, 2, 6, 24, 120]



.. code:: ipython3

    ac=accumulate([45, 23, 4, 10,5], operator.sub)
    list(ac)
    




.. parsed-literal::

    [45, 22, 18, 8, 3]



.. code:: ipython3

    from itertools import groupby
    nums=[1,1,1,2,3,3,3,2,2,2,4,4]
    grp=groupby(nums)
    

.. code:: ipython3

    for g , v in grp:
        print(g, list(v))


.. parsed-literal::

    1 [1, 1, 1]
    2 [2]
    3 [3, 3, 3]
    2 [2, 2, 2]
    4 [4, 4]
    

.. code:: ipython3

    data = [{'month': 'Jan', 'T': 18},{'month': 'Feb', 'T': 20},{'month': 'Jan', 'T': 17},{'month': 'Feb', 'T': 21}, {'month': 'Jan', 'T': 16.5},{'month': 'Feb', 'T': 18}]
    from collections import defaultdict
    df=defaultdict(list)
    grp = groupby(data,key=lambda x: x['month'])
    for k , g in grp:
        df[k].append(list(g)[0]["T"])
    

.. code:: ipython3

    df["Jan"]




.. parsed-literal::

    [18, 17, 16.5]



فصل 8
صفحه
114

.. code:: ipython3

    from itertools import product
    letters=["A","B","C"]
    print(list(product(letters,range(2))))
    


.. parsed-literal::

    [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
    

.. code:: ipython3

    list(product(letters,letters))




.. parsed-literal::

    [('A', 'A'),
     ('A', 'B'),
     ('A', 'C'),
     ('B', 'A'),
     ('B', 'B'),
     ('B', 'C'),
     ('C', 'A'),
     ('C', 'B'),
     ('C', 'C')]



.. code:: ipython3

    from itertools import permutations
    print(list(permutations(letters,2)))
    


.. parsed-literal::

    [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    

.. code:: ipython3

    from itertools import  combinations
    list(combinations(letters,2))
    




.. parsed-literal::

    [('A', 'B'), ('A', 'C'), ('B', 'C')]



.. code:: ipython3

    from itertools import combinations_with_replacement
    cwr=combinations_with_replacement(letters,2)
    list(cwr)
    




.. parsed-literal::

    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]



فصل 8
صفحه
115

.. code:: ipython3

    theta_e = 0.486
    psi = 16.7
    K = 0.65
    S_e = 0.3
    t = 1
    dtheta = (1-S_e)*theta_e
    F_old = K*t
    epsilon = 1
    F = []
    import math
    while epsilon > 1e-4:
    	F_new = psi*dtheta * math.log(1+F_old/(psi*dtheta)) + K*t
    	epsilon = F_new - F_old
    	F_old = F_new
    	F.append(F_new)
    

.. code:: ipython3

    F[-1]




.. parsed-literal::

    3.1670531257440495



