def fib(a,b,n):
  if(n>0):
    print(a+b)
    fib(b,a+b, n-1)

fib(0,1,20)
