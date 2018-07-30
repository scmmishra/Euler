import sys
n = 2
LIMIT = 1000000
size_list = [0] * LIMIT

def update(number):
  if number%2==0:
    return int(number/2)
  else:
    return 3*number+1

def check(number):
  if size_list[number] != 0:
    return size_list[number]

def count(number):
  size = 0
  while True:
    if number < LIMIT and check(number):
      size = size + check(number)
      return size
    elif number == 1:
      size = size + 1
      return size
    else:
      number = update(number)
      size = size + 1

# for iterating from 1 to a million
for ii in range (3, LIMIT):
  size_list[ii] = count(ii)

print(size_list.index(max(size_list)))
