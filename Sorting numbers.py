count = int(input("enter the number of numbers: "))

S = [0] * count

for i in range(count):
    S[i] = int(input("enter the number: "))

for i in range(count - 1):
    for j in range(count - 1 - i):
        if S[j] > S[j + 1]:
            temp = S[j]
            S[j] = S[j + 1]
            S[j + 1] = temp

print("sorted numbers:")
print(S)
