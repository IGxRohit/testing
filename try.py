i=(input("Enter Number for table:"))
print(f"table of {i}:")
try:
        a=1
        while a<=10:
            print(f"{int(i)} X {a} ={int(i)*a} ")
            a=a+1
# except Exception as e:
#       print(e)
except ValueError:
      print("please Enter Number only")

finally:
      print("ENJOY")

#testing of file handlingtesting file handling