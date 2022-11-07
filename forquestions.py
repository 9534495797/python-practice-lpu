#def count(listofnum):
 #   even=0
   # odd=0
   # for i in listofnum:
    #    if i % 2 ==0:
    #        even+=1
    #    else:
    #        odd+=1
    #return even,odd

#x=[32,21,64,100,13]
#even,odd=count(listofnum)
#print(even)
#print(odd)




def name(*ac):
    a=0
    b=0
    for i in ac:
        if len(i)>5:
            print(i)
            a+=1
        else:
            b+=1
    print("items having leength morebthan 5:",a)
    print("items having length less than or equal to 5:",b)

name("atul","shubham","anurag","rahul","dev","roy")

