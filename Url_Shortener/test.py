def arrEnteros(arr1, arr2):
    n = len(arr1)+len(arr2)
    arr3 = [0]*n
    i = j = k = 0

    while (i<len(arr1) and j<len(arr2)):
        if (arr1[i]<arr2[j]):
            arr3[k]=arr1[i]
            i+=1
            k+=1
        else:
            arr3[k]=arr2[j]
            j+=1
            k+=1

    while (i<len(arr1)):
        arr3[k]=arr1[i]
        i+=1
        k+=1

    while (j<len(arr2)):
        arr3[k]=arr2[j]
        j+=1
        k+=1

    return arr3

arr1 = [3, 4, 9, 9, 17, 20]
arr2=[8, 9, 40, 41]

arr=arrEnteros(arr1,arr2)
print(arr)
