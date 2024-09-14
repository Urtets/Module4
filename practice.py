import datetime
import time

from module_4_additional.module_4_practice import bubble_sort, selection_sort, insertion_sort

data_1 = [9, 13, 12, 1, 23, 3, 4, 7]
data_2 = [9, 14, 2, 1, 20, 31, 4, 5]
data_3 = [9, 13, 11, 1, 3, 2, 5, 6]


print(bubble_sort(data_1))
print(bubble_sort(data_2))
print(bubble_sort(data_3))

print(selection_sort(data_1))
print(selection_sort(data_2))
print(selection_sort(data_3))

print(insertion_sort(data_1))
print(insertion_sort(data_2))
print(insertion_sort(data_3))

