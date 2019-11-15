def findMedianSortedArrays(a, n, b, m):
    min_index = 0
    max_index = n

    while (min_index <= max_index):
        i = (min_index + max_index) // 2
        j = ((n + m + 1) // 2) - i

        if (i < n and j > 0 and b[j - 1] > a[i]):
            min_index = i + 1

        elif (i > 0 and j < m and b[j] < a[i - 1]):
            max_index = i - 1

        else:
            if (i == 0):
                return b[j - 1]
            if (j == 0):
                return a[i - 1]
            else:
                return max(a[i - 1], b[j - 1])
    print("ERROR!!! ", "returning\n")
    return 0

a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
b = [1, 23, 25]
n = len(a)
m = len(b)

if (n < m):
    print("The median is: ", findMedianSortedArrays(a, n, b, m))
else:
    print("The median is: ", findMedianSortedArrays(b, m, a, n))

