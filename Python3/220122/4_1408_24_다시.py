h1,m1,s1=map(int,input().split(':'))
h2,m2,s2=map(int,input().split(':'))
T=3600*(h2-h1)+60*(m2-m1)+(s2-s1)
if T<0:
    T+=60*60*24
h=T//3600
m=(T%3600)//60
s=T%60
print('%02d:%02d:%02d'%(h,m,s))
