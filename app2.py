print("welcome to compound interest calculator")
p=int(input("enter the principal amount:"))
r=float(input("enter the rate of interest:"))
t=int(input("enter the time in years:"))
amount=p*(1+r/100)**t
print("The compound interest is:", amount-p ,)

print("welcome to Simple interest calculator")
p=int(input("enter the principal amount:"))
r=float(input ("enter the rate of interest: "))
t=int(input("enter the time in years:"))
si=(p*r*t)/100
print("The simple interest is:", si)
