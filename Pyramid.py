2. Pyramid of numbers 1 to 20

n = 20
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(0, n - i):
        print(" ", end=" ")

    # Print numbers in ascending order
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print numbers in descending order
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    # Move to the next line for the next row
    print()