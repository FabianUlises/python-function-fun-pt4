#1
def max_num(a, b, c):
    return max([a, b, c])
print(max_num(1, 2, 3));

#2
def mult_list(list) :
    res = 1
    for x in list:
        res = res * x
    return res
list1 = [2, 3, 4]
print(mult_list(list1))

#3
def rev_string(str):
    return str[::-1]
print(rev_string("bonjour"))

#4
def num_within(x, a, b):
  return x in range(a, b + 1)
print(num_within(10, 2, 5))

#5
def pascal(n):
   for i in range(n + 1):
      for j in range(n - i):
         print(' ', end = '')

      C = 1
      for j in range(1, i + 1):
         print(C, ' ', sep = '', end = '')
         C = C * (i - j) // j
      print()

n = 5
pascal(n)