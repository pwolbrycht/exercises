def factorial(n):
    answer = 0
    if int(n) == 0 or int(n) == 1:
        answer = 1
    else:
        answer = factorial(int(n)-1)*int(n)
    return answer

def f(n):
    sumOfFactorials = 0
    for i in str(n):
        currentFactorial = factorial(i)
        sumOfFactorials += currentFactorial
    return sumOfFactorials

def sf(sumOfFactorials):
    sumOfNumbers = 0
    for i in str(sumOfFactorials):
      sumOfNumbers += int(i)
    return sumOfNumbers
        
def g(sumOfNumbers):
  i = 1
  while True:
    if sf(f(i)) == sumOfNumbers:
      return i
      break
    else:
      i += 1

def sg(i):
  minPositiveInteger = g(i)
  print(minPositiveInteger)
  answer = 0
  for i in str(minPositiveInteger):
    answer += int(i)
  return answer

numOfQueries = input()
currentAnswer = 0

for i in range(int(numOfQueries)):
  currentQuery = input()
  currentList = currentQuery.split()
  n = currentList[0]
  m = currentList[1]
  for j in range(1, int(n)+1):
    print("Waiting...")
    currentAnswer += int(sg(n)) % int(m)
  print(currentAnswer)
