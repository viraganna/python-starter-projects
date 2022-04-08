"""
While loops keep going until a certain condition is met
"""


from operator import countOf


i = 1
while i <= 10:
    print(i * "n")
    i = i + 1
    

x = 0
while x < 10:
    print(x)
    x += 1
  


x = 0
while x < 10:
    if x == 5:
        print("Found it!")
        break
    print(x)
    x += 1

numbers = [2, 5, 6, 1, 7, 22, 33, 11]
ind = 0
while ind < len(numbers):
    if (ind % 2 == 0):
        print(numbers[ind], ind)
    ind += 1