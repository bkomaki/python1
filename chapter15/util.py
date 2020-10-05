from __future__ import division
from datetime import datetime
dateparser=lambda x:datetime.strptime(x,
                                      "%Y-%m-%d") if "-" in x else datetime.strptime(x,
                                                                                     "%m/%d/%Y")

summov=lambda x,win:[sum(x[i:win+i])for i in range(len(x[win-1:]))]
def resample(data,dates,by="monthly", how="sum"):
    """Convert daily values to monthly(default), 16 (16) daily or 8  (8) daily scales"""
    if by =="monthly":
        funcg= lambda x :(x[0].year, x[0].month)
    grp=groupby(zip(dates, data),key=funcg)
    data=defaultdict(list)
    for i , g in grp:
##        global gdata
        gdata=list(g)
        data["date"].append(gdata[0][0])
        if how=="sum":
            data["data"].append(round(sum([g[1] for g in gdata]),4))
        elif how== "mean":
            h=[g[1] for g in gdata]
            data["data"].append(round(sum(h)/float(len(h)),4))
            
##        data["n"].append(len( gdata))
    #print (data["Rain"],data["date"])
    return  data["data"],data["date"]

################# The cumulative  distribution function(CDF) of normal distribution##################
def cdfnorm(x,mu=0,sigma=1):
    return 0.5*(1+erf((x-mu)/(sigma*sqrt(2)))) #erf=Error function https://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function
def pdfnorm(x,mu=0,std=1):
    """normal distribution for the specified mean and standard deviation"""
    if std<0:
        return float("nan")
    return exp((-0.5*((x-mu)**2)/std**2))/(std*sqrt(2*pi))
    

from math import sqrt,log,e
def gammafit (data):
    n=len(data)
    if n==0:
        return 0,0
    while 0 in data:
        data.remove(0)
    nact=len(data)
    if  nact>0:
        mn=sum(data)/nact
    if nact==1 or sum(data)==0 or sum(data)/nact==data[0]:
        alpha,gamm,mn=0.0,1.0,mn
        return gamm, mn
    sumlog=sum([log(i)for i in data])
    A=log(mn)-sumlog/nact
##    print(data)
    k=(1.0+sqrt(1.0+4.0*A/3.0))/(4.0*A)
    theta=mn/k
    return k,theta

def lower_incomplete_gamma(a,x,d=0,iterations=100):
    if d == iterations:
        if ((d % 2) == 1):
            return 1.0 # end iterations
        else:
            m = d/2
            return x + (m-a)
    if d == 0:
        result = ((x**a) * (e**(-x)))/lower_incomplete_gamma(a,x,d=d+1)
        return result
    elif ((d % 2) == 1):
        m = d - 1
        n = (d-1.0)/2.0
        return a + m - (((a+n)*x)/lower_incomplete_gamma(a,x,d=d+1))
    else:
        m = d-1
        n = d/2.0
        return a+m+((n*x)/(lower_incomplete_gamma(a,x,d=d+1)))
#https://github.com/dj-on-github/sp800_22_tests/blob/master/gamma_functions.py
def gammainc (a,b):
    from math import gamma
    return lower_incomplete_gamma(a,b)/gamma(a)


def cdf2Z(p):
    c=p
    """ P probably betwen 0 and 1 """
    if p<=0 or p>1 :
        print("p={} is out of range".format(c))
        return float("inf")
    if (c-0.5)>0:
        c=1. - c
    if (c-0.5)<0:
        #print(c)
        dt2= -2*log(c)
        t=sqrt(dt2)
        ppf= t- ((.010328*t + .802853)*t+ 2.515517) /\
             (((.001308*t + .189269)*t + 1.432788)*t + 1.)
        if p<0.5:
            ppf=-ppf
        return ppf
    if c-0.5==0:
        return 0
##
##print(cdf2Z(.6),cdf2Z(.4))

from collections import Counter
def SPI_function(x, fit=gammafit):
    zeros=Counter(x)[0]
    pzero=zeros/len(x) 
    x2=list(x[:])
    while 0 in x2 :
        x2.remove(0)
    if fit== gammafit:
        
        k,theta=fit(x2)# apply fit function
        print(pzero)
        if pzero<1:
            cdf1=[cdf2Z(pzero + (1.-pzero) *gammainc(k,i/theta)) for i in x]
        else:
            cdf1=[cdf2Z(pzero-0.0001 ) for i in x]
            
    print(str(fit.__name__),
          "shape ={}, scale= {}, pzero={}".format(k,theta,pzero))
    return cdf1


import io, csv
from collections import defaultdict
def readcsv(infile):
    """input file name, csv format"""
    with io.open(infile, newline='') as csvfile:
            data = defaultdict(list)
            reader = csv.DictReader(csvfile)
            for row in reader:
                for key in  row:
                    try:
                        data[key].append(dateparser(row[key]))
                    except:
                        if row[key]=="NA":
                            row[key]=float("nan")
                            #print(row[key])
                        data[key].append(float(row[key]))
                        
##                        global a
##                        a=row[key]
    keys=data.keys()
    return data


def write (data, outfile, fields=None):
    with io.open(outfile, 'w', newline='') as csvfile:
        if fields==None:
            fields=list(data.keys())
        csvWriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvWriter.writeheader()
    with io.open(outfile, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        for  row in list(zip(*data.values())):
            row=list(row)
            row[0]=row[0].strftime("%Y-%m-%d")
            writer.writerow(row)
    print("The result is saved as {}".format(outfile))
##dates[1]-dates[0]
from itertools import groupby
def group(indata,indate,func=None, fit=None):
    zdata=list(zip(indata,indate))
    grp=groupby(zdata, lambda x: x[1].month)
    P=defaultdict(list)
    gdates= defaultdict(list)
    for i, g in grp:
            for v , d in g:
                    gdates[i].append(d)
                    P[i].append(v)
    res=defaultdict(list)
    for key  in P:
            spiout=func(P[key],fit=fit)
            kdates=gdates[key]
            for d in kdates:
                    res["date"].append(d)
            for v in spiout:
                res["spi"].append(v)
    zdata=list(zip(res["spi"],res["date"]))
    zdata.sort(key=lambda x :x[1])
    res.clear()
    for  k in zdata:
            res["spi"].append(k[0])
            res["date"].append(k[1])
    sp,dat=res["spi"],res["date"]
    return sp,dat

##print(dateparser("2000-5-10"))
##data=[2,5,3,6,7,10]
##sm=summov(data,2)
##print(sm)
##data=[3,2,4,4,5,2,1,1]
##print(gammafit(data))#k = 3.42065439733066, theta= 0.80393973800626
##
###source https://agrimetsoft.com/distributions-calculator/gamma-distribution-fitting#toolSection
##g = (112,118,132,129,121,135,148,148,136,119,104,118 
##          ,115,126,141,135,125,149,170,170,158,133,114,140 
##          ,145,150,178,163,172,178,199,199,184,162,146,166 
##          ,171,180,193,181,183,218,230,242,209,191,172,194
##          ,196,196,236,235,229,243,264,272,237,211,180,201 
##          ,204,188,235,227,234,264,302,293,259,229,203,229 
##          ,242,233,267,269,270,315,364,347,312,274,237,278 
##          ,284,277,317,313,318,374,413,405,355,306,271,306 
##          ,315,301,356,348,355,422,465,467,404,347,305,336 
##          ,340,318,362,348,363,435,491,505,404,359,310,337 
##          ,360,342,406,396,420,472,548,559,463,407,362,405 
##          ,417,391,419,461,472,535,622,606,508,461,390,432 )
##print(gammafit(g))
###  5.49911     ; shape #50.9716      ; scale#  0.0         ; pzero
##g=list(g)#+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
##spig=SPI_function(list(g))
##print(spig)
##data=r"Rain.csv"
##data=readcsv(data)
##rain,dates=data["RAIN"],data['date']
##dates[2]-dates[1]
##
##print(SPI_function(rain[0::12]))


##spim,datesm=group(rain,dates)
#write(res, r"D:\py\book\spi1\pydrought\data\test.csv", ["date", "spi"])
##from pylab import *
##print(dates,spim)
##plot(dates, spim)
##show()

###########SPEI###################
##from __future__ import division
from math import *
def daylight(lat,J):
    
    """lat  latitude [degree]
        J  Julian day
      return L (daylight hours in units of 12 hours), w ( sunset hour angle [radians], d (declination [radians] )"""
    dec=0.4093*sin(2*pi/365*J-1.39) #d declination [radians]
    t=tan(dec)*tan(radians(float(lat)))
    w=acos(-t)#w   the sunset hour angle [radians]
    L=24/pi*w #L daylight hours in units of 12 hours (Average day length of the month )
    return L,w,dec
###########Thornthwaite Evapotranspirration potential ###################
#http://ijarcsse.com/Before_August_2017/docs/papers/Volume_6/8_August2016/V6I8-01812.pdf
def etp(T,lat):
    """  T is the mean air temperature at a 2-m height (C).
          lat  latitude [degree]
      return ETP (Thornthwaite Evapotranspirration potential)
      PE=16Nm((10Tm)/I)**a;  for month m"""
    julian=[17,47,75,105,135,162,198,228,258,288,318,334] # mean average Julian day for each month
    days=[31,28,31,30,31,30,31,31,30,31,30,31]# days in months
    I= sum([(t/5)**1.514  if t>0 else 0 for t in T])#  S(Tm/5)**1.5;for month m:Thornthwaite's temperature efficiency index,heat index  for the year: I index for each month when temperature more than zero.
    a=(6.75e-07)*I**3 -(7.71e-05)*I**2 + 0.01792*I + 0.49239 # Expentail factor
    pet=[]
    for n,  t in  zip(days,T):
        if t<=0:
            pet.append(0)
        elif 0<t<=26.5:
            et=16 *(10*t/I)**a
            pet.append(et)
##            print(et,t)
        elif 26.5<t:
            et=-415.85+32.24*t-0.43*t**2
            pet.append(et)
##            print(et,16 *(10*t/I)**a)
        else:
            raise
    correction=[n/30*(daylight(lat,j)[0])/12. for n, j in zip(days,julian)]
    pet=[c*et for c,et in zip(correction ,pet)]
    return pet#,correction
#############Extraterrestrial radiation for daily periods (Ra) ###########
#http://www.fao.org/3/x0490e/x0490e07.htm
from math import *
def Ra(lat,J):
    """lat latitude [degree] ,
         J  Julian day
      return Ra Extraterrestrial radiation for daily periods  [MJ m-2 day-1],
    References
    R.G. Allen, L.S. Pereira, D. Raes and M. Smith (1998). Crop Evaporation - Guidelines for computing crop water requirements,
    FAO - Food and Agriculture Organization of the United Nations.
    Irrigation and drainage paper 56, Chapter 3. Rome, Italy.
    (http://www.fao.org/docrep/x0490e/x0490e07.htm)  -> Calculation procedures  Eq. 21
    """
    #inverse relative distance Earth-Sun, dr
    Gs= 0.0820 # solar constant = 0.0820 MJ m-2 min-1,
    dr=1+.033*cos(2*pi *J/365) #inverse relative distance Earth-Sun
    N,ws,d=daylight (lat,J)#sunset hour angle (Equation 25 or 26) [rad], d solar decimation (Equation 24) [rad].
    latrad=radians(lat) #latitude [rad]
    jds=sin(latrad)*sin(d)
    jdc=cos(latrad)*cos(d)
    Ra=24*60/pi*Gs* dr*(ws*jds + jdc* sin(ws))
    #print(dr,ws,d ,jds,jdc, Ra)
    return  Ra
##print(Ra(-20,246))
def oudin(Ra,Tmean=None, Tmin=None, Tmax=None):
    """ Ra is the extraterrestrial solar radiation (MJ m-2 d-1) given by the Julian day and the latitude,
         T is the mean air temperature at a 2-m height (C).
     References
    Oudin, Ludovic, Latitia Moulin, Hocine Bendjoudi, and Pierre Ribstein. 2010.
    Estimating Potential Evapotranspiration without Continuous Daily Data
    Possible Errors and Impact on Water Balance Simulations.
    Hydrological Sciences Journal 55 (2): 209-22. 
     http://www.tandfonline.com/doi/full/10.1080/02626660903546118
     Eq. 3     """
    if Tmean==None:
        Tmean=(Tmin+Tmax)/2.
    if (Tmean+5)<0:
        return 0
    else:
        #a=max(T)-min(T)
        return 0.408 *Ra*(Tmean+5.)/100
def hargreaves(Ra,Tmin, Tmax, Tmean=None, KT="hs"):
    """
    Estimate reference evapotranspiration over grass (ETo) using the Hargreaves
    equation.
    Generally, when solar radiation data, relative humidity data
    and/or wind speed data are missing, as an alternative, ETo can be
    estimated using the Hargreaves ETo equation based on equation 52 in Allen et al (1998).
     Tmin: Minimum daily temperature [deg C]
     Tmax: Maximum daily temperature [deg C]
     Tmean: Mean daily temperature [deg C]. If None,
     it can be estimated as (Tmin* + Tmax*) / 2.
     Ra: Extraterrestrial radiation (Ra) [MJ m-2 day-1]. Can be
        estimated using ``RA``.
      Return:  Reference evapotranspiration over grass (ETo) [mm day-1]
      Reference:Estimating Solar Radiation and Evapotranspiration Using Minimum Climatological Data(Hargreaves-Samani equation)
      KT=="hs" -> Hargreaves-Samani equation
      else:
      Hargreaves
    """
    if  Tmean==None:
        Tmean=(Tmin+Tmax)/2.
    if KT=="hs":
##        global kt
        Td=Tmax - Tmin
        kt=0.00185*Td**2 - 0.0433 *Td + 0.4023
        return 0.0135*kt* (Tmean + 17.8) * Td ** 0.5 * 0.408 * Ra #

        
    # Note, multiplied by 0.408 to convert extraterrestrial radiation could
    # be given in MJ m-2 day-1 rather than as equivalent evaporation in
    # mm day-1
    return 0.0023 * (Tmean + 17.8) * Td ** 0.5 * 0.408 * Ra 


##print(oudin(Ra(57.1526,32),3.8)) #0.2557878129597254
##print(hargreaves(Ra(57.1526,32),1.3, 5.6, 3.8))#0.29944219073002043
##def Pristley(Td, T3,Rn):#later
##    """Pristley-Taylor
##    Td the average temperature of the air on the day in question
##    T3, the average temperature of the air 3 days before
##    Rn daily total liquid radiationbMJm-2d-1"""
##    #G  daily total of heat on the soil
##    G=0.38*(Td- T3)
##    #factor of temperature and psychometric coefficient
##    if Td<=0:
##        W=0
##    elif 0<Td<16:
##        W=0.407+(0.0145*Td)
##    elif 16<Td<32:
##        W=0.483+(0.01*Td)
##    return (1.26*W*(Rn-G))/2.45
##def Penman(Tmax,Tmin,T3, wind,Rn, G,UR=1):
##    """Penman-Monteith"""
##    U2=wind
##    omga=0.063 #the psychometric constant kPaC-1
##    T=(Tmax+Tmin)/2#the air mean temperature (daily) in Celsius
##    #G  daily total of heat on the soil
##    G=0.38*(T- T3)
##    ESmax=0.6108*exp(17.27*Tmax)/(247.3+Tmax)
##    ESmin=0.6108*exp(17.27*Tmin)/(247.3+Tmin)
##    Es=(ESmax+ESmin)/2 #saturated vapor pressure kPA
##    Ea=(UR*Es)/100 #the partial vapor pressure kPa
##    S=(4098*Es)/((T+237.2)**2)#curve declivity of vapor pressure.
##    pet=(0.408*S*(Rn-G)+((omga*900*U2*(Es-Ea))/(T+273)))/(S+omga*(1+0.34*U2))
##    return pet
#############PWM & Lmoment #########################
def pascal():
    row=[1]
    while True:
        yield row
        row= [i+j for  i,j  in zip(row+[0],[0]+row)]
def binom(N,s,exact=1):
    if exact:
        if (s > N) or (N < 0) or (s < 0):
            return 0
    can=pascal()
    k=[next(can) for i in range(N+1)]
    return k[N][s]

def binom1(N,s,exact=1):
    if exact:
        if (s > N) or (N < 0) or (s < 0):
            return 0
        val = 1
        for j in range(min(s, N-s)):
            val = (val*(N-j))//(j+1)
        return val
def binom2(N,s):
    if (s > N) or (N < 0) or (s < 0):
        return 0
    else:
        return binom(N-1,s-1)+binom(N-1,s)
#https://www.mathsisfun.com/algebra/binomial-theorem.html
def B(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))
def w(x,s):
    """X:data series
         s: order, integer value {0, 1, .....}
     return The unbiased PWMs (probability weighted moments)"""
    x=list(x)
    x.sort()
    n=len(x)
    s=int(s)
    ws=sum([1/n* x[i-1]*binom(n-i,s)/binom(n-1,s) for i in range(1, n+1)])
    return ws
def gammaLn(x):
   return log(gamma(x))
def lMoment(alpha0,alpha1,alpha2):
    """
    L-moments
    """
    L1= alpha0
    L2= alpha0 - 2*alpha1
    L3= alpha0 - 6*alpha1 + 6*alpha2
    #print ("lMoment",L1,L2,L3)
    return L1,L2,L3
########################log Logistic distribution###############
def LLfit(x):
    """x:data series
        return: scale,shape , location 
        the parameters of the Log-logistic distribution after Singh et al. (1993) """
    w0,w1,w2=w(x,0),w(x,1),w(x,2)
    beta=(2*w1-w0)/(6*w1-w0-6*w2)
    gb=gamma(1+1/beta)*gamma(1-1/beta)
    alpha=(w0-2*w1)*beta/gb
    omga=w0-alpha*gb
    return  alpha,beta,omga #
def logLogisticCDF(x,alpha,beta,omga):
    """ x : non-negative  data series
      Cumulative distribution function of a three parameter Log-logistic distributin  (Fisk distribution)
        scale=.1
        shape=3
        loc=5
        x=7
        logLogisticCDF(x,scale, shape,loc)
        0.9998750156230471"""
    return 1 / (1+pow(alpha/(x-omga),beta));
###########Pearson type III distribution#####################
#http://www.imsbio.co.jp/RGM/R_rdfile?f=nsRFA/man/P3.Rd&d=R_CC
def pe3fit( x):#Pearson3Fit
    #x=[log(i) for i in x]
    pwms=w(x,0),w(x,1),w(x,2)
    L1,L2,L3=lMoment(*pwms)
    t3=L3/L2
    if t3<1/3.:
        tm=3*pi*t3**2
        beta=(1+0.2906*tm)/(tm+0.1882*tm**2-0.0442*tm**3)
    else:
        tm=1-t3
        beta=(0.36067*tm-0.5967*tm**2+0.25361*tm**3)/(1-2.78861*tm+2.56096*tm**2-0.77045*tm**3)
    alpha=sqrt(pi)*L2*exp(gammaLn(beta)-gammaLn(beta+0.5))
    scale=alpha*sqrt(beta)
    if L2< 0:
        skew = -2.0 /sqrt(beta)
        # pearson3_parameters[2] = -2.0 / alpha_root
    else:
        skew = 2.0 / sqrt(beta)
    #print("me",L1, scale,skew)
    return L1, scale,skew

def cdfpe3(x,para1,para2,para3):
    """x p1,p2,p3 Pearson type III distribution which generalizes the gamma distribution"""
    if para2<=0:
        raise RuntimeError(" parameter 2 is lower than 0") 
    if abs(para2)<=01e-6:
        return  cdfnorm(x,para1,para2)
    
    alpha=4/para3**2
    z=2 * (x - para1)/(para2 * para3) + alpha
    res=gammainc(alpha,max(0,z))
    if para3<0:
        res-=1
    return res

def pwm(d,nmom=3):
    d.sort()
    n=len(d)
    betas=[]
    for r in range(nmom):
        i=r+1
        sm=0
        for j in range(n):
            sm=sm+binom(j,r)*d[j]
        betas.append(sm/(n*binom(n-1,r)))
    return betas


def lambdas(p):
    nmom=len(p)
    L=[]
    for i in range(1,nmom+1):
        r=i-1
        sm=0
        for k in range(0,r+1):
            weight=(-1)**(r-k)*binom(r,k)*binom(r+k,k)
            sm=sm+weight*p[k]
        L.append(sm)
    return L

def ratio(L):
    nmom =len(L)
    R=[float("nan")]
    if nmom >= 2:
        R.append( L[1]/L[0])
    if nmom>= 3:
        for r in range(2, nmom):
            R.append(L[r]/L[1])
    ratios = R
    return ratios


from math import  pi,sin
def  glofit(d):
    p=pwm(d)
    lb=lambdas(p)
    r=ratio(lb)
    K =-r[2]
    KK = K * pi/sin(K * pi)
    A = lb[1]/KK
    XI =lb[0] - A * (1 - KK)/K
    omega= A
    alpha=K
    return XI , A,K
from math import exp,log
def glocdf (x, XI , A,K ):
    small = 1e-15
    if x==float("nan"):
        return float("nan")
    z = (x - XI)/A
    arg = 1 - K * z
    if K==0:
        return 1/(1 + exp(-z))
    elif arg > small:
        Y = -log(arg)/K
        return 1/(1 + exp(-Y))

def glcdf(x,XI,A,k):
    z= (x - XI)/A
    if k==0:
        return 1/(1+exp(-z))
    else:
        return 1/(1+(1+k*z)**(-1/k))

    
def SPEI_function(x,fit=None):
    if fit==LLfit:
        cdf=logLogisticCDF
    if  fit==pe3fit:
        print("Pearsin Type 3")
        cdf=cdfpe3
    elif fit ==glofit:
        cdf=glocdf
        
    zeros=Counter(x)[0]
    pzero=zeros/len(x)
    x2=x[:]
    while 0 in x2 :
        x2.remove(0)
    alpha,beta,omga=fit(x2)
    print(str(fit.__name__)+" Fit: ",alpha,beta,omga)
    spei=[cdf2Z(pzero + (1.-pzero) *cdf(i,alpha,beta,omga)) for i in x]
##    cdf1=[cdf(i,alpha,beta,omga ) for i in x]
##    spei=[  cdf2Z(pzero+(1-pzero)*cdfnorm(p))for  p in cdf1]
##    
##    
##    print(cdf2,x)
##    spei=[cdf2Z(c) for c  in cdf2]
    return spei

##
if __name__ == '__main__':
##    data=readcsv("Data/monthly_rain.csv")
##    data=readcsv("data/daily.csv")
##    rain=data["Rain"]
##    date=data['date']
##    rain,date=resample(rain,date)#,by=16 )
##    spi,date =group(rain,date)
##    d=0
##    while d<5:
##            print(spi[d],date[d].strftime("%Y-%m-%d"))
##            d+=1
     data=readcsv("data/gorgandata.csv")
     lat=36.85
     'tmax', 'tmin'
     data["Ra"]=[Ra(lat,x.timetuple().tm_yday) for x in data["Date"]]
     data["Tmean"]=[sum(x)/2 for x in zip(data["tmax"],data["tmin"])]
     data["oudin"]=[oudin(ra,t) for ra,t in zip(data["Ra"],data["Tmean"])]
     data["pe_hs"]=[hargreaves(ra, tmin, tmax) for ra, tmin, tmax in zip(data["Ra"],data["tmin"],data["tmax"])]
     write(data,"c11.csv")
     
     t=11.00951613,11.40431034,8.255483871,15.29716667,21.38709677,26.57183333,27.52290323,27.53225806,25.95,22.105,14.75616667,10.72306452
     et=etp(t,lat)
     
     
     


     
      

    
##
##    T= [6,8,10,12,15,20,25,20,16,12,10,8]
##    T=[23.3, 21.1, 19.6, 17.2, 12.6, 10.9 ,10.0, 11.0, 13.0, 15.8, 17.8, 20.1]
##    print(etp(T,-38))
##    data=[45, 32, 37, 46, 39, 36, 41, 48, 36]
##    spei=SPEI_function(x)
##    print(spei)
##data=[112,118,132,129,121,135,148,148,136,119,104,118 
##          ,115,126,141,135,125,149,170,170,158,133,114,140 
##          ,145,150,178,163,172,178,199,199,184,162,146,166 
##          ,171,180,193,181,183,218,230,242,209,191,172,194 
##          ,196,196,236,235,229,243,264,272,237,211,180,201 
##          ,204,188,235,227,234,264,302,293,259,229,203,229 
##          ,242,233,267,269,270,315,364,347,312,274,237,278 
##          ,284,277,317,313,318,374,413,405,355,306,271,306 
##          ,315,301,356,348,355,422,465,467,404,347,305,336 
##          ,340,318,362,348,363,435,491,505,404,359,310,337 
##          ,360,342,406,396,420,472,548,559,463,407,362,405 
##          ,417,391,419,461,472,535,622,606,508,461,390,432]
##
##    
####    data.sort()
##alpha,beta,omga=LLfit(data)
##cdf1=[logLogisticCDF(i,alpha,beta,omga) for i in data]
##alpha,beta,omga=glofit(data)
##cdf2=[glocdf(i,alpha,beta,omga) for i in data]

##    
##    alpha,beta,omga=pe3fit(data)
##    cdf2=[cdfpe3(i,alpha,beta,omga) for i in data]
##    from scipy import stats
##    import matplotlib.pyplot as plt
##    fig, ax = plt.subplots(1, 1)
##    c,loc,scale=stats.fisk.fit(data)
##    ax.plot(data, stats.fisk.cdf(data, c,loc,scale),
##            'r-', lw=2, alpha=0.6, label='fisk cdf')
##    ax.plot(data, cdf1,
##            'g-', lw=1, alpha=0.6, label='LL cdf')
##    ax.plot(data, cdf2,
##            'b-', lw=2, alpha=0.6, label='pe3 cdf')
##    from lmoments3 import distr
##    ##pe3
##    paras = distr.pe3.lmom_fit(data)
##    print("lmoments3",paras)
##    cdf3=distr.pe3.cdf(data,*paras.values())
##    ax.plot(data, cdf3,
##            'k*-', lw=5, alpha=0.2, label='lm3  cdf')
##    plt.legend()
##    plt.show()
##    #SPEI_function(data ,fit=pe3fit)
    
     

