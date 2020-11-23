def my_power(func):
   def innerFunc(n):
      return func(n) ** 2
   return innerFunc