# 1 find the mean from list or value
import math as m
import statistics
from scipy import stats
# from sklearn import preprocessing

# Helper Method we did im Ex1


def list_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):

            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


def lst_mean(lst):
    if len(lst) > 0:
        return sum(lst) / len(lst)
    else:
        return


# 2 find the median from list or value


def lst_median(lst):
    lst_length = len(lst)
    half_length = lst_length // 2
    lst = list_sort(lst)
    if lst_length > 0:
        if lst_length % 2 == 1:

            return lst[half_length]
        else:
            return (lst[half_length - 1] + lst[half_length]) / 2
    else:
        return


# 3 find the mode from list or value


def lst_mode(lst):
    max_count = 0
    mode = []
    for item in lst:
        if item in mode:
            continue
        count = lst.count(item)
        if count > max_count:
            del mode[:]
            mode.append(item)
            max_count = count
        elif count == max_count:
            mode.append(item)
    if len(mode) == 1:
        return mode[0]
    return


# 4 find the variance from list or value


def lst_variance(lst):
    mean_value = lst_mean(lst)
    lst_length = len(lst)
    if lst_length > 0:
        total = 0
        for item in lst:
            total = total + (item-mean_value)**2
        return total/lst_length
    else:
        return


# 5 find the co-variance from list_x and  list_y


def lst_covariance(lst_x, lst_y):
    if len(lst_x) == len(lst_y):
        mean_x = lst_mean(lst_x)
        mean_y = lst_mean(lst_y)
        cov_sum = 0
        for item in range(0, len(lst_x)):
            cov_sum = cov_sum + ((lst_x[item] - mean_x)*(lst_y[item] - mean_y))
        return cov_sum/(len(lst_x)-1)
    return


# 6 find the normalization from list


def lst_normalize(lst):
    norm_lst = [None] * len(lst)
    lst_sum = sum(lst)
    for item in range(0, len(lst)):
        norm_lst[item] = lst[item] / lst_sum
    return norm_lst


# 7 find the z-score or z-value or z-standard from list

def z_score(lst):
    if len(lst) > 0:
        z_mean = lst_mean(lst)
        z_sd = m.sqrt(lst_variance(lst))
        z_sum = 0
        for item in lst:
            z_sum = z_sum + (item - z_mean)
        return z_sum/z_sd
    return


lst_input1 = [1, 5, 6, 1, 1, 2]
lst_input2 = [5, 6, 7, 8, 9]
lst_input3 = [20, 24, 28, 32, 36]
lst_input4 = [2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7]
lst_input5 = []

print("Values from our methods:")
print("Input1:")
print("mean: % s" % lst_mean(lst_input1))
print("median: % s" % lst_median(lst_input1))
print("mode: % s" % lst_mode(lst_input1))
print("variance: % s" % lst_variance(lst_input1))
print("normalize: % s" % lst_normalize(lst_input1))
print("Z-score: % s" % z_score(lst_input1))

print("Values from System methods:")
print("Input1:")
print("mean: % s" % statistics.mean(lst_input1))
print("median: % s" % statistics.median(lst_input1))
print("mode: % s" % statistics.mode(lst_input1))
print("variance: % s" % statistics.variance(lst_input1))
# print("normalize: % s" % preprocessing.normalize(lst_input1))
print("Z-score: % s" % stats.zscore(lst_input1))


print("Values from our methods:")
print("Input2:")
print("mean: % s" % lst_mean(lst_input2))
print("median: % s" % lst_median(lst_input2))
print("mode: % s" % lst_mode(lst_input2))
print("variance: % s" % lst_variance(lst_input2))
print("normalize: % s" % lst_normalize(lst_input2))
print("Z-score: % s" % z_score(lst_input2))

print("Values from System methods:")
print("Input2:")
print("mean: % s" % statistics.mean(lst_input2))
print("median: % s" % statistics.median(lst_input2))
# print("mode: % s" % statistics.mode(lst_input2))
print("variance: % s" % statistics.variance(lst_input2))
# print("normalize: % s" % preprocessing.normalize(lst_input2))
print("Z-score: % s" % stats.zscore(lst_input2))

print("Values from our methods:")
print("Input3:")
print("mean: % s" % lst_mean(lst_input3))
print("median: % s" % lst_median(lst_input3))
print("mode: % s" % lst_mode(lst_input3))
print("variance: % s" % lst_variance(lst_input3))
print("normalize: % s" % lst_normalize(lst_input3))
print("Z-score: % s" % z_score(lst_input3))

print("Values from System methods:")
print("Input3:")
print("mean: % s" % statistics.mean(lst_input3))
print("median: % s" % statistics.median(lst_input3))
# print("mode: % s" % statistics.mode(lst_input3))
print("variance: % s" % statistics.variance(lst_input3))
# print("normalize: % s" % preprocessing.normalize(lst_input3))
print("Z-score: % s" % stats.zscore(lst_input3))

print("Values from our methods:")
print("Input4:")
print("mean: % s" % lst_mean(lst_input4))
print("median: % s" % lst_median(lst_input4))
print("mode: % s" % lst_mode(lst_input4))
print("variance: % s" % lst_variance(lst_input4))
print("normalize: % s" % lst_normalize(lst_input4))
print("Z-score: % s" % z_score(lst_input4))

print("Values from System methods:")
print("Input4:")
print("mean: % s" % statistics.mean(lst_input4))
print("median: % s" % statistics.median(lst_input4))
print("mode: % s" % statistics.mode(lst_input4))
print("variance: % s" % statistics.variance(lst_input4))
# print("normalize: % s" % preprocessing.normalize(lst_input4))
print("Z-score: % s" % stats.zscore(lst_input4))

print("Values from our methods:")
print("Input5:")
print("mean: % s" % lst_mean(lst_input5))
print("median: % s" % lst_median(lst_input5))
print("mode: % s" % lst_mode(lst_input5))
print("variance: % s" % lst_variance(lst_input5))
print("normalize: % s" % lst_normalize(lst_input5))
print("Z-score: % s" % z_score(lst_input5))

print("Values from System methods:")
print("Input5:")
print("mean: % s" % statistics.mean(lst_input5))
print("median: % s" % statistics.median(lst_input5))
print("mode: % s" % statistics.mode(lst_input5))
print("variance: % s" % statistics.variance(lst_input5))
# print("normalize: % s" % preprocessing.normalize(lst_input5))
print("Z-score: % s" % stats.zscore(lst_input5))
