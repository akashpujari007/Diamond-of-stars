n = int(input())
i = 1
n1 = (n + 1) // 2
n2 = n // 2
while i <= n1:
    spaces = 1
    while spaces <= n1- i:
        print(' ', end='')
        spaces = spaces + 1
    stars = 1
    while stars <= 2*i - 1:
        print('*', end='')
        stars = stars + 1
    print()
    i = i + 1
i = n2
while i >= 1:
  spaces = 1
  while spaces <= (n2 - i + 1):
    print(' ', end='')
    spaces = spaces + 1
  j = 1
  while j <= (2*i - 1):
    print('*', end='')
    j = j + 1
  print()
  i = i - 1
  
  