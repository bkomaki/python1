import os
inf=r"D:\spi\pydrought\data\Rain.csv"
cols="RAIN date"
outf=r"D:\spi\pydrought\data\spiss.csv"
scales="1 3 6 9 "
cmd=r"D:\spi\pydrought\spi.py"
py="python"
expression=" ".join([py,cmd, inf, cols,outf ,scales])         
os.system(expression)

import subprocess 
try:
    with open('output.txt', 'wb') as f:
        subprocess.check_call(expression, stdout=f, stderr=f)
except subprocess.CalledProcessError as error:
    print (error)
    with open('output.txt') as f:
        for line in f:
            print (line,)
##        
##import os
##p = sp.Popen(exp, shell=True,stdout=sp.PIPE)
##pid, sts = os.waitpid(p.pid, 0)


##try:
##    ps=sp.check_output(exp)
##except sp.CalledProcessError as error:
##    print (error)
