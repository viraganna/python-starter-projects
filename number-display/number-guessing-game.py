import time

print("Think of an integer between 1-100 and Computer will guess it in no more than 7 times!")
time.sleep(5)
print("Let Computer know if your number is higher, lower or equal by writing: h, l, e!")
time.sleep(5)

ready = input("Are you ready? (y/n): ")
print("")
if ready != "y" and ready != "n":
    ready = input("Are you ready? (y/n): ")
if ready == "n":
    print("Bye")