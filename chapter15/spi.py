try:
    import util
except:
    from . import util
from collections import  defaultdict
class SPI (object):
    def __init__(self, indata,dates,scales):
        self.scales=scales
        self.rain=indata
        self.dates=dates
    def calculate(self,fit=None):
        spiData=defaultdict(list)
        spiData["date"]=self.dates
        for scale in self.scales:
            dates2=self.dates[scale-1:]
            raindata=util.summov(self.rain,scale)
            spis,groupdate=util.group(raindata,dates2,func=util.SPI_function, fit=fit)
            lags= [float("nan") for i in range(scale-1)]
            spiData[scale]=lags+spis
        self.fields=spiData.keys()
        return spiData

def main():
    import sys
    # make sure there are at least three arguments
    if  len(sys.argv) >=6:
        script = sys.argv[0]
        infile = sys.argv[1]
        raincol ,datecol= sys.argv[2], sys.argv[3]
        outfile = sys.argv[4]
        scales=sys.argv[5:]
        scales=map(int,scales)
        data=util.readcsv(infile)
        rain,dates=data[raincol],data[datecol]
        myspi=SPI(rain,dates,scales).calculate(fit=util.gammafit)
        util.write(myspi,outfile)
        print ('SPI is calcualted and saved in {}'.format(outfile))
    else:
        print ("\nUsage: spi  <infile> <rain col> <date col>\
<outfile> <scale>\n")
        print ("Example: spi  d:/Rain.csv  Rain \
date d:/spi.csv 1 3 6 9 12 24\n")
        #sys.exit(2)
if __name__ == '__main__':
    main()


##    data=util.readcsv("Rain.csv")
##    rain,dates=data["RAIN"],data['date']
##    spi=SPI(rain,dates,[1,3,6])
##    spis=spi.calculate()
##    ##spidata,cols=spidata.calculate()
##    from pylab import *
##    plot(dates,spis[1], label="spi1")
##    plot(dates,spis[3],label="spi3")
##    plot(dates,spis[6],label="spi6")
##    legend()
##    show()
