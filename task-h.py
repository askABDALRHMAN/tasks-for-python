import math

A = int(input("Enter the first number (A): "))
B = int(input("Enter the second number (B): "))

print("floor", A, "/", B, "=", math.floor(A / B))
print("ceil", A, "/", B, "=", math.ceil(A / B))
print("round", A, "/", B, "=", round(A / B))
