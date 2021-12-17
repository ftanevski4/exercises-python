

def rotLeft(a, d):
    temp = []
    i = 0
    while i < d:
        temp.append(a[i])
        i += 1
    i = 0
    while d < len(a):
        a[i] = a[d]
        i = i+1
        d = d+1
    a[:] = a[:i] + temp

    print(a)


rotLeft([1, 2, 3, 4, 5], 4)


# Function to left rotate arr[] of size n by d*/
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

# Function to left Rotate arr[] of size n by 1*/


def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp


# utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")
