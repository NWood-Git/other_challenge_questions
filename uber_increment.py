def increment(num_list):
    if num_list == sorted(num_list, reverse=True):
        return f"{num_list} is already the largest number that can be made."
    elif num_list[-1] > num_list[-2]:
        x = num_list.pop()
        num_list.insert(-1,x)
    elif num_list[-1] > num_list[-3]:
        x = num_list.pop()
        num_list.insert(-2,x)
    elif num_list[-1] < num_list[-2] > num_list[-3]:
        x = num_list.pop(-3)
        num_list.append(x)
    else:
        x = num_list[-4]
        s = sorted(num_list)
        frst = s[s.index(x)+1]
        num_list.remove(frst)
        num_list = sorted(num_list)
        num_list.insert(0,frst)
    return num_list

# print(increment([2,4,3,1]))
# print(increment([1,4,3,2]))

# print(increment([1,2,3,4]) == [1,2,4,3])
# print(increment([1,2,4,3]) == [1,3,2,4])
# print(increment([1,3,2,4]) == [1,3,4,2])
# print(increment([1,3,4,2]) == [1,4,2,3])
# print(increment([1,4,2,3]) == [1,4,3,2])
# print(increment([1,4,3,2]) == [2,1,3,4]) 
# print(increment([2,1,3,4]) == [2,1,4,3]) 


# 1234
# 1243
# 1324
# 1342
# 1423
# 1432

# 2134
# 2143
# 2314
# 2341
# 2413
# 2431

# 3124
# 3142
# 3214
# 3241
# 3412
# 3421

# 4123
# 4132
# 4213
# 4231
# 4312
# 4321
