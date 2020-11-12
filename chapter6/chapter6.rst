فصل 6
صفحه 73

.. code:: ipython3

    S=set()

.. code:: ipython3

    names={"ahmad", "homa", "hassan"}

.. code:: ipython3

    print(names)


.. parsed-literal::

    {'ahmad', 'homa', 'hassan'}
    

.. code:: ipython3

    set2=set(['jack', 'sjoerd', "ferri","jef"])

فصل 6
صفحه 74

.. code:: ipython3

    nums={1,2,3,4}
    4  in nums
    




.. parsed-literal::

    True



.. code:: ipython3

    set2={1,2,1,1,3,4,5,6,3}
    print(set2)


.. parsed-literal::

    {1, 2, 3, 4, 5, 6}
    

.. code:: ipython3

    set2.add(7)
    print(set2)


.. parsed-literal::

    {1, 2, 3, 4, 5, 6, 7}
    

.. code:: ipython3

    set2.remove(4)
    print(set2)


.. parsed-literal::

    {1, 2, 3, 5, 6, 7}
    

.. code:: ipython3

    set2.pop()
    




.. parsed-literal::

    1



.. code:: ipython3

    set2.pop()




.. parsed-literal::

    2



.. code:: ipython3

    print(set2)


.. parsed-literal::

    {3, 5, 6, 7}
    

فصل 6
صفحه 75

.. code:: ipython3

    first={1,2,5,7}
    second={3,5,4,7,8}
    print(first|second)
    
    


.. parsed-literal::

    {1, 2, 3, 4, 5, 7, 8}
    

.. code:: ipython3

    print(first&second)


.. parsed-literal::

    {5, 7}
    

.. code:: ipython3

    print(first-second)


.. parsed-literal::

    {1, 2}
    

.. code:: ipython3

    print(first^second)


.. parsed-literal::

    {1, 2, 3, 4, 8}
    

فصل 6
صفحه 75

.. code:: ipython3

    ages={"ahmad":24,"hassan":36,"ali":63}

.. code:: ipython3

    a = dict(one=1, two=2, three=3)

.. code:: ipython3

    b = {'one': 1, 'two': 2, 'three': 3}

.. code:: ipython3

    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

.. code:: ipython3

    d = dict([('two', 2), ('one', 1), ('three', 3)])

فصل 6
صفحه 76

.. code:: ipython3

    e = dict({'three': 3, 'one': 1, 'two': 2})

.. code:: ipython3

    a == b == c == d == e




.. parsed-literal::

    True



.. code:: ipython3

    ages["ahmad"]




.. parsed-literal::

    24



.. code:: ipython3

    colors={"red":[0,0,255],
            "green":[0,255,0],
            "blue":[255,0,0]}
    

.. code:: ipython3

    colors["brown"]


::


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-34-03e154fe3165> in <module>
    ----> 1 colors["brown"]
    

    KeyError: 'brown'


.. code:: ipython3

    sums={(2,3):5,(3,3):6}

.. code:: ipython3

    k={[2,34]:"ali",[3,45]:"asad"}


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-36-3a58c015afe4> in <module>
    ----> 1 k={[2,34]:"ali",[3,45]:"asad"}
    

    TypeError: unhashable type: 'list'


فصل 6
صفحه 77

.. code:: ipython3

    colors={"blue":3,"red":5}
    colors.update(red=1, blue=2)
    

.. code:: ipython3

    colors.update(green=1)

.. code:: ipython3

    squares={1:1, 2:4, 3:"error", 4:16, 5:25}
    print(squares)
    


.. parsed-literal::

    {1: 1, 2: 4, 3: 'error', 4: 16, 5: 25}
    

.. code:: ipython3

    squares[3]=9
    print(squares)


.. parsed-literal::

    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    

.. code:: ipython3

    squares[6]=36

.. code:: ipython3

    squares.update({7:49})

.. code:: ipython3

    del squares[2]

.. code:: ipython3

    squares




.. parsed-literal::

    {1: 1, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}



.. code:: ipython3

    print (3 in squares)


.. parsed-literal::

    True
    

.. code:: ipython3

    print (5 not in nums)


.. parsed-literal::

    True
    

.. code:: ipython3

    print (5 in squares)


.. parsed-literal::

    True
    

فصل 6
صفحه 78

.. code:: ipython3

    print ("one" in nums)


.. parsed-literal::

    False
    

.. code:: ipython3

    for key in squares:
    	print(key, squares[key])
    


.. parsed-literal::

    1 1
    3 9
    4 16
    5 25
    6 36
    7 49
    

.. code:: ipython3

    list(squares)




.. parsed-literal::

    [1, 3, 4, 5, 6, 7]



.. code:: ipython3

    squares.keys()




.. parsed-literal::

    dict_keys([1, 3, 4, 5, 6, 7])



.. code:: ipython3

    squares.values()




.. parsed-literal::

    dict_values([1, 9, 16, 25, 36, 49])



.. code:: ipython3

    squares.get(3)
    




.. parsed-literal::

    9



.. code:: ipython3

    squares.get(8, "not in dictinary")




.. parsed-literal::

    'not in dictinary'



.. code:: ipython3

    day1=[2, 4.5, 1.5]
    day2=[4, 0, 1]

فصل 6
صفحه 79

.. code:: ipython3

    stations=["Gorgan", "Gonbad", "Marvaeh"]

.. code:: ipython3

    rain={}

.. code:: ipython3

    for name in stations:
        i=stations.index(name)
        rain[name]= day1 [i], day2[i]
    

.. code:: ipython3

    rain




.. parsed-literal::

    {'Gorgan': (2, 4), 'Gonbad': (4.5, 0), 'Marvaeh': (1.5, 1)}



.. code:: ipython3

    rain['Gonbad']




.. parsed-literal::

    (4.5, 0)



.. code:: ipython3

    T=[12, 13, 13, 13, 13, 14, 14, 11, 13, 12, 13, 14,15, 15, 13,13]

.. code:: ipython3

    hist={}
    for x in T:
        hist[x]=hist.get(x,0)+1
    

.. code:: ipython3

    hist




.. parsed-literal::

    {12: 2, 13: 8, 14: 3, 11: 1, 15: 2}



.. code:: ipython3

    for val, freq in hist.items():
                 print(val, freq)
    


.. parsed-literal::

    12 2
    13 8
    14 3
    11 1
    15 2
    

.. code:: ipython3

    from collections import Counter
    Counter(T)
    




.. parsed-literal::

    Counter({12: 2, 13: 8, 14: 3, 11: 1, 15: 2})



.. code:: ipython3

    d={}
    total=sum(hist.values())
    for x, freq in hist.items():
        d[x]=freq/total
    

.. code:: ipython3

    print(d)


.. parsed-literal::

    {12: 0.125, 13: 0.5, 14: 0.1875, 11: 0.0625, 15: 0.125}
    

.. code:: ipython3

    sum(d.values())




.. parsed-literal::

    1.0



.. code:: ipython3

    hist.clear()
    hist
    




.. parsed-literal::

    {}



.. code:: ipython3

    from collections import defaultdict
    n=defaultdict(int)
    s=list("asasadadsa")
    s
    




.. parsed-literal::

    ['a', 's', 'a', 's', 'a', 'd', 'a', 'd', 's', 'a']



.. code:: ipython3

    for key in s:
        n[key]+=1

فصل 6
صفحه 81

.. code:: ipython3

    n




.. parsed-literal::

    defaultdict(int, {'a': 5, 's': 3, 'd': 2})



.. code:: ipython3

    rain=[["Jan",12],["Feb",15],["Mar",16],
          ["Jan",13.5],["Feb",14],["Mar",17.5],
          ["Jan",11],["Feb",13],["Mar",15]]
    month=defaultdict(list)
    for item in rain:
        k,v=item
        month[k].append(v)
    

.. code:: ipython3

    month["Jan"]




.. parsed-literal::

    [12, 13.5, 11]



.. code:: ipython3

    month




.. parsed-literal::

    defaultdict(list,
                {'Jan': [12, 13.5, 11],
                 'Feb': [15, 14, 13],
                 'Mar': [16, 17.5, 15]})



.. code:: ipython3

    from collections import OrderedDict 
    od = OrderedDict()
    

.. code:: ipython3

    od['a'] = 1;od['b'] = 2;od['c'] = 3;od['d'] = 4

.. code:: ipython3

    od




.. parsed-literal::

    OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])



.. code:: ipython3

    from collections import Counter
    lis=[1,2,3,1,1,1,3,2,2,2,4,2,1,1,4]
    cnr=Counter(lis)
    cnr
    




.. parsed-literal::

    Counter({1: 6, 2: 5, 3: 2, 4: 2})



فصل 6
صفحه 82

.. code:: ipython3

    cnr.most_common(2)




.. parsed-literal::

    [(1, 6), (2, 5)]



.. code:: ipython3

    cnr.most_common(1)




.. parsed-literal::

    [(1, 6)]



.. code:: ipython3

    cnr[1]




.. parsed-literal::

    6



.. code:: ipython3

    c = Counter(a=3, b=1)
    d = Counter(a=1, b=2,c=3)
    c+d
    




.. parsed-literal::

    Counter({'a': 4, 'b': 3, 'c': 3})



.. code:: ipython3

    c-d




.. parsed-literal::

    Counter({'a': 2})



.. code:: ipython3

    c&d




.. parsed-literal::

    Counter({'a': 1, 'b': 1})



.. code:: ipython3

    c|d




.. parsed-literal::

    Counter({'a': 3, 'b': 2, 'c': 3})



.. code:: ipython3

    from collections import deque
    d=deque("cde")
    d
    




.. parsed-literal::

    deque(['c', 'd', 'e'])



فصل 6
صفحه 83

.. code:: ipython3

    d.appendleft("b")
    d
    




.. parsed-literal::

    deque(['b', 'c', 'd', 'e'])



.. code:: ipython3

    d.extendleft("af")
    d
    




.. parsed-literal::

    deque(['f', 'a', 'b', 'c', 'd', 'e'])



.. code:: ipython3

    d.rotate(1)
    d




.. parsed-literal::

    deque(['e', 'f', 'a', 'b', 'c', 'd'])



.. code:: ipython3

    d.rotate(-2)
    d




.. parsed-literal::

    deque(['a', 'b', 'c', 'd', 'e', 'f'])



.. code:: ipython3

    d.popleft()




.. parsed-literal::

    'a'



.. code:: ipython3

    d.popleft()




.. parsed-literal::

    'b'



.. code:: ipython3

    d




.. parsed-literal::

    deque(['c', 'd', 'e', 'f'])



.. code:: ipython3

    list(reversed(d))




.. parsed-literal::

    ['f', 'e', 'd', 'c']



فصل 6
صفحه 83
تمرین عملی
1

.. code:: ipython3

     st={}

فصل 6
صفحه 83
تمرین عملی
2

.. code:: ipython3

    st=set((1,2,3,4))
    st.discard(4)
    st
    




.. parsed-literal::

    {1, 2, 3}



فصل 6
صفحه 83
تمرین عملی
3

.. code:: ipython3

    st1={"a", "b"}
    st2={"d","a", "b","c"}
    st1<=st2
    
    




.. parsed-literal::

    True



.. code:: ipython3

    st1.issubset(st2)




.. parsed-literal::

    True



فصل 6
صفحه 83
تمرین عملی
4

.. code:: ipython3

    st2.issuperset(st1)




.. parsed-literal::

    True



فصل 6
صفحه 83
تمرین عملی
5

.. code:: ipython3

    d = {"A":10, "B":20}
    d.update({"C":30})
    

فصل 6
صفحه 83
تمرین عملی
6

.. code:: ipython3

    d1 = {"A":10, "B":20}
    d2={"C":30,"D":40}
    d3={}
    for i in d1,d2:
        d3.update(i)
    d3
    




.. parsed-literal::

    {'A': 10, 'B': 20, 'C': 30, 'D': 40}



فصل 6
صفحه 83
تمرین عملی
7

.. code:: ipython3

    color={"r":20,"b":30,"d":5}
    for key in color:
        print(color[key])
    


.. parsed-literal::

    20
    30
    5
    

