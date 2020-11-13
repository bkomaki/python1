فصل 5
صفحه 61


.. code:: ipython3

    k=[2,3,4,"a","b"]
    print (k)
    


.. parsed-literal::

    [2, 3, 4, 'a', 'b']
    

.. code:: ipython3

    for i in k:
    	print(i)
    


.. parsed-literal::

    2
    3
    4
    a
    b
    

.. code:: ipython3

    k[0]=10
    k
    




.. parsed-literal::

    [10, 3, 4, 'a', 'b']



فصل 5
صفحه 62


.. code:: ipython3

    p=[]
    print(p)


.. parsed-literal::

    []
    

.. code:: ipython3

    p = list()

.. code:: ipython3

    p1 = ['a', 'b', 'c']

.. code:: ipython3

    list('abcd')
    




.. parsed-literal::

    ['a', 'b', 'c', 'd']



.. code:: ipython3

    line = []
    line.append('b')
    line.append('c')
    print(line)
    


.. parsed-literal::

    ['b', 'c']
    

.. code:: ipython3

    line.insert(0, 'a')
    print(line)
    


.. parsed-literal::

    ['a', 'b', 'c']
    

.. code:: ipython3

    line.extend(['d','e'])

فصل 5
صفحه 63


.. code:: ipython3

    print(line)


.. parsed-literal::

    ['a', 'b', 'c', 'd', 'e']
    

.. code:: ipython3

    line + ['d','e']




.. parsed-literal::

    ['a', 'b', 'c', 'd', 'e', 'd', 'e']



.. code:: ipython3

    lis=list('abcd')
    lis
    
    




.. parsed-literal::

    ['a', 'b', 'c', 'd']



.. code:: ipython3

    lis.pop()




.. parsed-literal::

    'd'



.. code:: ipython3

    lis




.. parsed-literal::

    ['a', 'b', 'c']



.. code:: ipython3

    del lis[2]

.. code:: ipython3

    lis




.. parsed-literal::

    ['a', 'b']



.. code:: ipython3

    lis.remove("b")

.. code:: ipython3

    lis




.. parsed-literal::

    ['a']



.. code:: ipython3

    lis.clear()

.. code:: ipython3

    m=["a","b","c"]
    m*3
    




.. parsed-literal::

    ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']



.. code:: ipython3

    a=[2,3,4]

فصل 5
صفحه 64


.. code:: ipython3

    b=[5,6,7]
    a+b
    




.. parsed-literal::

    [2, 3, 4, 5, 6, 7]



.. code:: ipython3

    L = ['A', 'b', 'c', 'D']
    L.sort()
    L




.. parsed-literal::

    ['A', 'D', 'b', 'c']



.. code:: ipython3

    L.sort(key=str.lower)
    L




.. parsed-literal::

    ['A', 'b', 'c', 'D']



.. code:: ipython3

    L = sorted(L,key=str.lower)

.. code:: ipython3

    L




.. parsed-literal::

    ['A', 'b', 'c', 'D']



.. code:: ipython3

    L.sort(reverse=True)
    L




.. parsed-literal::

    ['c', 'b', 'D', 'A']



.. code:: ipython3

    for i in L:
    	    print(i,ord(i))
    


.. parsed-literal::

    c 99
    b 98
    D 68
    A 65
    

فصل 5
صفحه 65


.. code:: ipython3

    line = ['a', 'b', 'c']
    for letter in line:
        print(letter)
    


.. parsed-literal::

    a
    b
    c
    

.. code:: ipython3

    print(letter)


.. parsed-literal::

    c
    

.. code:: ipython3

    L = ['a', 'b', 'c']
    while len(L):
        print (L.pop())
    


.. parsed-literal::

    c
    b
    a
    

.. code:: ipython3

    L = ['a', 'b', 'c']
    len(L)
    




.. parsed-literal::

    3



.. code:: ipython3

    a=range(3)
    a




.. parsed-literal::

    range(0, 3)



.. code:: ipython3

    for i in range(len(L)):
    	print(i,L[i])
    


.. parsed-literal::

    0 a
    1 b
    2 c
    

فصل 5
صفحه 66


.. code:: ipython3

    p = list("abcdefgh")
    p
    




.. parsed-literal::

    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']



.. code:: ipython3

    p[3]




.. parsed-literal::

    'd'



.. code:: ipython3

    p[-3]




.. parsed-literal::

    'f'



.. code:: ipython3

    p[1:4]




.. parsed-literal::

    ['b', 'c', 'd']



فصل 5
صفحه 67


.. code:: ipython3

    p[1:-1]




.. parsed-literal::

    ['b', 'c', 'd', 'e', 'f', 'g']



.. code:: ipython3

    p[0:6:2]




.. parsed-literal::

    ['a', 'c', 'e']



.. code:: ipython3

    p[::2]




.. parsed-literal::

    ['a', 'c', 'e', 'g']



.. code:: ipython3

    print(p[2:8:2])


.. parsed-literal::

    ['c', 'e', 'g']
    

.. code:: ipython3

    print(p[8:2:-2])


.. parsed-literal::

    ['h', 'f', 'd']
    

.. code:: ipython3

    print(p[1::-1])


.. parsed-literal::

    ['b', 'a']
    

.. code:: ipython3

    p[::-1]




.. parsed-literal::

    ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']



.. code:: ipython3

    p.index('c')




.. parsed-literal::

    2



.. code:: ipython3

    p[p.index("f"):]     




.. parsed-literal::

    ['f', 'g', 'h']



.. code:: ipython3

    list1 = [1991,1994, 1997, 2000]

.. code:: ipython3

     print (list1[2])


.. parsed-literal::

    1997
    

.. code:: ipython3

    list1[2] = 2001
    print (list1[2])
    


.. parsed-literal::

    2001
    

.. code:: ipython3

    list1[1:3]=1995,1998

.. code:: ipython3

    list1[1:3]=1995,1998,2001     

.. code:: ipython3

    list1




.. parsed-literal::

    [1991, 1995, 1998, 2001, 2000]



.. code:: ipython3

    p1 = ['a', 'b', 'c']

.. code:: ipython3

    p2 =p1

.. code:: ipython3

    p2[0]="A"

.. code:: ipython3

    p1




.. parsed-literal::

    ['A', 'b', 'c']



.. code:: ipython3

    v=[1,2,3]     
    w=v.copy()     
    w     
    




.. parsed-literal::

    [1, 2, 3]



.. code:: ipython3

    w=v[:]
    w=list(v)
    

.. code:: ipython3

    chars = list('abcdef')
    chars
    'g' in chars




.. parsed-literal::

    False



.. code:: ipython3

    'c' in chars




.. parsed-literal::

    True



.. code:: ipython3

    q=[0,0,0,2,3,1]     
    q.count(0)
    




.. parsed-literal::

    3



.. code:: ipython3

    rain=[['Gorgan', 2, 4],
              ['Gonbad', 4.5, 0], 
              ['Marvaeh', 1.5, 1]]
    

.. code:: ipython3

    rain1=[2,4.5,1.5]
    rain2=[4,0,1]
    stations=["Gorgan", "Gonbad", "Marvaeh"]
    

فصل 5
صفحه 70


.. code:: ipython3

    data=[]
    for i in zip(stations,rain1,rain2):
        data.append(list(i))
    

.. code:: ipython3

    data




.. parsed-literal::

    [['Gorgan', 2, 4], ['Gonbad', 4.5, 0], ['Marvaeh', 1.5, 1]]



.. code:: ipython3

    data[1]




.. parsed-literal::

    ['Gonbad', 4.5, 0]



.. code:: ipython3

    nums=[2,3,4,1,5,8,9]
    s=sum(nums)
    print(s)
    


.. parsed-literal::

    32
    

.. code:: ipython3

    n=len(nums)

.. code:: ipython3

    s/n




.. parsed-literal::

    4.571428571428571



.. code:: ipython3

    print(max(nums))
    


.. parsed-literal::

    9
    

.. code:: ipython3

    print(min(nums))


.. parsed-literal::

    1
    

.. code:: ipython3

    chars=list("abcdef")
    max(chars)
    




.. parsed-literal::

    'f'



فصل 5
صفحه 71


.. code:: ipython3

    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list(enumerate(seasons))
    




.. parsed-literal::

    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]



.. code:: ipython3

    list(enumerate(seasons, start=1))




.. parsed-literal::

    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]



.. code:: ipython3

    name = ['Gorgan', 'Gonbad', 'Sari', 'Neka']
    Rain=[15, 10, 20,30]
    z=zip(name,Rain)
    z
    




.. parsed-literal::

    <zip at 0x2a4f3a909c8>



.. code:: ipython3

    list(z)




.. parsed-literal::

    [('Gorgan', 15), ('Gonbad', 10), ('Sari', 20), ('Neka', 30)]



.. code:: ipython3

    z=zip(name,Rain)
    [ i  for i in z]
    




.. parsed-literal::

    [('Gorgan', 15), ('Gonbad', 10), ('Sari', 20), ('Neka', 30)]



.. code:: ipython3

    [ i  for i in z]




.. parsed-literal::

    []



.. code:: ipython3

    range(12)




.. parsed-literal::

    range(0, 12)



.. code:: ipython3

    range(10,20,2)




.. parsed-literal::

    range(10, 20, 2)



.. code:: ipython3

    range(10,3,-2)




.. parsed-literal::

    range(10, 3, -2)



.. code:: ipython3

    range(12)




.. parsed-literal::

    range(0, 12)



.. code:: ipython3

    range(10,20,2)




.. parsed-literal::

    range(10, 20, 2)



.. code:: ipython3

    range(10,3,-2)




.. parsed-literal::

    range(10, 3, -2)




فصل 5
صفحه 72
تمرین عملی
1

