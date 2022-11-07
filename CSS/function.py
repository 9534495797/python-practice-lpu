#defining a fun
#def ac():
  #  print("ANKIT CHAUBEY")
#CALLING FUN
#ac()




#def add(num1,num2):
 #   sum=num1+num2
#    print(sum)
#add(4,7) 












#def sub(num1,num2):
  #  sub=num1-num2
  #  print(sub)
#sub(6,4)











#def multi(num1,num2):
 #   multi=num1*num2
   # return multi
#x=multi(2,5)
#print(x)








#def name(firstname,lastname):
   # print("my name is",firstname +""+lastname )
#name("ankit","chaubey")

#def name(*args):
  #  print(args[2])
#name("ankit","kumar","chaubey")







#def name(name,*args):
 #   print(name)
  #  print(args)
#name("ankit","kumar","chaubey")


a=5  #global
def example():
    global a  #global is keyword
    a=10   #local,internal
    print(a)
example()
print(a)







