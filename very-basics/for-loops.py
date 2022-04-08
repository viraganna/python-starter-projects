
"""
For loops iterate through a certain number of values

numbers = [1,2,3,4,5]
for item in numbers:
    print(item)



nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
   
    

for num in nums:
    if num == 6:
        print("Found it!")
        break
    print(num)




for num in nums:
    if num == 3:
        print("Found it!")
        continue
    print(num)
         


for num in nums:
    for letter in 'abc':
        print(num, letter)
  


for i in range(10):
    print(i)



for i in range(1, 11):
    print(i)


for number in range(1, 10, 2):
    print("Attempt", number, number * '.')
    """

numbers = [2, 5, 6, 1, 7, 22, 33, 11]
for ind, num in enumerate(numbers):
    if (ind % 2 == 0):
        print(num, ind)
