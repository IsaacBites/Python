x = int(input())
cont_in = 0
cont_out = 0

for _ in range(x):
    num = int(input())

    if 10 <= num <= 20:
        cont_in += 1
    else:
        cont_out += 1

print(f"{cont_in} in")
print(f"{cont_out} out")