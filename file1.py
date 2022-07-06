#1
def name_args(**kwargs):
  for k in kwargs.keys():
    print(f"{k}:{kwargs[k]}")
#2
def all_true(iter):
  return all(iter)

print(all_true([True,True,True]))
print(all_true((True, False)))
#3
def one_true(iter):
  return any(iter)

print(one_true([True,True,True]))
print(one_true([False, False, False]))
print(one_true((True, False)))
#4
def recursive_factorial(n):
  if n <= 1:
    return 1
  else:
    return n * recursive_factorial(n-1)

print(recursive_factorial(3))
print(recursive_factorial(6))
#5
#6