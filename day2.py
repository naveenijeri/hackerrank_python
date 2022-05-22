import copy 
def min_max(test_lst):
    min_list = copy.deepcopy(test_lst)
    max_list = copy.deepcopy(test_lst)
    min_sum = 0
    max_sum = 0
    for i in range(len(min_list)-1):
        min_val = min(min_list)
        min_list.remove(min_val)
        min_sum += min_val
    for i in range(len(max_list)-1):
        max_val = max(max_list)
        max_list.remove(max_val)
        max_sum += max_val
    print(min_sum,"",max_sum)





test_lst =[1,2,3,4,5]
min_max(test_lst)
# print("minimum of a list is {}".format(min(test_lst)))
# print("maximum of a list is {}".format(max(test_lst)))