# Subtask 8.2

s = 0
n = 0
m = float("-inf")

x = int(input("Enter x: "))

while x != -1:
    s = s + x
    n = n + 1

    if x > m:
        m = x

    x = int(input("Enter x: "))

if n > 0:
    a = s / n
    print("s =", s)
    print("n =", n)
    print("m =", m)
    print("a =", a)
else:
    print("s = 0")
    print("n = 0")
    print("m = undefined")
    print("a = undefined")
#it looks like I learned how to use git today
