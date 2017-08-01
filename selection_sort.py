L = [5,4,3,1,2]
def selection_sort(L):
    n = len(L)
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if L[min] > L[j]:
                min = j

        tmp = L[min]
        L[min] = L[i]
        L[i] = tmp
    return L
print(selection_sort(L))
