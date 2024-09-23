# Dylan Stitt
# Unit 2 Lab 1
# Mul. Table

table = [i*j for i in range(1, 11) for j in range(1, 11)]
for i, num in enumerate(table):
    if i % 10 == 0: print()
    print(num, end="\t")
