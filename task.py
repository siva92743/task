a = int(input("bottom num : "))
b = int(input("top num : "))

matrix = [
    [1 for x in range(b)]
    for y in range(a)
]
count = 1
for y in range(a):
    for x in range(b):
        matrix[y][x] = count
        count += 1

for y in range(a):
    for x in range(b):
        print(matrix[y][x], end=" ")
    print()