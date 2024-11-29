#simple Interest

def simple_interest(p,n,r):
    i=(p*n*r)/100
    amt=p+i
    return{"interest": i,"Amount": amt}

p=float(input("Please enter principle in INR: "))
n=int(input("Please enter number of years: "))
r=float(input("Please Enter rate of interest"))

results=simple_interest(p,n,r)

print(results)