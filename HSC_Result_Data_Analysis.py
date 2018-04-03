import pandas as pd
from matplotlib import pyplot as p
import numpy as np
from math import fsum
d201=[i for i in range(1,7)]
d201[1] = pd.read_excel("HSC_data.xlsx","2011")
d201[2] = pd.read_excel("HSC_data.xlsx","2012")
d201[3] = pd.read_excel("HSC_data.xlsx","2013")
d201[4] = pd.read_excel("HSC_data.xlsx","2014")
d201[5] = pd.read_excel("HSC_data.xlsx","2015")
s=[i for i in range(1,7)] 

#Distinction
dist=[i for i in range(1,7)] 
adist=[i for i in range(1,7)]
#First class
fc=[i for i in range(1,7)] 
afc=[i for i in range(1,7)]
#Second class
sc=[i for i in range(1,7)] 
asc=[i for i in range(1,7)]
#Fail
fail=[i for i in range(1,7)] 
afail=[i for i in range(1,7)] 
    
sum=0.0
def createsheet(x):
    s[x]=[]
    for i in range(0,2000):
        l=list(d201[x].iloc[i])
        sum=0.0
        for j in range(1,7):
            sum=sum+l[j]
        sum=sum/6
        s[x].insert(i,round(sum,2))    

#print(s1)
createsheet(1)
createsheet(2)
createsheet(3)
createsheet(4)
createsheet(5)

    
# Marks of sheets 
def create(x):  
    dist[x] = [i for i in s[x] if i>=75]
    adist[x]=(len(dist[x])/20)
    fc[x]=[i for i in s[x] if i>=60 and i<75 ]
    afc[x]=(len(fc[x])/20)
    sc[x]=[i for i in s[x] if i>=40 and i<60 ]
    asc[x]=(len(sc[x])/20)
    fail[x]=[i for i in s[x] if i<40]
    afail[x]=(len(fail[x])/20)

# Marks of first sheet
create(1)

# Marks of second sheet
create(2)

# Marks of Third Sheet
create(3)

# Marks of fourth sheet
create(4)

# Marks of fifth sheet
create(5)

# Subject wise marks

#Object of subjects
#Physics Marks
physics=[i for i in range(1,7)] 
#Maths Marks
maths=[i for i in range(1,7)] 
#Chemistry Marks
chemistry=[i for i in range(1,7)] 
#Biology
biology=[i for i in range(1,7)] 
#Hindi Marks
hindi=[i for i in range(1,7)] 
#English Marks
english=[i for i in range(1,7)]

sub=['English','Hindi','Physics','Chemistry','Maths','Biology']
def submarks(x):
    english[x]=d201[x][sub[0]]
    hindi[x]=d201[x][sub[1]]
    physics[x]=d201[x][sub[2]]
    chemistry[x]=d201[x][sub[3]]
    maths[x]=d201[x][sub[4]]
    biology[x]=d201[x][sub[5]]
# Year wise subjects marks        
for i in range(1,6):
    submarks(i)
    



#Student pass in each year
x2=["2011","2012","2013","2014","2015"]
bar2 =[round((adist[1]+afc[1]+asc[1]),2),round((adist[2]+afc[2]+asc[2]),2),round((adist[3]+afc[3]+asc[3]),2),round((adist[4]+afc[4]+asc[4]),2),round((adist[5]+afc[5]+asc[5]),2)];
p.bar(x2,bar2,align='center')
p.title('Student pass in each year')
p.ylabel('Pass in each year')
p.xlabel('Passing Year')
p.show()

#Student passed with distinction
x2=["2011","2012","2013","2014","2015"]
bar2 =[round(adist[1],2),round(adist[2],2),round(adist[3],2),round(adist[4],2),round(adist[5],2)];
p.bar(x2,bar2,align='center')
p.title('Student passed with distinction ')
p.ylabel('percentage of students Passed with distinction ')
p.xlabel('Passing Year')
p.show()

#Student passed in first class
x2=["2011","2012","2013","2014","2015"]
bar2 =[round(afc[1],2),round(afc[2],2),round(afc[3],2),round(afc[4],2),round(afc[5],2)];
p.bar(x2,bar2,align='center')
p.title('Student passed with First class ')
p.ylabel('percentage of students Passed with First Class ')
p.xlabel('Passing Year')
p.show()

#Student passed with Second Class
x2=["2011","2012","2013","2014","2015"]
bar2 =[round(asc[1],2),round(asc[2],2),round(asc[3],2),round(asc[4],2),round(asc[5],2)];
p.bar(x2,bar2,align='center')
p.title('Student passed with Second Class ')
p.ylabel('percentage of students Passed with Second Class ')
p.xlabel('Passing Year')
p.show()

#Student Fail in exam in Each year
x2=["2011","2012","2013","2014","2015"]
bar2 =[round(afail[1],2),round(afail[2],2),round(afail[3],2),round(afail[4],2),round(afail[5],2)];
p.bar(x2,bar2,align='center')
p.title('Student Fail in Exam')
p.ylabel('percentage of students Fail ')
p.xlabel('Year')
p.show()

#Student passed in exam
x2=[2011,2012,2013,2014,2015]
bar2=[round((adist[1]+afc[1]+asc[1]),2),round((adist[2]+afc[2]+asc[2]),2),round((adist[3]+afc[3]+asc[3]),2),round((adist[4]+afc[4]+asc[4]),2),round((adist[5]+afc[5]+asc[5]),2)];
p.plot(x2,bar2,'y-')
p.title('Student pass in each year')
p.ylabel('Pass in each year')
p.xlabel('Passing Year')
p.show()

#Student passed with distinction
x2=[2011,2012,2013,2014,2015]
bar2=[round(adist[1],2),round(adist[2],2),round(adist[3],2),round(adist[4],2),round(adist[5],2)];
p.plot(x2,bar2,'r-')
p.title('Student passed with distinction ')
p.ylabel('percentage of students Passed with distinction ')
p.xlabel('Passing Year')
p.show()

#Student passed with first Class
x2=[2011,2012,2013,2014,2015]
bar2=[round(afc[1],2),round(afc[2],2),round(afc[3],2),round(afc[4],2),round(afc[5],2)];
p.plot(x2,bar2,'r-')
p.title('Student passed with First class ')
p.ylabel('percentage of students Passed with First Class ')
p.xlabel('Passing Year')
p.show()

#Student passed with Second Class
x2=[2011,2012,2013,2014,2015]
bar2=[round(asc[1],2),round(asc[2],2),round(asc[3],2),round(asc[4],2),round(asc[5],2)];
p.plot(x2,bar2,'r-')
p.title('Student passed with Second Class ')
p.ylabel('percentage of students Passed with Second Class ')
p.xlabel('Passing Year')
p.show()

#Students failed in exam
x2=[2011,2012,2013,2014,2015]
bar2=[round(afail[1],2),round(afail[2],2),round(afail[3],2),round(afail[4],2),round(afail[5],2)];
p.plot(x2,bar2,'r-')
p.title('Student Fail in Exam')
p.ylabel('percentage of students Fail')
p.xlabel('Year')
p.show()

#biology graphs

bins = [i for i in range(101) if i%5==0]
p.hist(biology[1], bins, histtype='bar', alpha=0.5,label='Biology', rwidth=0.8, color='skyblue')
p.xlabel('Marks Of Biology')
p.ylabel('Number of Students')
p.title('Year 2011')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(biology[2], bins, histtype='bar', alpha=0.5,label='Biology', rwidth=0.8, color='skyblue')
p.xlabel('Marks Of Biology')
p.ylabel('Number of Students')
p.title('Year 2012')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(biology[3], bins, histtype='bar', alpha=0.5,label='Biology', rwidth=0.8, color='skyblue')
p.xlabel('Marks Of Biology')
p.ylabel('Number of Students')
p.title('Year 2013')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(biology[4], bins, histtype='bar', alpha=0.5,label='Biology', rwidth=0.8, color='skyblue')
p.xlabel('Marks Of Biology')
p.ylabel('Number of Students')
p.title('Year 2014')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(biology[5], bins, histtype='bar', alpha=0.5,label='Biology', rwidth=0.8, color='skyblue')
p.xlabel('Marks Of Biology')
p.ylabel('Number of Students')
p.title('Year 2015')
p.legend()
p.show()

#chemistry graphs

bins = [i for i in range(101) if i%5==0]
p.hist(chemistry[1], bins, histtype='bar', alpha=0.5,label='Chemistry', rwidth=0.8, color='black')
p.xlabel('Marks Of Chemistry')
p.ylabel('Number of Students')
p.title('Year 2011')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(chemistry[2], bins, histtype='bar', alpha=0.5,label='Chemistry', rwidth=0.8, color='black')
p.xlabel('Marks Of Chemistry')
p.ylabel('Number of Students')
p.title('Year 2012')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(chemistry[3], bins, histtype='bar', alpha=0.5,label='Chemistry', rwidth=0.8, color='black')
p.xlabel('Marks Of Chemistry')
p.ylabel('Number of Students')
p.title('Year 2013')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(chemistry[4], bins, histtype='bar', alpha=0.5,label='Chemistry', rwidth=0.8, color='black')
p.xlabel('Marks Of Chemistry')
p.ylabel('Number of Students')
p.title('Year 2014')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(chemistry[5], bins, histtype='bar', alpha=0.5,label='Chemistry', rwidth=0.8, color='black')
p.xlabel('Marks Of Chemistry')
p.ylabel('Number of Students')
p.title('Year 2015')
p.legend()
p.show()

#english graphs

bins = [i for i in range(101) if i%5==0]
p.hist(english[1], bins, histtype='bar', alpha=0.5,label='English', rwidth=0.8, color='g')
p.xlabel('Marks Of English')
p.ylabel('Number of Students')
p.title('Year 2011')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(english[2], bins, histtype='bar', alpha=0.5,label='English', rwidth=0.8, color='g')
p.xlabel('Marks Of English')
p.ylabel('Number of Students')
p.title('Year 2012')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(english[3], bins, histtype='bar', alpha=0.5,label='English', rwidth=0.8, color='g')
p.xlabel('Marks Of English')
p.ylabel('Number of Students')
p.title('Year 2013')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(english[4], bins, histtype='bar', alpha=0.5,label='English', rwidth=0.8, color='g')
p.xlabel('Marks Of English')
p.ylabel('Number of Students')
p.title('Year 2014')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(english[5], bins, histtype='bar', alpha=0.5,label='English', rwidth=0.8, color='g')
p.xlabel('Marks Of English')
p.ylabel('Number of Students')
p.title('Year 2015')
p.legend()
p.show()

#Hindi graphs

bins = [i for i in range(101) if i%5==0]
p.hist(hindi[1], bins, histtype='bar', alpha=0.5,label='Hindi', rwidth=0.8, color='y')
p.xlabel('Marks Of Hindi')
p.ylabel('Number of Students')
p.title('Year 2011')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(hindi[2], bins, histtype='bar', alpha=0.5,label='Hindi', rwidth=0.8, color='y')
p.xlabel('Marks Of Hindi')
p.ylabel('Number of Students')
p.title('Year 2012')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(hindi[3], bins, histtype='bar', alpha=0.5,label='Hindi', rwidth=0.8, color='y')
p.xlabel('Marks Of Hindi')
p.ylabel('Number of Students')
p.title('Year 2013')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(hindi[4], bins, histtype='bar', alpha=0.5,label='Hindi', rwidth=0.8, color='y')
p.xlabel('Marks Of Hindi')
p.ylabel('Number of Students')
p.title('Year 2014')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(hindi[5], bins, histtype='bar', alpha=0.5,label='Hindi', rwidth=0.8, color='y')
p.xlabel('Marks Of Hindi')
p.ylabel('Number of Students')
p.title('Year 2015')
p.legend()
p.show()

#Maths project

bins = [i for i in range(101) if i%5==0]
p.hist(maths[1], bins, histtype='bar', alpha=0.5,label='Maths', rwidth=.9, color='b')
p.xlabel('Marks Of Maths')
p.ylabel('Number of Students')
p.title('Year 2011')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(maths[2], bins, histtype='bar', alpha=0.5,label='Maths', rwidth=.9, color='b')
p.xlabel('Marks Of Maths')
p.ylabel('Number of Students')
p.title('Year 2012')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(maths[3], bins, histtype='bar', alpha=0.5,label='Maths', rwidth=.9, color='b')
p.xlabel('Marks Of Maths')
p.ylabel('Number of Students')
p.title('Year 2013')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(maths[4], bins, histtype='bar', alpha=0.5,label='Maths', rwidth=.9, color='b')
p.xlabel('Marks Of Maths')
p.ylabel('Number of Students')
p.title('Year 2014')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(maths[5], bins, histtype='bar', alpha=0.5,label='Maths', rwidth=.9, color='b')
p.xlabel('Marks Of Maths')
p.ylabel('Number of Students')
p.title('Year 2015')
p.legend()
p.show()

#Physics graphs.

bins = [i for i in range(101) if i%5==0]
p.hist(physics[1], bins, histtype='bar', alpha=0.5,label='Physics', rwidth=0.8, color='r')
p.xlabel('Marks Of Physics')
p.ylabel('Number of Students')
p.title('Year 2011')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(physics[2], bins, histtype='bar', alpha=0.5,label='Physics', rwidth=0.8, color='r')
p.xlabel('Marks Of Physics')
p.ylabel('Number of Students')
p.title('Year 2012')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(physics[3], bins, histtype='bar', alpha=0.5,label='Physics', rwidth=0.8, color='r')
p.xlabel('Marks Of Physics')
p.ylabel('Number of Students')
p.title('Year 2013')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(physics[4], bins, histtype='bar', alpha=0.5,label='Physics', rwidth=0.8, color='r')
p.xlabel('Marks Of Physics')
p.ylabel('Number of Students')
p.title('Year 2014')
p.legend()
p.show()

bins = [i for i in range(101) if i%5==0]
p.hist(physics[5], bins, histtype='bar', alpha=0.5,label='Physics', rwidth=0.8, color='r')
p.xlabel('Marks Of Physics')
p.ylabel('Number of Students')
p.title('Year 2015')
p.legend()
p.show()

# pie graphs

labels = 'Distinction', 'First Class', 'Second Class', 'Fail'
sizes = [adist[1], afc[1], asc[1], afail[1]]
explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = p.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
p.title('Student Marks Analysis of 2011')
p.show()

labels = 'Distinction', 'First Class', 'Second Class', 'Fail'
sizes = [adist[2], afc[2], asc[2], afail[2]]
explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = p.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
p.title('Student Marks Analysis of 2012')
p.show()

labels = 'Distinction', 'First Class', 'Second Class', 'Fail'
sizes = [adist[3], afc[3], asc[3], afail[3]]
explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = p.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
p.title('Student Marks Analysis of 2013')
p.show()

labels = 'Distinction', 'First Class', 'Second Class', 'Fail'
sizes = [adist[4], afc[4], asc[4], afail[4]]
explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = p.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
p.title('Student Marks Analysis of 2014')
p.show()

labels = 'Distinction', 'First Class', 'Second Class', 'Fail'
sizes = [adist[5], afc[5], asc[5], afail[5]]
explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = p.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
p.title('Student Marks Analysis of 2015')
p.show()

