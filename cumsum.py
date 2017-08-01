def cumsum(L,l,r):
    sum = 0
    for i in range(l,r):
        sum += L[i]
    return sum
print(cumsum([1,2,5,6],2,4))
