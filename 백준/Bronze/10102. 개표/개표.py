A = int(input())
B = input()

B_a = B.count('A')
B_b = B.count('B')
if (B_a > B_b):
    print("A")
elif (B_a < B_b):
    print("B")
else:
    print("Tie")