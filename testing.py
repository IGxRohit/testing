# i=int(input("enter 1st number:"))
# j=int(input("enter 2nd number"))
# print("choice\n1.add\n2.sub\n3.mul\n4.div.\n5.mod")
# choice=int(input("enter your choice"))
# if choice==1:
#   print(i,"+",j,"=",i+j)
# elif choice==2:
#   print(i-j)
# elif choice==3:
#   print(i*j)
# elif choice==4:
#   print(i/j)
# elif choice==5:
#   print(i%j)
# else:
#   print("wrong option entered")


# l=[2,3,4,6,7]
# l2=[4,5,6,4,1,2,7]

# print(l.extend(l2))
# print(l)


# tpl=(2,3,4,5,6)
# tpl1=(3,4,5,6)
# print(tpl.index(3))
# print(tpl)

# se={2,3,4,5,1,2,3,3,3}
# s={"Rohit",6}
# print(se.add(9))
# print(se)

# d={"name":"Rohit"}
# print(d)



# # Fraction solution

# # n=(input("Enter number for fraction:"))
# # print(f"Fraction of {n} ")

# def fr(n):
#   if n==0 or n==1:
#       return 1
#   else: 
#     a=n*fr(n-1)
#     return a

# a=fr(3) 
# print(a)

# file handling

# F=open("try.py",'r')
# print(F.read())


# f=open("try.py",'w')
# f.write("#testing of file handling")#overwrite the file
# f.close()

# f=open("try.py",'a')
# f.write("#testing of file handling")
# f.close()




# f=open("try.py",'a')
# f.write("testing file handling")
# f.close()




#lamda function: small anonymass function
#lamda arguments:expression,parameters


# a=lambda x: x**2
# print(a(5))


# def square(fx,value):
#     return fx(value)

# print(square(lambda x: x**2,5))


# #map-applies function on each element
# l=[1,2,3,4,5,6,7]
# newl=list(map(lambda x:x**2,l))
# print(newl)


# # filter- apllies function on filter elements
# newlf=list(filter(lambda x:x%2!=0,l))
# print(newlf)

# # reduce- takes two arguments and gives a single value-----from functools import reduce is important

# from functools import reduce

# newlr=reduce(lambda x,y:x*y,l)
# print(newlr)

