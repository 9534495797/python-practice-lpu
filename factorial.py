#def fact(n):
   # if n==0:
   #     return  1
   # return n*fact(n-1)
#num=fact(20)
#print(num)

#def sqr(x):
 #   x**=2
 #   print(x)
#sqr(8)

#x=lambda a,b: a*b
#num=x(4,8)
#print(num)

def name(y):
   return lambda a:a+y
num=name(10)
print(num(8))