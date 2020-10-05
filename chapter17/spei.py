try:
    from . import util
except:
    import util
from collections import  defaultdict
from itertools import groupby
class SPEI (object):
    def __init__(self, date,rain,Tmean,latDeg=None, scales=None):
        self.rain, self.Tmean, self.date=rain,Tmean,date
        self.scales=scales
        self.Ds,self.dates,self.ETP=self.initial(latDeg)
    def initial(self,latDeg):
        values=zip(self.Tmean, self.date,self.rain)
        grp=groupby(values, key=lambda x : x[1].year)
        data=defaultdict(list)
        for k, g in  grp:
            g=list(g)
            t=[i[0] for i in g]
            date=[i[1] for i in g]
            etp=util.etp(t, latDeg)
            print(etp)
            D=[g[i][2]-etp[i] for i in range(len(g))]
            for i in range(len(etp)):
                data["etp"].append(etp[i])
                data["D"].append(D[i])
                data["date"].append(g[i][1])
        return  data["D"],data["date"],data["etp"]
    def calculate(self, fit=None):
        speiData=defaultdict(list)
        speiData["date"]=self.dates
        for scale in self.scales:
            print("scale\t",scale)
            data=util.summov(self.Ds,scale)
            #print(data)
            dates2=self.dates[scale-1:]
            spei,groupdate=util.group(data,dates2,func=util.SPEI_function, fit=fit)
            lags= [float("nan") for i in range(scale-1)]
            for i in lags+spei:
                speiData[scale].append(i)
        return speiData


def main():
    from  util import readcsv,write
    import sys
    if  len(sys.argv) >=7:
        script = sys.argv[0]
        infile = sys.argv[1]
        rainCol ,Tcol,dateCol= sys.argv[2], sys.argv[3],sys.argv[4]
        lat, outfile ,scales= sys.argv[5], sys.argv[6],sys.argv[7:]
        scales=map(int,scales)
        data=readcsv(infile)
        rain, tmean, date=data[rainCol],data[Tcol],data[dateCol]
        myspei=SPEI(date,rain, tmean, latDeg=lat ,scales=scales)
        myspeic=myspei.calculate(fit=util.LLfit)
        print(myspeic.keys())
        util.write(myspeic,outfile)
        print ('spei is calcualted and saved in {}'.format(outfile))
    else:
        print ("\nUsage: spei  <infile> <RAIN col> <Tmean col> <date col>\
<latitude> <outfile> <scales>\n")
        print ("Example: spei  data/wichita.csv  PRCP TMED date 37.6475 data/outspei.csv 1 3 6 9 12 24")
        #sys.exit(2)
if __name__ == '__main__':
    main()
  
##import util
##infile="data/wichita.csv"#gorgandata.csv" lat=54.432922
##data=util.readcsv(infile)
##print(data.keys())
##scale=[1,3,6,12]
####    for i , j in zip(data["tmin"], data["tmax"]):
####        data["TMED"].append((i+j)/2)
####        'Date', 'RAIN', 'Tmean'
##rain, tmean, date=data["PRCP"],data["TMED"],data["date"]
##myspei=SPEI(date,rain, tmean, latDeg=37.6475 ,scales=scale)
##myspeic=myspei.calculate(fit=util.LLfit)
##util.write(myspeic,infile.replace(".csv", "spei2.csv"))
####        

            
