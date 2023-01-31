import time

def fib(n):
   starting_time = time.time() 
   fi = [0] * (n+1) 
   fi[1] = 1
   for i in range (2,n+1): 
      fi[i] = fi[i-1] + fi[i-2] 
   end_time = time.time() 
   executiontime = end_time - starting_time
   return fi[n], executiontime

n = int(input("Input an integer from 15 to 35: "))
fibvalue,_ = fib(n)
_,executiontime = fib(n)
print(f"fib({n})=",fibvalue, end='\n')
print(f"fib({n}) took",executiontime, "seconds")

