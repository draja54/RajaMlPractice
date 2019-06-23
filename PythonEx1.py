import sys


# 1) Reverse String
# I/p : rakesh kumar   o/p : ramuk hsekar
# i/p : deep  learn o/p : nrael peed


def reverse_string(str):
    str_out = ''
    for c in str:
        str_out = c + str_out  # appending chars in reverse order
    return str_out


rev_string1 = 'rakesh kumar'
rev_output_string1 = reverse_string(rev_string1)
print(rev_output_string1)
rev_string2 = 'deep  learn'
rev_output_string2 = reverse_string(rev_string2)
print(rev_output_string2)


# 2) Reverse String
# I/p : rakesh kumar   o/p : hsekar ramuk
# i/p : deep  learn o/p : peed nrael


def reverse_each_word(str):
    temp_str = str.split()
    str_output = ''
    for item in temp_str:
        str_output = str_output + reverse_string(item) + ' '
    return str_output.rstrip()


rev_word_string1 = 'rakesh kumar'
rev_word_output_string1 = reverse_each_word(rev_word_string1)
print(rev_word_output_string1)
rev_word_string2 = 'deep  learn'
rev_word_output_string2 = reverse_each_word(rev_word_string2)
print(rev_word_output_string2)


# 3) Sorting ascending a number
# I/p : [3,9,2,5,90,3,2]  o/p : [2,2,3,3,5,9,90]
# i/p : [4,9,3,5,0,9,4] o/p : [0,3,4,4,5,9,9]


def list_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):

            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


input_lst1 = [3, 9, 2, 5, 90, 3, 2]
output_lst1 = list_sort(input_lst1)
print(output_lst1)
input_lst2 = [4, 9, 3, 5, 0, 9, 4]
output_lst2 = list_sort(input_lst2)
print(output_lst2)

# 4) Sorting descending a number
# I/p : [3,9,2,5,90,3,2]  o/p : [2,2,3,3,5,9,90]
# i/p : [4,9,3,5,0,9,4] o/p : [0,3,4,4,5,9,9]


def list_sort_desc(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):

            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


input_desc_lst1 = [3, 9, 2, 5, 90, 3, 2]
output_desc_lst1 = list_sort_desc(input_desc_lst1)
print(output_desc_lst1)
input_desc_lst2 = [4, 9, 3, 5, 0, 9, 4]
output_desc_lst2 = list_sort_desc(input_desc_lst2)
print(output_desc_lst2)

# 5) Print 2nd smallest number
# I/p : [3,9,2,5,90,3,2]  o/p : 2
# i/p : [9,3,5,9,4] o/p : 3


def second_smallest(lst):
    if len(lst) < 2:
        return 0
    else:
        first = second = sys.maxsize
        for index in range(0, len(lst)):
            if lst[index] < first:
                second = first
                first = lst[index]
            elif lst[index] < second and lst[index] != first:
                second = lst[index]
        if second == sys.maxsize:
            return 0
        else:
            return second


def second_smallest2(lst):
    if len(lst) < 2:
        return 0
    else:
        return list_sort(lst)[1]


second_smallest_input1 = [3, 9, 2, 5, 90, 3, 2]
second_smallest_output1 = second_smallest(second_smallest_input1)
print(second_smallest_output1)

second_smallest_input2 = [9, 3, 5, 9, 4]
second_smallest_output2 = second_smallest(second_smallest_input2)
print(second_smallest_output2)


second_smallest_output3 = second_smallest2(second_smallest_input1)
print(second_smallest_output3)

second_smallest_output4 = second_smallest2(second_smallest_input2)
print(second_smallest_output4)

# 6) Print 2nd largest number
# I/p : [3,9,2,5,90,3,80,81,2]  o/p : 81
# i/p : [14,9,3,5,15,9,4] o/p : 14


def second_largest(lst):
    if len(lst) < 2:
        return 0
    else:
        first = second = -(sys.maxsize - 1)
        for index in range(0, len(lst)):
            if lst[index] > first:
                second = first
                first = lst[index]
            elif lst[index] > second and lst[index] != first:
                second = lst[index]
        if second == -(sys.maxsize - 1):
            return 0
        else:
            return second


def second_largest2(lst):
    if len(lst) < 2:
        return 0
    else:
        return list_sort_desc(lst)[1]


second_largest_input1 = [3, 9, 2, 5, 90, 3, 80, 81, 2]
second_largest_output1 = second_largest(second_largest_input1)
print(second_largest_output1)

second_largest_input2 = [14, 9, 3, 5, 15, 9, 4]
second_largest_output2 = second_largest(second_largest_input2)
print(second_largest_output2)


second_largest_output3 = second_largest2(second_largest_input1)
print(second_largest_output3)

second_largest_output4 = second_largest2(second_largest_input2)
print(second_largest_output4)


# 7) remove duplicate number
# I/p : [1,9,2,3,4,6,8,1,2,3,6]  o/p :[1,9,2,3,4,6]
# i/p : [5,4,6,1,1,1,2,1,2,3] o/p : [5,4,6,1,2,3]


def remove_duplicate(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


duplicate_input1 = [1, 9, 2, 3, 4, 6, 8, 1, 2, 3, 6]
duplicate_output1 = remove_duplicate(duplicate_input1)
print(duplicate_output1)

duplicate_input2 = [5, 4, 6, 1, 1, 1, 2, 1, 2, 3]
duplicate_output2 = remove_duplicate(duplicate_input2)
print(duplicate_output2)

# 8) reverse the list
# I/p : ["b" ,"a","c","d"]   o/p :["d" ,"c","a","b"]
# i/p : ["a" ,"a","r","d"]  o/p : ["d" ,"r","a","a"]


def reverse_list(lst):
    return lst[::-1]


def reverse_list2(lst):
    length = len(lst)
    result = [None] * length
    for i in range(length):
        result[i] = lst[length-1-i]
    return result


reverse_input1 = ["b", "a", "c", "d"]
reverse_output1 = reverse_list(reverse_input1)
print(reverse_output1)

reverse_input2 = ["a", "a", "r", "d"]
reverse_output2 = reverse_list(reverse_input2)
print(reverse_output2)

reverse_output3 = reverse_list2(reverse_input1)
print(reverse_output3)

reverse_output4 = reverse_list2(reverse_input2)
print(reverse_output4)

# 9) remove duplicate from the list
# I/p : ["b" ,"a","c","d","a","c","k"]   o/p :["b" ,"a","c","d","k"]
# i/p : ["a" ,"a","r","d","r"]  o/p :  ["a" ,"r","d"]
# remove_duplicate method works for characters as well

str_duplicate_input1 = ["b", "a", "c", "d", "a", "c", "k"]
str_duplicate_output1 = remove_duplicate(str_duplicate_input1)
print(str_duplicate_output1)

str_duplicate_input2 = ["a", "a", "r", "d", "r"]
str_duplicate_output2 = remove_duplicate(str_duplicate_input2)
print(str_duplicate_output1)

# 10) Print the String in order
# I/p : a2bMA@3H1h   o/p : AHMabh123@
# i/p : 1D@DA1ab21ba . o/p : ADDaabb112@


def string_sort(str_input):
    lst_caps = []
    lst_small = []
    lst_num = []
    lst_special = []
    for i in range(len(str_input)):
        if ord(str_input[i]) in range(ord('A'), ord('Z')+1):
            lst_caps.append(str_input[i])
        elif ord(str_input[i]) in range(ord('a'), ord('z')+1):
            lst_small.append(str_input[i])
        elif ord(str_input[i]) in range(ord('0'), ord('9')+1):
            lst_num.append(str_input[i])
        else:
            lst_special.append(str_input[i])
    lst_char = list_sort(lst_caps) + list_sort(lst_small) + list_sort(lst_num) + list_sort(lst_special)
    return ''.join(lst_char)


string_sort_input1 = "a2bMA@3H1h"
string_sort_output1 = string_sort(string_sort_input1)
print(string_sort_output1)

string_sort_input2 = "1D@DA1ab21ba"
string_sort_output2 = string_sort(string_sort_input2)
print(string_sort_output2)

# 11) Print the String in order and remove duplicated
# I/p : aB3c1D$A9A1$d3   o/p : ABDacd139$
# i/p : Lg@32aH23 o/p : HLag23@


def string_sort_dup(str_input):
    lst_caps = []
    lst_small = []
    lst_num = []
    lst_special = []
    for i in range(len(str_input)):
        if ord(str_input[i]) in range(ord('A'), ord('Z')+1):
            lst_caps.append(str_input[i])
        elif ord(str_input[i]) in range(ord('a'), ord('z')+1):
            lst_small.append(str_input[i])
        elif ord(str_input[i]) in range(ord('0'), ord('9')+1):
            lst_num.append(str_input[i])
        else:
            lst_special.append(str_input[i])
    lst_char = (list_sort(remove_duplicate(lst_caps)) + list_sort(remove_duplicate(lst_small)) +
               list_sort(remove_duplicate(lst_num)) + list_sort(remove_duplicate(lst_special)))
    return ''.join(lst_char)


string_sort_dup_input1 = "aB3c1D$A9A1$d3"
string_sort_dup_output1 = string_sort_dup(string_sort_dup_input1)
print(string_sort_dup_output1)

string_sort_dup_input2 = "Lg@32aH23"
string_sort_dup_output2 = string_sort_dup(string_sort_dup_input2)
print(string_sort_dup_output2)
