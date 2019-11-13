# input : n, arr1, arr2
def solution(n, arr1, arr2):
    for idx, _ in enumerate(arr1):
        arr1[idx] = tentotwo(arr1[idx], n)
        arr2[idx] = tentotwo(arr2[idx], n)
    print(arr1)
    print(arr2)
    arr3 = list()
    for idx in range(n):
        arr3.append("")
        for jdx in range(n):
            if arr1[idx][jdx] or arr2[idx][jdx]:
                arr3[idx] = arr3[idx]+"#"
            else:
                arr3[idx] = arr3[idx]+" "
    print(arr3)

    return 0

def tentotwo(input, n):
    result = list()
    for i in range(n):
        input, a = divmod(input, 2)
        result.insert(0, a)
    return result

n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
solution(n, arr1, arr2)
