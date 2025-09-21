size = int(input("Enter the size of the pattern: "))

i=1
while i <= size:
    for j in range(4):
        print("*", end="")
    print()    
    i += 1