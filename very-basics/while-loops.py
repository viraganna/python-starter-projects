"""
While loops keep going until a certain condition is met
"""


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
