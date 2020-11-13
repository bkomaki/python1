فصل دهم
صفحه
138

.. code:: ipython3

    colors = ['red', 'yellow', 'blue']
    f=open("D:/colors.txt", "w")
    f.write("\n".join(colors))
    




.. parsed-literal::

    15



.. code:: ipython3

    f.close()

.. code:: ipython3

    colors = ['red\n', 'yellow\n', 'blue\n']
    f = open('D:/colors.txt', 'w')
    f.writelines(colors)
    

.. code:: ipython3

    f.close()

فصل دهم
صفحه
139

.. code:: ipython3

    import io
    f=io.open("D:/colors.txt", "w")
    f.writelines(colors)
    f.close()
    

.. code:: ipython3

    f = open('D:/colors.txt')
    f.readline()




.. parsed-literal::

    'red\n'



.. code:: ipython3

    f.readline()




.. parsed-literal::

    'yellow\n'



.. code:: ipython3

    f.readline()




.. parsed-literal::

    'blue\n'



.. code:: ipython3

    f.readline()




.. parsed-literal::

    ''



.. code:: ipython3

    f.readline()




.. parsed-literal::

    ''



.. code:: ipython3

    f.readline()




.. parsed-literal::

    ''



.. code:: ipython3

    f.readline()




.. parsed-literal::

    ''



.. code:: ipython3

    f.close()

.. code:: ipython3

    f = open('D:/colors.txt')
    print(f.readline(),end="")
    


.. parsed-literal::

    red
    

.. code:: ipython3

    f = open('D:/colors.txt')
    f.readlines()
    




.. parsed-literal::

    ['red\n', 'yellow\n', 'blue\n']



.. code:: ipython3

    f = open('D:/colors.txt')
    for line in f:
        print (line,)
    


.. parsed-literal::

    red
    
    yellow
    
    blue
    
    

فصل دهم
صفحه
140

.. code:: ipython3

    f.close()

.. code:: ipython3

    f = open('D:/colors.txt')
    try:
        lines = f.readlines()
    finally:
        f.close()
    

.. code:: ipython3

    lines




.. parsed-literal::

    ['red\n', 'yellow\n', 'blue\n']



.. code:: ipython3

    f.seek(0)


::


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-20-16754355c5bd> in <module>
    ----> 1 f.seek(0)
    

    ValueError: I/O operation on closed file.


.. code:: ipython3

    f = open('D:/colors.txt')
    try:
        f.writelines('magenta\n')
    finally:
        f.close()
    


::


    ---------------------------------------------------------------------------

    UnsupportedOperation                      Traceback (most recent call last)

    <ipython-input-21-9d795cbe9154> in <module>
          1 f = open('D:/colors.txt')
          2 try:
    ----> 3     f.writelines('magenta\n')
          4 finally:
          5     f.close()
    

    UnsupportedOperation: not writable



فصل دهم
صفحه
141

.. code:: ipython3

    f = open('D:/colors.txt',"a")
    f.writelines('magenta\n')
    f.close()
    f = open('D:/colors.txt')
    f.readlines()




.. parsed-literal::

    ['red\n', 'yellow\n', 'blue\n', 'magenta\n']



.. code:: ipython3

    f.close()

.. code:: ipython3

    with open('D:/colors.txt') as f:
    	for line in f:
    		print ( line,)
    


.. parsed-literal::

    red
    
    yellow
    
    blue
    
    magenta
    
    

.. code:: ipython3

    f.seek(0)


::


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-25-16754355c5bd> in <module>
    ----> 1 f.seek(0)
    

    ValueError: I/O operation on closed file.


.. code:: ipython3

    colors = ['red\n', 'yellow\n', 'blue\n']
    from io import StringIO
    buffer = StringIO()
    buffer.writelines(colors)
    buffer.seek(0)
    for line in buffer:
        print (line,)
    


.. parsed-literal::

    red
    
    yellow
    
    blue
    
    

فصل دهم
صفحه
142

.. code:: ipython3

    buffer.seek(0)
    for line in buffer:
        print (line,)
    


.. parsed-literal::

    red
    
    yellow
    
    blue
    
    

.. code:: ipython3

    buffer.getvalue()




.. parsed-literal::

    'red\nyellow\nblue\n'



.. code:: ipython3

    with open(r"D:/evens.dat","w") as fil:
    	nums=range(20)
    	fil.write("n, n2\n")
    	for i in nums:
    		if not i%2 and not i==0:
    			num=[str(i), str(i**2)]
    			line=",".join(num)
    			fil.write(line+"\n")
    

فصل دهم
صفحه
143

.. code:: ipython3

    import os,csv

.. code:: ipython3

    if not os.path.exists("D:/temp"):
    	os.mkdir("D:/temp")
    

.. code:: ipython3

    data=range(10)
    fil="D:/temp/nums.csv"

فصل دهم
صفحه
144

.. code:: ipython3

    with open(fil, "w", newline='') as csv_file:
    	writer = csv.writer(csv_file, delimiter=',')
    	for i in data:
    		line=map(str,[i,i**2])
    		writer.writerow(line)
    

.. code:: ipython3

    from io import open
    with open(fil, "w", newline='') as csv_file:
    	writer = csv.writer(csv_file, delimiter=',')
    	for i in data:
    		line=map(str,[i,i**2])
    		writer.writerow(line)
    

.. code:: ipython3

    dct={"value":list(data)}
    dct["value2"]=[i**2 for i in data]
    dct["value3"]=[i**3 for i in data]
    with open(fil, "w", newline='') as out_file:
    	writer = csv.DictWriter(out_file,delimiter=',', fieldnames=dct.keys())
    	writer.writeheader()
    	for v in zip(*dct.values()):
    		z=zip(dct.keys(),v)
    		d={}
    		for i in z:
    			d[i[0]]=i[1]
    		writer.writerow(d)
    

فصل دهم
صفحه
145

.. code:: ipython3

    import csv
    fil="D:/temp/nums.csv"
    lis=[[],[],[]]
    with open(fil) as f:
    	reader = csv.reader(f, delimiter=',')
    	next(reader)
    	for row in reader:
    		for i in range(len(row)):
    			lis[i].append(float(row[i]))
    

.. code:: ipython3

    lis




.. parsed-literal::

    [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
     [0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0],
     [0.0, 1.0, 8.0, 27.0, 64.0, 125.0, 216.0, 343.0, 512.0, 729.0]]



فصل دهم
صفحه
146

.. code:: ipython3

    from collections import defaultdict
    import csv
    fil="D:/temp/nums.csv"
    dfd=defaultdict(list)
    with open(fil) as f:
        reader = csv.DictReader(f, delimiter=',')
        print(reader.fieldnames)
        for row in reader:
            for  k in  row.keys():
                dfd[k].append(float(row[k]))
    


.. parsed-literal::

    ['value', 'value2', 'value3']
    

.. code:: ipython3

    dfd["value"]




.. parsed-literal::

    [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]



.. code:: ipython3

    import os

.. code:: ipython3

    #dir(os)

.. code:: ipython3

    #help(os)

.. code:: ipython3

    cwd =os.getcwd()
    print (cwd)
    


.. parsed-literal::

    C:\Users\bairam
    

.. code:: ipython3

    os.chdir("c:/tempt")

.. code:: ipython3

    os.mkdir("c:/tempt ")


::


    ---------------------------------------------------------------------------

    FileExistsError                           Traceback (most recent call last)

    <ipython-input-45-8df41cf8f11e> in <module>
    ----> 1 os.mkdir("c:/tempt ")
    

    FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'c:/tempt '


.. code:: ipython3

    os.system('mkdir tempt')




.. parsed-literal::

    1



.. code:: ipython3

    os.rmdir("c:/tempt")


::


    ---------------------------------------------------------------------------

    PermissionError                           Traceback (most recent call last)

    <ipython-input-47-8c4c4e7de105> in <module>
    ----> 1 os.rmdir("c:/tempt")
    

    PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'c:/tempt'


.. code:: ipython3

    os.rmdir("samples")


::


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-48-0177ea65bf2e> in <module>
    ----> 1 os.rmdir("samples")
    

    FileNotFoundError: [WinError 2] The system cannot find the file specified: 'samples'


.. code:: ipython3

    os.listdir("c:/tempt")
    




.. parsed-literal::

    ['tempt']



.. code:: ipython3

    for file in os.listdir("c:/tempt"):
                       print ( file)
    


.. parsed-literal::

    tempt
    

.. code:: ipython3

    os.chdir(os.pardir)
    os.pardir
    




.. parsed-literal::

    '..'



.. code:: ipython3

    os.getcwd()




.. parsed-literal::

    'c:\\'



for root, dirs, files in os.walk(".", topdown=False):
       for name in files:
             print(os.path.join(root, name))
       for name in dirs:
              print(os.path.join(root, name))


cmdout=os.popen(r"dir C:\users").read()
print (cmdout)


hel = os.popen(“help dir”).read()
print (hel)


فصل دهم
صفحه
148

entry = os.stat("C:\Users")
entry


.. code:: ipython3

    os.name




.. parsed-literal::

    'nt'



os.environ

.. code:: ipython3

    import os.path
    fil="D:/colors.txt"
    if os.path.exists(fil) and os.path.isfile(fil):
    	name=os.path.basename(fil)
    	folder=os.path.dirname(fil)
    	ex=os.path.splitext(fil)[1]
    
    print(name,  folder, ex)
    


.. parsed-literal::

    colors.txt D:/ .txt
    

فصل دهم
صفحه
149

.. code:: ipython3

    from glob import glob
    files=glob("D:/*.txt")
    files
    




.. parsed-literal::

    ['D:/colors.txt',
     'D:/data.txt',
     'D:/data1.txt',
     'D:/datav.txt',
     'D:/lesson2.txt',
     'D:/nums.txt',
     'D:/spi.txt',
     'D:/table.txt']



.. code:: ipython3

    دهم
    صفحه
    149
    تمرین عملی
    1
