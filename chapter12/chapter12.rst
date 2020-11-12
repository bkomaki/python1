فصل 12
صفحه 188

.. code:: ipython3

    class A(object):
        def show(self):
            return self.__class__.__name__

فصل 12
صفحه 189

.. code:: ipython3

    a=A()
    a.show()
    




.. parsed-literal::

    'A'



فصل 12
صفحه 189

.. code:: ipython3

    class point(object):
        def __init__(self,x,y):
            self.X = x
            self.Y = y
        def show(self):
            return self.X, self.Y
    
    

فصل 12
صفحه 190

.. code:: ipython3

    p1=point()


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-9ed6333782dc> in <module>
    ----> 1 p1=point()
    

    TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'


.. code:: ipython3

    p1=point(12,23)

.. code:: ipython3

    p1.X

.. code:: ipython3

    p1.Y

.. code:: ipython3

    p1.show()

.. code:: ipython3

    p1.X=13

.. code:: ipython3

    p1.X

.. code:: ipython3

    class point(object):
        def __init__(self,x,y):
            self.__X=x
            self.__Y=y
        def show(self):
            return self.__X, self.__Y

فصل 12
صفحه 191

.. code:: ipython3

    p1=point(25,33)
    p1.show()
    
    

.. code:: ipython3

    p1._point__X


فصل 12
صفحه 191

.. code:: ipython3

    class point(object):
    	def __init__(self,x,y):
    		self.X=x
    		self.Y=y
    	def __repr__(self):
    		return "point({0.X!r}, {0.Y!r})".format(self)
    	def __str__(self):
    		return "x={0.X!s},y= {0.Y!s}".format(self)
    

.. code:: ipython3

    p1=point(12,23)

.. code:: ipython3

    p1

.. code:: ipython3

    " p is {0!r}".format(p1)


فصل 12
صفحه 192

.. code:: ipython3

    print (p1)

.. code:: ipython3

    " p is {0}".format(p1)

.. code:: ipython3

    class point:
    	def __init__(self,x,y):
    		self.x=x
    		self.y=y
    	@property
    	def hypot(self):
    		return (self.x ** 2 + self.y ** 2) ** 0.5
    	def __str__(self):
    	     return '(x={0.x!s},y= {0.y!s}, distance={0.hypot!s})'.format(self)
    

.. code:: ipython3

    p1=point(12,34)

.. code:: ipython3

    p1

.. code:: ipython3

     print(p1)

.. code:: ipython3

    class point:
    	def __init__(self,x,y):
    		self.x=x
    		self.y=y
    	@property
    	def x(self):
    		return self.__x
    	@x.setter
    	def x(self, x):
    		if x<0:
    			self.__x=0
    		elif x>100:
    			self.__x=100
    		else:
    			self.__x=x
    	@property
    	def y(self):
    		return self.__y
    	@y.setter
    	def y(self,y):
    		if y<0:
    			self.__y=0
    		elif y>100:
    			self.__y=100
    		else:
    			self.__y=y
    
    

.. code:: ipython3

    p1=point(-120,10)

.. code:: ipython3

    p1.x
    

.. code:: ipython3

    p1.y


فصل 12
صفحه 194

.. code:: ipython3

    import math
    class circle:
    	def __init__(self, r):
    		self.r=r
    	@property
    	def area(self):
    		return math.pi *self.r**2
    	@property
    	def perimeter(self):
    		return 2*math.pi*self.r
    	@property
    	def r(self):
    		return self.__r
    	@r.setter
    	def r(self, value):
    		if not (isinstance(value, float) or   isinstance(value, int)) :
    			raise TypeError ("Expected a number")
    		else:
    			self.__r=value
    	def __str__(self):
    	     return 'r={0.r!s} p= {0.perimeter!s}, area={0.area!s}'.format(self)
    
    
    

.. code:: ipython3

    c=circle(23.2)

.. code:: ipython3

    c.r




.. parsed-literal::

    23.2



.. code:: ipython3

    c.area
    




.. parsed-literal::

    1690.9308298681703



.. code:: ipython3

    c.perimeter




.. parsed-literal::

    145.7698991265664



.. code:: ipython3

    print(c)


.. parsed-literal::

    r=23.2 p= 145.7698991265664, area=1690.9308298681703
    

.. code:: ipython3

    c=circle("a")


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-030b5b768569> in <module>
    ----> 1 c=circle("a")
    

    <ipython-input-5-cc61de86c747> in __init__(self, r)
          2 class circle:
          3         def __init__(self, r):
    ----> 4                 self.r=r
          5         @property
          6         def area(self):
    

    <ipython-input-5-cc61de86c747> in r(self, value)
         15         def r(self, value):
         16                 if not (isinstance(value, float) or   isinstance(value, int)) :
    ---> 17                         raise TypeError ("Expected a number")
         18                 else:
         19                         self.__r=value
    

    TypeError: Expected a number



فصل 12
صفحه 195

.. code:: ipython3

    class Queue:
    	def __init__(self, contents):
    		self._hidenlist=list(contents)
    	def push(self, value):
    		self._hidenlist.insert(0,value)
    	def pop(self):
    		self._hidenlist.pop(-1)
    	def __repr__(self):
    		return "Queue({0._hidenlist})".format(self)
    

.. code:: ipython3

    queue=Queue([1,2,3])
    queue
    

.. code:: ipython3

    queue.push(0)
    queue
    

.. code:: ipython3

    queue.pop()
    queue
    

.. code:: ipython3

    print (queue._hidenlist)


فصل 12
صفحه 197

.. code:: ipython3

    class point:
    	def __init__(self,x,y):
    		self.x=x
    		self.y=y
    	@property
    	def hypot(self):
    		return (self.x ** 2 + self.y ** 2) ** 0.5
    	def __str__(self):
    		form='x={0.x!s}y={0.y!s}length={0.hypot:6.3f}'
    		return form.format(self)
    	def __repr__(self):
    		form=' point: x={0.x!r}  y={0.y!r} length={0.hypot:6.3f}'
    		return form.format(self)
    
    	def __add__(self,other):
    		return point(self.x+other.x,self.y+other.y)
    	def __sub__(self,other):
    		return point(self.x-other.x,self.y-other.y)
    	def __call__(self, point):
    		return self.x+point.x, self.y+point.y
    

.. code:: ipython3

    p1=point(12,23)
    print(p1)
    

.. code:: ipython3

    p1

.. code:: ipython3

    p2=point(33,45)

.. code:: ipython3

    p12=p1+p2

.. code:: ipython3

    p12

.. code:: ipython3

    p2_1=p2-p1

.. code:: ipython3

    p2_1

.. code:: ipython3

    p1(p2)

فصل 12
صفحه 199

.. code:: ipython3

    class SpecialString:
    	def __init__(self,cont):
    		self.cont=cont
    	def __div__(self,other):
    		line ="-"*len(other.cont)
    		return "\n".join([self.cont,line,other.cont])
    	def __truediv__(self,other):
    		line ="="*len(other.cont)
    		return "\n".join([self.cont,line,other.cont])
    	
    

.. code:: ipython3

    spam=SpecialString("spam")
    hello=SpecialString("Hello World!")
    print(spam/hello)


.. parsed-literal::

    spam
    ============
    Hello World!
    

.. code:: ipython3

    print(spam/hello)


.. parsed-literal::

    spam
    ============
    Hello World!
    

.. code:: ipython3

    print(spam/hello)


.. parsed-literal::

    spam
    ============
    Hello World!
    

فصل 12
صفحه 200

.. code:: ipython3

    from __future__ import division 

.. code:: ipython3

    print(spam/hello)


.. parsed-literal::

    spam
    ============
    Hello World!
    

.. code:: ipython3

    class SpecialString:
    	def __init__(self,cont):
    		self.cont=cont
    	def __gt__(self,other):
    		for index in range(len(other.cont)+1):
    			result=other.cont[:index]+">"+self.cont
    			result+=">"+self.cont[index:]
    			print(result)
    

.. code:: ipython3

    spam=SpecialString("spam")
    egg=SpecialString("eggs")
    spam>egg
    


.. parsed-literal::

    >spam>spam
    e>spam>pam
    eg>spam>am
    egg>spam>m
    eggs>spam>
    

فصل 12
صفحه 201

.. code:: ipython3

    class Lister(object):
        def __init__(self, *args):
            self.items = tuple(args)
        def __iter__(self):
            return (i for i in self.items)
            
    s = Lister('a', 'b', 'c')
    for letter in s:
        print ( letter,)    
    


.. parsed-literal::

    a
    b
    c
    

.. code:: ipython3

    class Lister(object):
        def __init__(self, *args):
            self.items = tuple(args)
        def __iter__(self):
            for i in self.items:
                yield i
                  
    s= Lister('a', 'b', 'c')
    for letter in s:
         print (letter)
    


.. parsed-literal::

    a
    b
    c
    

فصل 12
صفحه 202

.. code:: ipython3

    import random
    class VagueList:
    	def __init__(self,cont):
    		self.cont=cont
    	def  __getitem__(self,index):
    		return self.cont[index+random.randint(-1,1)]
    	def __len__(self):
    		return random.randint(0, len(self.cont)*2)
    

.. code:: ipython3

    vague_list=VagueList(["A","B","C","D","E","F"])
    random.seed(1234567)
    len(vague_list)
    




.. parsed-literal::

    6



.. code:: ipython3

    len(vague_list)
    




.. parsed-literal::

    3



.. code:: ipython3

    vague_list[1]
    




.. parsed-literal::

    'A'



.. code:: ipython3

    vague_list[2]




.. parsed-literal::

    'D'




فصل 12
صفحه 203

.. code:: ipython3

    class Rectangle:
    	def __init__(self, width,height):
    		self.width=width
    		self.height=height
    	def area(self):
    		return self.width*self.height
    	@classmethod
    	def square(cls,side):
    		return cls(side,side)
    

.. code:: ipython3

    sq=Rectangle.square(3)
    sq.area()
    
    




.. parsed-literal::

    9



.. code:: ipython3

    sq.width
    




.. parsed-literal::

    3



.. code:: ipython3

    sq.height




.. parsed-literal::

    3



.. code:: ipython3

    class Rectangle:
    	def __init__(self, width,height):
    		self.width=width
    		self.height=height
    	@property
    	def area(self):
    		return self.width*self.height
    	@staticmethod
    	def square(side):
    		return side*side
    	def __str__(self):
    		return "{0. area}".format(self)
    

فصل 12
صفحه 204

.. code:: ipython3

    sq=Rectangle.square(23)
    print(sq)
    


.. parsed-literal::

    529
    

.. code:: ipython3

    print (Rectangle. square(12))
    


.. parsed-literal::

    144
    

.. code:: ipython3

    for i in [23,2,25]:
        print(Rectangle. square(i))


.. parsed-literal::

    529
    4
    625
    

فصل 12
صفحه 205

.. code:: ipython3

    class Shape (object):
    	"""Shape class: has method move"""
    	def  __init__ (self, x, y):
    		self.x = x
    		self.y = y
    	def move(self, deltaX, deltaY):
    		self.x += deltaX
    		self.y  += deltaY
    

.. code:: ipython3

    class Square(Shape):
        """Square Class:inherits from Shape"""
        def __init__(self, side=1, x=0, y=0):
            Shape.__init__(self, x, y)
            self._side = side
        @property
        def area(self):
            """Square area method: returns the area of the square."""
            return self._side * self._side
        def  __str__(self):
            form="Area is {0.area} at coordinate ({0.x}, {0.y})"
            return form.format(self)
    

.. code:: ipython3

    sq=Square(side=12)
    print(sq)
    


.. parsed-literal::

    Area is 144 at coordinate (0, 0)
    

.. code:: ipython3

    sq.move(23,12)

فصل 12
صفحه 206

.. code:: ipython3

    print(sq)


.. parsed-literal::

    Area is 144 at coordinate (23, 12)
    

.. code:: ipython3

    class Circle(Square):
    	"""Circle Class: inherits from Shape and has method area"""
    	_pi = 3.14159
    	def __init__(self, r=1, x=0, y=0):
    		Square.__init__(self, x, y)
    		self.radius = r
    	@property
    	def area(self):
    		"""Circle area method: returns the area of the circle."""
    		return self.radius * self.radius * self._pi
    

.. code:: ipython3

    cr=Circle(23)   
    print(cr)
    


.. parsed-literal::

    Area is 1661.90111 at coordinate (0, 0)
    

.. code:: ipython3

    cr.move(23,-2)
    print(cr)


.. parsed-literal::

    Area is 1661.90111 at coordinate (23, -2)
    

.. code:: ipython3

    >>> class Vehicle(object):
    	def __init__ (self, model, speed_max):
    		    self.model=model
    		    self.speed_max=speed_max
    		    self.speed=0
    	def accelerate(self, speed_difference):
    		self.speed+=abs(speed_difference)
    		self.speed=min (self.speed,self.speed_max)
    	def slow_down (self, speed_difference):
    		self.speed-=abs(speed_difference)
    		self.speed=max (self.speed,-5)
    


فصل 12
صفحه 207

.. code:: ipython3

    class Bus(Vehicle):
    	def slow_down(self, speed_difference):
    		super(Bus,self).slow_down(speed_difference)
    		self.speed = max(self.speed , 0)
    

.. code:: ipython3

    class Bike(Vehicle):
        def __init__(self, name, max_speed):
            max_speed = min(max_speed, 30)
            Vehicle.__init__(self,name, max_speed)
        def show_status(self):
            print ("The bike is " + self.model + ", its speed is "+ str(self.speed) + "km/h")
    

.. code:: ipython3

    class Bike(Vehicle):
    	def __init__(self,model, speed_max):
    		super(Bike, self).__init__( model, speed_max)
    		self.speed = min(speed_max, 30)
    	def show_status(self):
    		print ("The bike is " + self.model + ", its speed is "+ str(self.speed) + "km/h")
    


فصل 12
صفحه 208

.. code:: ipython3

    bike=Bike("Indian",25)
    print (bike.model)
    
    


.. parsed-literal::

    Indian
    

.. code:: ipython3

    bike.accelerate(30)
    bike. show_status()


.. parsed-literal::

    The bike is Indian, its speed is 25km/h
    

فصل 12
صفحه 208
تمرین عملی

.. code:: ipython3

    class Vec2D(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __add__(self, other):
            return Vec2D(self.x + other.x, self.y + other.y)
        def __sub__(self, other):
            return Vec2D(self.x - other.x, self.y - other.y)
        def __mul__(self, other):
            return self.x*other.x + self.y*other.y
        def __abs__(self):
            return math.sqrt(self.x**2 + self.y**2)
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y
        def __str__(self):
            return '(%g, %g)' % (self.x, self.y)
        def __ne__(self, other):
            return not self.__eq__(other)  # reuse __eq__
    

.. code:: ipython3

    v1=Vec2D(3,5)
    v2=Vec2D(4,6)
    v3=v1+v2

.. code:: ipython3

    v3.x,v3.y




.. parsed-literal::

    (7, 11)



