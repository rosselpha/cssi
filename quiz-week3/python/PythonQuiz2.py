def smallestNumber(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    elif n3 >= n1 and n3 >= n2:
        return n3

print(smallestNumber(0,90,3))

print(max(2,3,4))
