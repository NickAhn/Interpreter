def fizzbuzz(n):
    s = ""
    if n % 3 == 0:
        s += "fizz"
    if n % 5 == 0:
        s += "buzz"

    if s == "":
        print(n)
    else:
        print(s)

for i in range (100):
    fizzbuzz(i)