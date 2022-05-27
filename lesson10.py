#
a =str(input("enter the firstnumber"))
d=(input("enter the common difference"))
n=(input("number of terms"))


for i in range (1,n+1):
    n_terms = a +( i -1)*d
    print(n_terms)

    sum_n = (n_terms/2)*(2*a +(n-1)*d)
    print(sum_n)

