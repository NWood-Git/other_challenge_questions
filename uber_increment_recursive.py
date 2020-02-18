def increment(num_list):
    if num_list == sorted(num_list, reverse=True):
        print("Done")
        return num_list
    elif num_list[-1] > num_list[-2]:
        x = num_list.pop()
        num_list.insert(-1,x)
        print(num_list)
        return increment(num_list)
    elif num_list[-1] > num_list[-3]:
        x = num_list.pop()
        num_list.insert(-2,x)
        print(num_list)
        return increment(num_list)
    elif num_list[-1] < num_list[-2] > num_list[-3]:
        x = num_list.pop(-3)
        num_list.append(x)
        print(num_list)
        return increment(num_list)
    else:
        x = num_list[-4]
        s = sorted(num_list)
        frst = s[s.index(x)+1]
        num_list.remove(frst)
        num_list = sorted(num_list)
        num_list.insert(0,frst)
        print(num_list)
        return increment(num_list)

increment([1,2,3,4])



# # def increment(test_list):
# #     for x 

# # test_list = [3,8,5,4] #4358

# t_list = [4,3,1,2]
# sort_list = sorted(t_list, reverse=True)
# # print(sort_list)

# def increment(t_list):
#     m = len(t_list) - 1
#     n = len(t_list) - 2
#     # sort_list = sorted(t_list, reverse=True)
#     if t_list == sorted(t_list, reverse=True):
#         return "This is the highest number that can be created."
#     elif t_list[n] < t_list[m]:
#         t_list[m], t_list[n] = t_list[n], t_list[m]
#         return t_list
#     elif:
#         m-=1
#         n-=1


# print(increment(t_list))