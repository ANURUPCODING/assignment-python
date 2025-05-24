n=int(input("Enter the number of terms: "))
a,b=0,1
count=0 
print(f"Fibonacci series upto {n} terms is: ")
while count<n :
    print(a)
    a,b=b,a+b
    count=count+1