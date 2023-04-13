def MedianOfArrays():
    nums1 = [1, 2]
    nums2 = [3, 4]
    
    mergedArrays = nums1 + nums2
   
    answer = GetMedian(mergedArrays)
    print('Returned answer: ' + str(answer))



def GetMedian(concatArray):
    """
    This function accesses the middle of the array by its index via dividing the total length of the array.
    The median is returned by gettng the middle of the sorted array and dividing it by two.
    """
    arrayLen = len(concatArray)

    # If Array is even. Grabs first element by reducing index by -1, then gets the second element and concatentates them together
    if arrayLen % 2 == 0:
        middleOfArray = (concatArray[(len(concatArray) -1) // 2] + concatArray[len(concatArray) // 2]) / 2


    # If Array is odd (remainder == 1)
    elif arrayLen % 2 == 1:
        middleOfArray = concatArray[len(concatArray) // 2]


    else:
        print('Empty array provided!')
        exit()
       

    return middleOfArray

MedianOfArrays()