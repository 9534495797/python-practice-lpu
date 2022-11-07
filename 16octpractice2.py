#take input for 3 sides of triangle and print if possible to  make triangle


x=int(input("write 1st side of triangle="))
y=int(input("write 2nd side of triangle="))
z=int(input("write 3rd side of triangle="))
if x+y>z or y+z>x or z+x>y:
  print("triangle is possible")
else:
    print("not possible")
