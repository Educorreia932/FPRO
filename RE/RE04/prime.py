n = int(input("Choose an integer number: "))

for i in range(2, n):
    if n % i == 0:
        result = False
        break
    
    else:
        result = True

print(result)
