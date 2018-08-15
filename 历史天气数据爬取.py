# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 17:09:41 2016

@author: MaMargot
"""

# -*- coding: cp936 -*-
import urllib2
from BeautifulSoup import BeautifulSoup     

f = open('C:\Users\MaMargot\.spyder2\scrpit\wunder-data.txt','w')     #open the file

m = 3                               #get weather data of March(3) 2014
for d in range(1,31):               #loop from 2014.3.1 to 2014.3.31

    timestamp = '2014' + str(m) + str(d)    
    print "Getting data for " + timestamp   #for we can see the process in shell
    url = "http://www.wunderground.com/history/airport/KBUF/2014/" + str(m) + "/" + str(d) + "/DailyHistory.html"
    page = urllib2.urlopen(url)     #get the web page

    soup = BeautifulSoup(page)      #use BeautifulSoup to parsing the web page

    dayTemp1 = soup.findAll(attrs = {"class":"wx-data"})[2].span.string   #the data is showed in some HTML code where <class = "nobr">s are appeared 
    dayTemp2 = soup.findAll(attrs = {"class":"wx-data"})[3].span.string
    dayTemp3 = soup.findAll(attrs = {"class":"wx-data"})[4].span.string
    
    if not dayTemp1 and dayTemp2 and dayTemp3:
        print("Error")
    else:
        if len(str(m)) < 2:             #format it
             mStamp = '0' + str(m)
        else:
             mStamp = str(m)

        if len(str(d)) < 2:             #format it
             dStamp = '0' + str(d)
        else:
             dStamp = str(d)
            
        timestamp = '2014-' + mStamp + '-' + dStamp  #make data look like 2014-03-01,which is convinient for excel or WPS to deal with

    f.write(timestamp + ',' + dayTemp1+','+dayTemp2+','+dayTemp3 + '\n')   #write it to the file
f.close()                           #close the file