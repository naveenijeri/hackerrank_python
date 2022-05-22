'''Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.'''

import time
#Normal approach

def plus_minus_zero(arr):
    start_time = time.time()
    length_arr = len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for ele in arr:
        if ele==0:
            zero_count+=1
        if ele>0:
            positive_count+=1
        if ele<0:
            negative_count+=1
    print("{:.6f}".format(positive_count/length_arr))
    print("{:.6f}".format(negative_count/length_arr))
    print("{:.6f}".format(zero_count/length_arr))
    end_time = time.time()
    print("time taken by normal approach is{}".format(end_time-start_time))


arr = [1,2,3,0,0,-1,-2,-3]
plus_minus_zero(arr)


#using python lambda function
start_time = time.time()
arr = [1,2,3,0,0,-1,-2,-3]
length_arr = len(arr)
positive_count = len(list(filter(lambda x:(x>0),arr)))
negative_count = len(list(filter(lambda x:(x<0),arr)))
zero_count = len(list(filter(lambda x:(x==0),arr)))
print("{:.6f}".format(positive_count/length_arr))
print("{:.6f}".format(negative_count/length_arr))
print("{:.6f}".format(zero_count/length_arr))
end_time = time.time()
print("time taken by lambda approach:{}".format(end_time-start_time))


#using the Class
class PlusMinusZero:
    def __init__(self,arr):
        self.arr = arr
    
    def positive_negative_count(self):
        positive_count = len(list(filter(lambda x:(x>0), self.arr)))
        negative_count = len(list(filter(lambda x:(x<0), self.arr)))
        zero_count = len(list(filter(lambda x:(x==0), self.arr)))
        positive_ratio = positive_count/len(self.arr)
        negative_ratio = negative_count/len(self.arr)
        zero_ratio = zero_count/len(self.arr)
        print("{:.6f}".format(positive_ratio))
        print("{:.6f}".format(negative_ratio))
        print("{:.6f}".format(zero_ratio))

p=PlusMinusZero([1,2,3,0,0,-2,-3])
p.positive_negative_count()

    
    
    

        