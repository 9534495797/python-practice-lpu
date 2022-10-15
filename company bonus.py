#company will give bonus based on following criteria 
#time spent in company               bonus 

#greaterbthan 10 years          10% 
#more than 6 and less than 10     8% 
#less than 6                       5% 

#ask sallary and time spent fro user 
#print net bonus ammount accordingly  


salary=int(input("write the salary=")) 
timespent=int(input("write timespent=")) 

if timespent>10: 
    bonus=10/100*salary
     print("your bonus is",salary+bonus) 
elif timespent>6 and timespent<10: 
    bonus=6/100*salary
     print("your bonus is", salary+8%) 
e