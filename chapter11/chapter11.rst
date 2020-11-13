فصل 11
صفحه
151

.. code:: ipython3

    def sayhi():
    	print ('Hello World')
    

.. code:: ipython3

    sayhi()


.. parsed-literal::

    Hello World
    

فصل 11
صفحه
152

.. code:: ipython3

    h= sayhi ()


.. parsed-literal::

    Hello World
    

.. code:: ipython3

    print(h)


.. parsed-literal::

    None
    

.. code:: ipython3

    def add(a,b):
    	return a+b

.. code:: ipython3

    c=add(2,4)
    print (c)
    


.. parsed-literal::

    6
    

.. code:: ipython3

    add(2)


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-7-c846fc9fb86e> in <module>
    ----> 1 add(2)
    

    TypeError: add() missing 1 required positional argument: 'b'


.. code:: ipython3

    t=add(b=3,a=4)
    t
    




.. parsed-literal::

    7



فصل 11
صفحه
153

.. code:: ipython3

    def wein(w, c=2897):
    	return c/w
    

.. code:: ipython3

    wein(300)




.. parsed-literal::

    9.656666666666666



فصل 11
صفحه
154

.. code:: ipython3

    def size(p,d=0.05, N=None,z=1.96):
    	q=1-p
    	if N:
    		return (N*z**2*p*q)/(N*d**2+z**2*p*q)
    	else:
    		return (z**2*p*q)/(d**2)
    	
    size(0.5)
    384.1599999999999
    




.. parsed-literal::

    384.1599999999999



.. code:: ipython3

    size(0.5,N=2000)




.. parsed-literal::

    322.26025098986634



.. code:: ipython3

    size(0.5,.1,1000)




.. parsed-literal::

    87.62453925039229



.. code:: ipython3

    size()


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-14-69a73d314862> in <module>
    ----> 1 size()
    

    TypeError: size() missing 1 required positional argument: 'p'


فصل 11
صفحه
155

.. code:: ipython3

    def slope(point1,point2):
        x1,y1=point1
        x2,y2=point2
        dY=y2-y1
        dX=x2-x1
        slope=dY/dX
        dist=(dY**2+dX**2)**0.5
        from math import atan, degrees
        angle=atan(slope)
        degree=degrees(angle)
        return slope*100,dist, degree
    

فصل 11
صفحه
156

.. code:: ipython3

    p1=2,5
    p2=4,9
    slop, dist, deg=slope(p1,p2)
    print( slop, dist, deg)
    


.. parsed-literal::

    200.0 4.47213595499958 63.43494882292201
    

.. code:: ipython3

    def avg(first, *rest):
        return (first + sum(rest)) / (1. + len(rest))
    

.. code:: ipython3

    avg(1,2,3,4,5)




.. parsed-literal::

    3.0



.. code:: ipython3

    def funcVar(*args, **kwargs):
    	print ('args:', args)
    	print ('kwargs:', kwargs)
    funcVar ('simple')
    


.. parsed-literal::

    args: ('simple',)
    kwargs: {}
    

.. code:: ipython3

    funcVar(type='Complex')


.. parsed-literal::

    args: ()
    kwargs: {'type': 'Complex'}
    

فصل 11
صفحه
157

.. code:: ipython3

    def mixFunc (a, b, c=None, *args, **kwargs):
    	print ('(a, b, c):', (a, b, c))
    	print ('args:', args)
    	print ('kwargs:', kwargs)
    mixFunc (1, 2, 3, 4, 5, d=10, e=20)
    


.. parsed-literal::

    (a, b, c): (1, 2, 3)
    args: (4, 5)
    kwargs: {'d': 10, 'e': 20}
    

.. code:: ipython3

    def printer(a, b, c=0, d=None):
     	print ('a: {0}, b: {1}, c: {2}, d: {3}'.format(a, b, c, d))
    printer(2, 3, 4, 5)
    


.. parsed-literal::

    a: 2, b: 3, c: 4, d: 5
    

فصل 11
صفحه
158

.. code:: ipython3

    ordered_args = (5, 6)
    keyword_args = {'c': 7, 'd': 8}
    printer(*ordered_args, **keyword_args)
    


.. parsed-literal::

    a: 5, b: 6, c: 7, d: 8
    

.. code:: ipython3

    def area(*args,**kwargs):
    	if len(args)==1:
    		r=args[0]
    		print("shape is circle")
    		A=kwargs["pi"]*r**2
    		return A
    	elif len(args)==2:
    		a,b=args
    		print("shape is square")
    		return a*b
    	elif len(args)==3:
    		a,b,c=args
    		print("shape is triangular")
    		s=sum(args)/2
    		A=(s*(s-a)*(s-b)*(s-c))**0.5
    		return A
    

.. code:: ipython3

    area(11,3)
    
    


.. parsed-literal::

    shape is square
    shape is triangular
    



.. parsed-literal::

    61.48170459575759



.. code:: ipython3

    area(11,pi=3.1)


.. parsed-literal::

    shape is circle
    



.. parsed-literal::

    375.1



.. code:: ipython3

    area(11,12,13)


.. parsed-literal::

    shape is triangular
    



.. parsed-literal::

    61.48170459575759



فصل 11
صفحه
159

.. code:: ipython3

    def mean(x):
    	return sum(x)/len(x)
    

.. code:: ipython3

    def std(x,dfd=1):
    	m=mean(x)
    	n=len(x)-dfd
    	var= [(i-m)**2/n for i in x]
    	return sum(var)**.5
    

.. code:: ipython3

    rain=[13,5, 7, 0, 16]
    m=mean(rain)
    s=std(rain)
    

.. code:: ipython3

    print('f mean: {m} ,std: {s}' )
    


.. parsed-literal::

      f mean: {m} ,std: {s} 
    

.. code:: ipython3

    import statistics
    statistics.mean(rain)
    statistics.stdev(rain)
    




.. parsed-literal::

    6.3796551630946325



.. code:: ipython3

    def add_items(new_items, base_items=[]):
    	for item in new_items:
    		base_items.append(item)
    	return base_items
    add_items((1, 2, 3))
    




.. parsed-literal::

    [1, 2, 3]



.. code:: ipython3

    add_items((4,6,7))




.. parsed-literal::

    [1, 2, 3, 4, 6, 7]



.. code:: ipython3

    def add_items(new_items, base_items=None):
    	if base_items is None:
    		base_items = []
    	for item in new_items:
    		base_items.append(item)
    	return base_items
    add_items((1, 2, 3))
    




.. parsed-literal::

    [1, 2, 3]



.. code:: ipython3

    add_items((4,6,7))




.. parsed-literal::

    [4, 6, 7]



فصل 11
صفحه
161

.. code:: ipython3

    def add2(x):
    	return x+2
    add2(5)

.. code:: ipython3

    addTwo=lambda x:x+2
    
    addTwo(5)




.. parsed-literal::

    7



.. code:: ipython3

    def deep_scope():
    	if True:
    		if True:
    			if True:
    				x = 5
    	return x
    deep_scope()
    




.. parsed-literal::

    5



فصل 11
صفحه
162

.. code:: ipython3

    def oops(letter):
    	if letter == 'a':
    		out = 'A'
    	return out
    oops('a')
    




.. parsed-literal::

    'A'



.. code:: ipython3

    def function_local(a):
    	print (a)
    function_local(50)
    


.. parsed-literal::

    50
    

.. code:: ipython3

    print(a)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-48-bca0e2660b9f> in <module>
    ----> 1 print(a)
    

    NameError: name 'a' is not defined


.. code:: ipython3

    def function_local(a):
    	global b
    	b=a
    
    function_local(12)
    

.. code:: ipython3

    def outside():
    	a=10
    	def inside():
    		a=2
    		print("Inside a ->", a)
    	inside()
    	print("outside a->", a)
    outside()


.. parsed-literal::

    Inside a -> 2
    outside a-> 10
    

.. code:: ipython3

    def outside():
           a = 10
           def inside():
                  nonlocal a
                  a = 20
                  print("The value of a in inside() function - ", a)
           inside()
           print("The value of a in outside() function -  ", a)
    outside()
    


.. parsed-literal::

    The value of a in inside() function -  20
    The value of a in outside() function -   20
    

.. code:: ipython3

    # -*- coding: cp1256 -*-

فصل 11
صفحه
164

.. code:: ipython3

    # This is a comment

.. code:: ipython3

    def f(x):
    	"""This is a function that adds 2 to each number
                          for example:
                           y=f(12)
                           you will get
                           14 """
    	x=x+2
    	return x
    

.. code:: ipython3

    print(f.__doc__)


.. parsed-literal::

    This is a function that adds 2 to each number
                          for example:
                           y=f(12)
                           you will get
                           14 
    

.. code:: ipython3

    def a_object(x):
    	return x
    a_object(a_object)
    




.. parsed-literal::

    <function __main__.a_object(x)>



فصل 11
صفحه
166

.. code:: ipython3

    def second_element(t):
          return t[1]
    zepp = [('Guitar', 'Jimmy'), ('Vocals', 'Robert'), ('Bass', 'John Paul'), ('Drums', 'John')]
    sorted(zepp)




.. parsed-literal::

    [('Bass', 'John Paul'),
     ('Drums', 'John'),
     ('Guitar', 'Jimmy'),
     ('Vocals', 'Robert')]



.. code:: ipython3

    sorted(zepp, key=second_element)




.. parsed-literal::

    [('Guitar', 'Jimmy'),
     ('Drums', 'John'),
     ('Bass', 'John Paul'),
     ('Vocals', 'Robert')]



.. code:: ipython3

     func1=lambda x,y:x+y

.. code:: ipython3

    def call_func(f, *args):
        return f(*args)
    

.. code:: ipython3

    call_func(func1,2,4)




.. parsed-literal::

    6



.. code:: ipython3

    import operator
    call_func( operator.add,2,4)
    




.. parsed-literal::

    6



فصل 11
صفحه
167

.. code:: ipython3

    def celsius(T):
        return (float(5)/9)*(T-32)
    

.. code:: ipython3

    temp = (25.5, 34, 46.5,46)

.. code:: ipython3

    f=list(map(celsius,temp))
    print (f)
    


.. parsed-literal::

    [-3.611111111111111, 1.1111111111111112, 8.055555555555555, 7.777777777777779]
    

.. code:: ipython3

    a = [1,2,3,4]
    b = [17,12,11,10]
    c = [-1,-4,5,9]

.. code:: ipython3

    list(map(lambda x,y:x+y, a,b))




.. parsed-literal::

    [18, 14, 14, 14]



.. code:: ipython3

    list(map(lambda x,y,z:x+y+z, a,b,c))




.. parsed-literal::

    [17, 10, 19, 23]



.. code:: ipython3

    list(map(lambda x,y,z:x+y-z, a,b,c))




.. parsed-literal::

    [19, 18, 9, 5]



.. code:: ipython3

    nums1=[3,4,2,4]
    nums2=[5,2,5,1]
    product=map(lambda x,y:x*y, nums1,nums1)
    sumproduct=sum(product)
    print(sumproduct)


.. parsed-literal::

    45
    

فصل 11
صفحه
168

.. code:: ipython3

    def powers(x):
    	return x**2, x**3,x**4
    y=[1.0,2.0,3.0,4.0]
    list(map(powers,y))
    




.. parsed-literal::

    [(1.0, 1.0, 1.0), (4.0, 8.0, 16.0), (9.0, 27.0, 81.0), (16.0, 64.0, 256.0)]



.. code:: ipython3

    def powers(x,y):
    	return x**2, x*y, y**2
    

.. code:: ipython3

    x = [10, 20]
    y = [11, 22, 33, 44]
    list(map(powers, x, y))
    




.. parsed-literal::

    [(100, 110, 121), (400, 440, 484)]



.. code:: ipython3

    x=range(35)

.. code:: ipython3

    result = filter(lambda x: x % 2, x)

.. code:: ipython3

     list(result)




.. parsed-literal::

    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]



.. code:: ipython3

    result = filter(lambda x: x % 2==0, x)

.. code:: ipython3

     list(result)




.. parsed-literal::

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]



فصل 11
صفحه
169

.. code:: ipython3

    nums=[23,26,32,45,56]
    result=list(filter(lambda x:x%2==0,nums))
    print (result)
    


.. parsed-literal::

    [26, 32, 56]
    

.. code:: ipython3

    x = [10, 20, 30]
    y = [11, 22, 33, 44]
    list(zip(x, y))
    




.. parsed-literal::

    [(10, 11), (20, 22), (30, 33)]



.. code:: ipython3

    from functools import reduce
    reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
    




.. parsed-literal::

    15



فصل 11
صفحه
170

.. code:: ipython3

    Add= lambda x, y: x+y
    reduce(Add, range(1,101))
    




.. parsed-literal::

    5050



.. code:: ipython3

    from operator import mul
    from functools import reduce
    def multiply(*args): 
                    return reduce(mul, args)
    multiply(2,4,5)
    




.. parsed-literal::

    40



.. code:: ipython3

    def factorial(x):
    		if 0<=x<1:
    			return 1
    		return x*factorial(x-1)
    

فصل 11
صفحه
171

.. code:: ipython3

    print(factorial(5))
    
    


.. parsed-literal::

    120
    

.. code:: ipython3

    factorial(0)




.. parsed-literal::

    1



.. code:: ipython3

    def sum_add(x):
    	if x==1:
    		return 1
    	else:
    		return x+ sum_add(x-1)
    

.. code:: ipython3

    sum_add(10)




.. parsed-literal::

    55



.. code:: ipython3

    def fib(x):
    	if x==0:
    		return 0
    	if x==1:
    		return 1
    	else:
    		return fib(x-1)+fib(x-2)
    fib(10)
    




.. parsed-literal::

    55



فصل 11
صفحه
172

.. code:: ipython3

    def factorial(x):
    	return x*factorial(x-1)
    

.. code:: ipython3

    #factorial(6)

.. code:: ipython3

    def factorial(x):
    	if x==1:
    		return 1
    	return x*factorial(x-1)
    
    factorial(6)
    




.. parsed-literal::

    720



فصل 11
صفحه
173

.. code:: ipython3

    from cmath import sin, sqrt, pi, exp
    p = [676.5203681218851
        ,-1259.1392167224028
        ,771.32342877765313
        ,-176.61502916214059
        ,12.507343278686905
        ,-0.13857109526572012
        ,9.9843695780195716e-6
        ,1.5056327351493116e-7]
    
    EPSILON = 1e-07  
    def drop_imag(z):
        if abs(z.imag) <= EPSILON:
            z = z.real
        return z
        
    def gamma(z):
        z = complex(z)
        if z.real < 0.5:
            y = pi / (sin(pi*z) * gamma(1-z)) ### Reflection formula 
        else:
            z -= 1
            x = 0.99999999999980993
            for (i, pval) in enumerate(p):
                x += pval / (z+i+1)
            t = z + len(p) - 0.5
            y = sqrt(2*pi) * t**(z+0.5) * exp(-t) * x
        return drop_imag(y)
    

.. code:: ipython3

    def is_even(x):
    	if x==0:
    		return True
    	else:
    		return is_odd(x-1)
    def is_odd(x):
    	return  not is_even(x)
    is_even(4)
    




.. parsed-literal::

    True



.. code:: ipython3

    is_odd(5)




.. parsed-literal::

    True



فصل 11
صفحه
174

.. code:: ipython3

    def findSum(arr, N): 
        if len(arr)== 1: 
            return arr[0] 
        else: 
            return arr[0]+findSum(arr[1:], N) 
    
    a=[1,2,4,6]
    n=len(a)
    findSum(a,n)
    




.. parsed-literal::

    13



.. code:: ipython3

    def countdown():
    	i=5
    	while i>0:
    		yield i
    		i-=1
    for i in countdown():
    	print(i)
    


.. parsed-literal::

    5
    4
    3
    2
    1
    

.. code:: ipython3

    def numbers(x):
    	for i in range(x):
    		yield i
    print(list(numbers(16)))
    


.. parsed-literal::

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    

فصل 11
صفحه
175

.. code:: ipython3

    def evens(x):
    	for i in range(x):
    		if i%2==0:
    			yield i
    print(list(evens(16)))
    


.. parsed-literal::

    [0, 2, 4, 6, 8, 10, 12, 14]
    

.. code:: ipython3

    def gen1():
    	while True:
    		yield 8
    

.. code:: ipython3

    #for i in gen1():
    #	print(i)
    

فصل 11
صفحه
176

.. code:: ipython3

    def pascal():
    	row=[1]
    	while True:
    		yield row
    		row=[i+j for i,j in zip(row+[0],[0]+row)]    
    can=pascal()
    
    kick=next
    k=[kick(can) for i in range(5)]	     
    for i in k:
        print(i)
    


.. parsed-literal::

    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    

.. code:: ipython3

    can=pascal()
    k=[next(can) for i in range(24)]
    k[23][20]
    




.. parsed-literal::

    1771



.. code:: ipython3

    from collections import deque
    >>> import itertools
    >>> def moving_average(iterable, n=3):
    	"""moving_average([40, 30, 50, 46, 39, 44])-->40.0 42.0 45.0 43.0"""
    	it = iter(iterable)
    	d = deque(itertools.islice(it, n-1))
    	d.appendleft(0)
    	s = sum(d)
    	for elem in it:
    		s += elem - d.popleft()
    		d.append(elem)
    		yield s / float(n)
    list(moving_average([40, 30, 50, 46, 39, 44]))
    
    




.. parsed-literal::

    [40.0, 42.0, 45.0, 43.0]



.. code:: ipython3

    list(moving_average([40, 30, 50, 46, 39, 44], n=4))




.. parsed-literal::

    [41.5, 41.25, 44.75]



فصل 11
صفحه
177
تمرین عملی
1

