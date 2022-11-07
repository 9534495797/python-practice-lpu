#create a function that will take two arugments,nameand age and print their values

#def ac(*args):
   # print(args)
#ac("ankit age is",20) 


#def ac(*args):
  #  for j in range(len(args)):
  #    print(args[j])
#ac(1,2,3,4,5,6,7,8,9)


#def name(firstname="roy",age=20):
 #   print("my name is "+firstname,"my age is",age)
#name("ankit")
#name("rdbsj",25)


#crreate a function using this condition
#it should accept employ name and salary and display
#if salary is missing in function assign the default value 10000 to salary
#ben(9000)mike(15000)bob()

def ac(name,salary=10000):
    print(name,salary)
ac("name","salary")
ac("ben",9000)
ac("mike",15000)
ac("bob")