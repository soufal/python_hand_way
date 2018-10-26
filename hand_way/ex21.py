#21Functions Can Return Something

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACT {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(35, 10)
height = subtract(88, 5)
weight = multiply(22, 4)
iq = divide(22, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, Iq: {iq}")

#A puzzle for the extra credit, type it in anyway
print("here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That become: ", what, "Can you do it by hand?")

my = add(24, subtract(divide(34,100), 1023))
print(f"my result is: ", my)
#print(add(32,2))