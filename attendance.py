totalclass=int(input("total no. of class="))  

attendclass=int(input("total no. of attendclass=")) 

percentage=(attendclass/totalclass)*100
if  percentage>=75: 

    print("you can sit in exam.") 
else: 
    print("you are not allowed to exam.")    
