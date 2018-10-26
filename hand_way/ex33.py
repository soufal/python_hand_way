#While loop

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

print("This is a function to append list.")

def test(num):
    j = 0
    while j < num:
        print(f"At the top i is {j}")
        numbers.append(j)

        j = j + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {j}")

n = int(input("The number is> "))

test(n)