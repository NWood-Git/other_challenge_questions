def increment(num_list):
    lim = len(num_list) * -1
    counter = -1
    if num_list == sorted(num_list, reverse=True):
        return num_list
    else:
        while counter >= lim+1:
            if counter > lim+1 and num_list[counter] <= num_list[counter-1]:
                counter -= 1
            elif num_list[counter] > num_list[counter-1]:
                x = num_list[counter-1] #the first num to dec from prev starting at end
                temp_list = sorted(num_list[counter-1:]) #sorting the list from the 1st dec num till end 
                num_x = temp_list.count(x) #count of x (first num to dec)
                # next_num_x = temp_list[temp_list.index(x) + num_x] #finding the next higher number
                beg = num_list[:counter-1]
                y = [temp_list.pop(temp_list.index(x) + num_x)]
                #temp list is end
                num_list = beg + y + temp_list
                return num_list

# print(increment([9,1,5,8,7,6,5,4,3,2,1]))
# print(increment([1,2]))

def recursive_increment(num_list):
    lim = len(num_list) * -1
    counter = -1
    if num_list == sorted(num_list, reverse=True):
        return num_list
    else:
        while counter >= lim+1:
            if counter > lim+1 and num_list[counter] <= num_list[counter-1]:
                counter -= 1
            elif num_list[counter] > num_list[counter-1]:
                x = num_list[counter-1] #the first num to dec from prev starting at end
                temp_list = sorted(num_list[counter-1:]) #sorting the list from the 1st dec num till end 
                num_x = temp_list.count(x) #count of x (first num to dec)
                # next_num_x = temp_list[temp_list.index(x) + num_x] #finding the next higher number
                beg = num_list[:counter-1]
                y = [temp_list.pop(temp_list.index(x) + num_x)]
                #temp list is end
                num_list = beg + y + temp_list
                print(num_list)
                return recursive_increment(num_list)

# recursive_increment([1,2])

recursive_increment([1,2,3,4])



# 12345
# 12354

# 12435
# 12453

# 12534
# 12543

# 13245
# 13254

# 13425
# 13452

# 14235
# 14253

# 14325
# 14352

# 14523
# 14532
# .
# .
# 15432
# 21345