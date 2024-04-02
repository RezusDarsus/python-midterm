# 1. A
# 2. C
# 3. B
# 4. C
#2
def numAverage(*nums):
    if not nums:
        return None

    total = sum(nums)
    return  total/len(nums)


print(numAverage())
#3
def oddChechk(lst):
    odd = filter(lambda x: x % 2 == 1 , lst)
    return  all(map(lambda  x : x > 15   , odd))

print(oddChechk([123,123124,1245,1]))

#4
def almostMax(lt):
    max_value = second_value = None
    for i in lt:
        if max_value is None or i >= max_value:
            second_value , max_value = max_value , i
        elif second_value is None or (i > second_value and i != max_value):
            second_value = i
    return second_value

print(almostMax([1,5,2,1,3,3]))

#5
def leapYearCount(start_year):
    storage = 0
    for z in range(start_year , 2025):
        if(z % 400 == 0) or (z % 4 == 0 and z % 100 != 0):
            storage = storage  + 1
            i = storage

    return i
print(leapYearCount(1121))
