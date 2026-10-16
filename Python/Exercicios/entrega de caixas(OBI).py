A, B, C = [int(input()), int(input()), int(input())]
if A + B < C:
    print(1)
elif A < B or B < C:
    print(2)
else:
    print(3)