import math

X2 = float(input("X2 Number: "))
X1 = float(input("X1 Number: "))
X0 = float(input("X0 Number: "))
a = X2
b = X1
c = X0
delta = (b * b) - 4 * a * c
print(delta)
if delta > 0:
    print("x1,2")
else:
    print("No, you can't, delta is less than 0")
    exit()
gyok_delta = math.sqrt(delta)
print(f"Root Delta is {gyok_delta}")
x1 = (-b + gyok_delta) / (2 * a)
x2 = (-b - gyok_delta) / (2 * a)
print(f"x1 = {x1}, x2 = {x2}")

prob1 = (math.pow(x1, 2)) + (math.pow(x1, 1)) + c
print(f"x1's probe is {prob1}")
prob2 = (math.pow(x2, 2)) + (math.pow(x2, 1)) + c
print(f"x2's probe is {prob2}")