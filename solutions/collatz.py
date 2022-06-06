def collatz(n):
  store = []
  while n!=1:
    if n%2 == 0:
      n = n //2
      store.append(n)
    else:
      n =  (n * 3)+1
      store.append(n)
 return store
    
