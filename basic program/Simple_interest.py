
#phyton program for simple interest 
def simple_interest(p,t,r):
    print('the principal is ',p)
    print('the time period is ', t)
    print('the rate of interest is', r)
    si = (p * t * r)/100
    print('the simple interest is ', si)

    P=int(input("enter the principal amount :"))
    T=int(input("enter the time period :"))
    R=int(input("enter the rate of interest :"))
    simple_interest(P,T,R)