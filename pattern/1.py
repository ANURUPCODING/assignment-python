rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(1,rows+1):
    for j in range(1,cols+1):
        print("*", end="")
    print()
    
    
    # end="" ->so that no new line...warna default in python new line hota hain
    #  print() for new line
 