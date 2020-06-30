print("Please enter an amount in cents less than a dollar.")
a = int(input())
valQ, remainderQ = int(a/25), a%25
valD, remainderD = int(remainderQ/10), remainderQ%10
valN, remainderN = int(remainderD/5), remainderD%5
valP = remainderN
print("Your change will be:")
print("Q: ", valQ)
print("D: ", valD)
print("N: ", valN)
print("P: ", valP)