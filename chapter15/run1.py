import sys
sys.path.append(r"D:\spi")
from pydrought import SPI
from pydrought.util import readcsv,write
import util
data=r"data\Rain.csv"
data=readcsv(data)
rain,dates=data["RAIN"],data["date"]
spi=SPI(rain,dates,[1,3,6])
spivalue=spi.calculate(fit=util.gammafit)
write(spivalue,r"D:\spi\pydrought\spi.csv")


