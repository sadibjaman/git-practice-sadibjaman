from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Sadib")
print("Today's date:", date.today())

print("5 + 3 =", add(5, 3))
print("5 - 3 =", subtract(5, 3))

try:
    print("10 / 2 =", divide(10, 2))
    print("10 / 0 =", divide(10, 0))
except ValueError as e:
    print("Error:", e)