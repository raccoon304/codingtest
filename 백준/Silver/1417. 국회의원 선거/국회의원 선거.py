n = int(input())
dasom = int(input())
if n <= 1 :
  print(0)
else :
  others = []
  for _ in range(n-1) :
    others.append(int(input()))

  result = 0
  while max(others) >= dasom :
    data = others.index(max(others))
    dasom += 1
    others[data] -=1
    result += 1

  print(result)