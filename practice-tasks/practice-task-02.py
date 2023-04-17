#1
print("1")
for i in range(3):
    for j in range(5):
        print(" * ", end='')
    print("")
print('\n')
#2
print("2")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 5-1 or j == 0 or j == 5-1:
            print(" * ", end='')
        else:
            print("   ", end='')
    print("")
print('\n')
#3
print("3")
for i in range(4):
    for j in range(5):
        if i == 0 or i == 4-1 or j == 0 or j == 5-1:
            print(" * ", end='')
        else:
            print("   ", end='')
    print("")
print('\n')
#4
print("4")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 5-1 or i == (5-1)/2 or j == 0 or j == 5-1 or j == (5-1)/2:
            print(" * ", end='')
        else:
            print("   ", end='')
    print("")
print('\n')
#5
print("5")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 5-1 or i == j or j == 0 or j == 5-1:
            print(" * ", end='')
        else:
            print("   ", end='')
    print("")
