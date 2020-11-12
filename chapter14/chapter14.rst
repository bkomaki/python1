فصل 14

صفحه 218

.. code:: ipython3

     import time

.. code:: ipython3

    time.time()




.. parsed-literal::

    1605177617.8485289



.. code:: ipython3

    time.ctime()




.. parsed-literal::

    'Thu Nov 12 14:10:35 2020'



.. code:: ipython3

    time.ctime(0)




.. parsed-literal::

    'Thu Jan  1 03:30:00 1970'



صفحه 219

.. code:: ipython3

    time. localtime ()




.. parsed-literal::

    time.struct_time(tm_year=2020, tm_mon=11, tm_mday=12, tm_hour=14, tm_min=11, tm_sec=34, tm_wday=3, tm_yday=317, tm_isdst=0)



.. code:: ipython3

    time.gmtime()




.. parsed-literal::

    time.struct_time(tm_year=2020, tm_mon=11, tm_mday=12, tm_hour=10, tm_min=42, tm_sec=11, tm_wday=3, tm_yday=317, tm_isdst=0)



.. code:: ipython3

    t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)

.. code:: ipython3

    time.mktime(t)




.. parsed-literal::

    1234877618.0



.. code:: ipython3

    time.localtime(1234877618.0)




.. parsed-literal::

    time.struct_time(tm_year=2009, tm_mon=2, tm_mday=17, tm_hour=17, tm_min=3, tm_sec=38, tm_wday=1, tm_yday=48, tm_isdst=0)



.. code:: ipython3

    time.strftime("%Y-%m-%d, %H:%M:%S")




.. parsed-literal::

    '2020-11-12, 14:13:22'



.. code:: ipython3

    time.strftime("%Y-%m-%d, %H:%M:%S", time.gmtime(2e9))




.. parsed-literal::

    '2033-05-18, 03:33:20'



صفحه 220

.. code:: ipython3

    time.strptime('2019-10-11',"%Y-%m-%d")




.. parsed-literal::

    time.struct_time(tm_year=2019, tm_mon=10, tm_mday=11, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=284, tm_isdst=-1)



.. code:: ipython3

    time.asctime(time.localtime())




.. parsed-literal::

    'Thu Nov 12 14:14:29 2020'



.. code:: ipython3

    time.daylight




.. parsed-literal::

    1



صفححه 221

.. code:: ipython3

    time.timezone




.. parsed-literal::

    -12600



.. code:: ipython3

     time.tzname




.. parsed-literal::

    ('Iran Standard Time', 'Iran Daylight Time')



.. code:: ipython3

    time.altzone




.. parsed-literal::

    -16200



.. code:: ipython3

    for i in range(3):
        print(time.strftime("%H:%M:%S +0000", time.gmtime()))
        time.sleep(5)
        
    


.. parsed-literal::

    10:50:43 +0000
    10:50:45 +0000
    10:50:47 +0000
    

صفحه 22

.. code:: ipython3

    import time
    from threading import Timer
    def print_time(c):
         print (f"From print_time {c}", time.time())
    
    def print_some_times():
         n,end,lag=0,10,5
         while n<=end:
             Timer(lag*n, print_time, [n]).start()
             n+=1
    
    
    print_some_times()
     


.. parsed-literal::

    From print_time 0 1605179174.6929007
    From print_time 1 1605179179.7119954
    From print_time 2 1605179184.696246
    From print_time 3 1605179189.7021713
    From print_time 4 1605179194.695672
    From print_time 5 1605179199.7008562
    From print_time 6 1605179204.692911
    From print_time 7 1605179209.6947324
    From print_time 8 1605179214.7015996
    From print_time 9 1605179219.7053568
    From print_time 10 1605179224.6944613
    

.. code:: ipython3

    from datetime import datetime,date,timedelta

.. code:: ipython3

    #from datetime import *

.. code:: ipython3

    from datetime import datetime
    datetime.now()
    




.. parsed-literal::

    datetime.datetime(2020, 11, 12, 14, 37, 42, 999044)



صفحه 223

.. code:: ipython3

    datetime.utcnow()




.. parsed-literal::

    datetime.datetime(2020, 11, 12, 11, 8, 17, 359211)



.. code:: ipython3

    d=datetime(2014,11,25,3,56,45,1000)

.. code:: ipython3

    d.year
    
    




.. parsed-literal::

    2014



.. code:: ipython3

    d.day




.. parsed-literal::

    25



.. code:: ipython3

    d.microsecond
    




.. parsed-literal::

    1000



.. code:: ipython3

    print (d.tzinfo)


.. parsed-literal::

    None
    

.. code:: ipython3

    type(d)




.. parsed-literal::

    datetime.datetime



.. code:: ipython3

    d.date()




.. parsed-literal::

    datetime.date(2014, 11, 25)



.. code:: ipython3

    from datetime import date,time,datetime
    d = date(2006, 7, 14)
    t = time(12, 30)
    datetime.combine(d, t)
    




.. parsed-literal::

    datetime.datetime(2006, 7, 14, 12, 30)



صفحه 224

.. code:: ipython3

    from datetime import datetime
    now = datetime.now()
    now
    
    




.. parsed-literal::

    datetime.datetime(2020, 11, 12, 14, 43, 20, 137188)



.. code:: ipython3

    now.strftime("%Y-%m-%d %H:%M:%S")




.. parsed-literal::

    '2020-11-12 14:43:20'



.. code:: ipython3

    dt = datetime.strptime("21/11/2006 16:30:47.5555", "%d/%m/%Y %H:%M:%S.%f")
    dt
    




.. parsed-literal::

    datetime.datetime(2006, 11, 21, 16, 30, 47, 555500)



.. code:: ipython3

    str(dt)




.. parsed-literal::

    '2006-11-21 16:30:47.555500'



.. code:: ipython3

    dt.isoformat("-")




.. parsed-literal::

    '2006-11-21-16:30:47.555500'



.. code:: ipython3

    dt.strftime("%X")




.. parsed-literal::

    '16:30:47'



.. code:: ipython3

    dt.strftime("%x")




.. parsed-literal::

    '11/21/06'



.. code:: ipython3

    dt.strftime("%c")




.. parsed-literal::

    'Tue Nov 21 16:30:47 2006'



.. code:: ipython3

    dt.strftime("%d-%m-%Y %H:%M %a")




.. parsed-literal::

    '21-11-2006 16:30 Tue'



.. code:: ipython3

    dt.strftime("%A, %d. %B %Y %I:%M%p")




.. parsed-literal::

    'Tuesday, 21. November 2006 04:30PM'



.. code:: ipython3

    textStr = "On January the 5th of 2018 meet me at 5 PM"
    dtm = datetime.strptime(textStr, "On %B the %dth of %Y meet me at %I %p")
    print(dtm)


.. parsed-literal::

    2018-01-05 17:00:00
    

صفحه 225

.. code:: ipython3

    'The {1} is {0:%Y}, the {2} is {0:%d},the {3} is {0:%B}.'.format(dt, "year","day", "month")




.. parsed-literal::

    'The year is 2006, the day is 21,the month is November.'



.. code:: ipython3

    tt=dt.timetuple()
    print(tt)
    


.. parsed-literal::

    time.struct_time(tm_year=2006, tm_mon=11, tm_mday=21, tm_hour=16, tm_min=30, tm_sec=47, tm_wday=1, tm_yday=325, tm_isdst=-1)
    

.. code:: ipython3

    for item in tt:
        print (item)
    


.. parsed-literal::

    2006
    11
    21
    16
    30
    47
    1
    325
    -1
    

صفحه 226

.. code:: ipython3

    from datetime import datetime
    datetime.strptime("2004-123", '%Y-%j').strftime('%Y-%m-%d')
    




.. parsed-literal::

    '2004-05-02'



.. code:: ipython3

    from time import localtime
    x = localtime()
    datetime(*x[:7])
    




.. parsed-literal::

    datetime.datetime(2020, 11, 12, 14, 50, 50, 3)



.. code:: ipython3

    from datetime import datetime
    dt=datetime(2007,1,23,3,45,32,100)
    dt.toordinal()
    
    




.. parsed-literal::

    732699



.. code:: ipython3

    datetime.fromordinal(732699)




.. parsed-literal::

    datetime.datetime(2007, 1, 23, 0, 0)



صفحه227

.. code:: ipython3

    datetime.fromordinal(1)




.. parsed-literal::

    datetime.datetime(1, 1, 1, 0, 0)



.. code:: ipython3

    from datetime import datetime
    du = datetime.fromtimestamp(1172969203.1)
    print(du)
    


.. parsed-literal::

    2007-03-04 04:16:43.100000
    

.. code:: ipython3

    from time import mktime
    mktime(du.timetuple())+1e-6*du.microsecond
    




.. parsed-literal::

    1172969203.1



.. code:: ipython3

    from datetime import timedelta
    d5=timedelta(days=5)
    d5
    




.. parsed-literal::

    datetime.timedelta(days=5)



.. code:: ipython3

    d = timedelta(microseconds=-1)
    print (d.days, d.seconds, d.microseconds)
    


.. parsed-literal::

    -1 86399 999999
    

صفحه 228

.. code:: ipython3

    timedelta(hours=-5)
    print(_)
    


.. parsed-literal::

    5 days, 0:00:00
    

.. code:: ipython3

    year = timedelta(days=365)
    year.total_seconds()




.. parsed-literal::

    31536000.0



.. code:: ipython3

    another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
    
    another_year
    




.. parsed-literal::

    datetime.timedelta(days=365)



.. code:: ipython3

    year == another_year




.. parsed-literal::

    True



.. code:: ipython3

    ten_years = 10 * year
    ten_years, ten_years.days // 365
    nine_years = ten_years - year
    nine_years, nine_years.days // 365
    
    




.. parsed-literal::

    (datetime.timedelta(days=3285), 9)



.. code:: ipython3

    three_years = nine_years // 3
    three_years, three_years.days // 365
    abs(three_years - ten_years) == 2 * three_years + year




.. parsed-literal::

    True



صفحه 
229
#pip install jdatetime

.. code:: ipython3

    import jdatetime as jd

.. code:: ipython3

    j=jd.GregorianToJalali(2001,2,23)
    print (j.jyear,j.jmonth,j.jday)
    


.. parsed-literal::

    1379 12 5
    

.. code:: ipython3

    jyear,jmonth, jday=j.getJalaliList()
    print(jyear,jmonth, jday)
    


.. parsed-literal::

    1379 12 5
    

.. code:: ipython3

    s=jd.JalaliToGregorian(1360,12,25)
    print (s.gyear,s.gmonth,s.gday)
    


.. parsed-literal::

    1982 3 16
    

تمرین عملی

مسئله 1

.. code:: ipython3

    from datetime import date
    import jdatetime as jd
    def convert( year, month, day):
        datej=jd.JalaliToGregorian(year,month,day)
        dateg=date(*datej.getGregorianList())
        jday=dateg.timetuple().tm_yday
        f=dateg.strftime("day:%A, day numer in week: %w, and Julian day:%j")
        return f
    

صفحه 230

.. code:: ipython3

    d=convert( 1379, 12, 29)

.. code:: ipython3

    d




.. parsed-literal::

    'day:Monday, day numer in week: 1, and Julian day:078'



صفحه 231

مسئله 2 : راه حل اول

.. code:: ipython3

    import jdatetime as jd
    from datetime import timedelta, datetime
    import csv
    td=timedelta(days=15)
    date1=datetime(2011,1,1)
    date2=datetime(2012,1,1)
    with open('d:/dates.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["row", "Jalali", "Gregory"])
        i=0
        while date1<date2:
            g=jd.GregorianToJalali(date1.year,date1.month,    date1.day)
            jdat=list(map(str,g.getJalaliList()))
            jdat="-".join(jdat)
            i+=1
            dates=[str(i), jdat, date1.strftime("%Y-%m-%d")]
            
            writer.writerow(dates)
            date1+=td

مسئله 2 : راه حل دوم

.. code:: ipython3

    import jdatetime as jd
    from datetime import timedelta, datetime
    import csv
    def date_range(start, end, delta):
        td=timedelta(days=15)
        d1=datetime.strptime( start,"%Y-%m-%d")
        d2=datetime.strptime( end,"%Y-%m-%d")
        lists=[]
        while d1<d2:
            g=jd.GregorianToJalali(d1.year,d1.month, d1.day)
            jdat=list(map(str,g.getJalaliList()))
            dates=["-".join(jdat), d1.strftime("%Y-%m-%d")]
            d1+=td
            lists.append(dates)
        return lists
    dr=date_range("2011-1-1","2012-1-1",15)
    
    with open('d:/dates.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["index", "Jalali", "Gregory"])
        for  i in range(len(dr)):
            writer.writerow([str(i+1)]+dr[i])

مسئله 3

.. code:: ipython3

    from datetime import date
    import jdatetime as jd
    today=date(2019,2,3)
    birthday=jd.JalaliToGregorian(1365,5,17)
    birthdayg=date(*birthday.getGregorianList())
    delta=today-birthdayg
    y=delta.days/365.25
    print(y)


.. parsed-literal::

    32.49007529089665
    

مسئله 4

.. code:: ipython3

    from datetime import  datetime, timedelta
    def age2date(age):
        bd=datetime.now()-age*timedelta(days=365.25)
        g=jd.GregorianToJalali(bd.year,bd.month,bd.day)
        return  (g.jyear, g.jmonth,g.jday),( g.gyear, g.gmonth,g.gday)
    age2date(30)




.. parsed-literal::

    ((1369, 8, 22), (1990, 11, 13))



مسئله 5

.. code:: ipython3

    import time
    m=time.strptime('2019-12-11 11:46:3',"%Y-%m-%d %H:%M:%S")
    m=time.mktime(m)
    t=time.strptime('2019-12-11 12:18:44',"%Y-%m-%d %H:%M:%S")
    t=time.mktime(t)
    minutes=(m-t)/60
    minutes
    




.. parsed-literal::

    -32.68333333333333



.. code:: ipython3

    m-t




.. parsed-literal::

    -1961.0



