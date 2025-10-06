def summation(n):
  if n==1:
    return 1
  else:
    return (n+ summation(n-1))