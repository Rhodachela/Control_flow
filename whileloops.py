outer_count = 5

while outer_count > 0:
    inner_count = 1

    while inner_count <= outer_count:
        print(inner_count,end= "" )
        inner_count +=1
    print()
    outer_count -= 1


#Multiplication table

for i in range (1, 5):
    for j in range (1, 5):
        product = i * j
        print(f"{i} * {j} = {product}", end="\t")
    print()


rows = 5
for i in range (1, rows+1):
    for j in range (1, i+1):
        print("*", end="")
    print()

rows = 5
for i in range(1, 7):
    print(" " * (rows - i), end="")

    print("* " * i)
