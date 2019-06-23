# Task 3
# 1)what is the digit value of the factorial number?
# Input :  5   output : 3(5! = 120)
# Input :  6   output : 3(6! = 720)
# Input :  7   output : 4(7! = 5040)
# Input :  4   output : 2(4! = 24)
# Input :  3   output : 1(3! =6)


def factorial(input_int):
    if type(input) is not int:
        raise Exception("input should be integer. Given input is % s" % type(input_int))
    elif input_int < 0:
        raise Exception("input should be positive. Given input is % s" % input_int)
    else:
        if input_int == 0:
            return 1
        else:
            return factorial(input_int - 1) * input_int


# 2)Replace the current value with the next large value in an array, if there is no any large value exists
# in an array, so Replace with -1.
# Test Case :
# 1) Input : [2,1,5,2,6,2] .output : [5,5,6,6-1,-1]

# 2) Input :  [2,1,5,2,6,20] . output : [5,5,6,6-20,-1]

# 3) Input :  [22,1,5,2,6,20] . output : [-1,-1,-1,1,-1,-1]

# 4) Input :  [0,1,5,2,6,20] . output : [1, 5, 6, 6, 20, -1]

# 5) Input :  [100,111,115,222,666,777] . output : [111,115,222,666,777,-1]

def arr_next_large(arr):
    arr_len = len(arr)
    if arr_len == 1:
        return [-1]
    elif arr_len == 0:
        return []
    else:
        for item in arr:
            if type(item) is not int:
                raise Exception("input should be integer. Given input is % s" % type(item))
        result = [None] * arr_len
        for i in range(0, arr_len):
            if i == arr_len - 1:
                result[i] = -1
            for j in range(i+1, arr_len):
                if arr[i] < arr[j]:
                    result[i] = arr[j]
                    break
                else:
                    result[i] = -1
        return result
