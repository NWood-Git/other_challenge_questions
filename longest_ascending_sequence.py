# longest_ascending_sequence (245893254) -> 5

def longest_ascending_sequence(number):
    max_num = 1
    counter = 1
    number = list(map(int, str(number)))
    for i in range(len(number)-1):
        index1 = i
        index2 = i + 1
        if number[index1] < number[index2]:
            counter += 1
            if counter > max_num:
                max_num = counter
        # elif number[index1] > number[index2]:
        else:
            counter = 1
            index1 += 1
    return max_num

print(longest_ascending_sequence(245893254))
print(longest_ascending_sequence(325424589))
print(longest_ascending_sequence(123123456712))
print(longest_ascending_sequence(12123412123456789))
print(longest_ascending_sequence(987654321))

#recursive answer

# def longest_ascending_sequence(num, max=1, counter=1):
#     number = list(map(int, str(num)))
#     for i in range(len(number)):
#         index1 = i
#         index2 = i+1
#         if index2 == len(number):
#             return max
#         else:
#             if number[index1] < number[index2]:
#                 counter += 1
#                 if counter > max:
#                     max = counter
#             elif number[index1] > number[index2]:
#                 counter = 1
#             number = number[index2:]
#             str_list = [str(x) for x in number]
#             number = int(''.join(str_list))
#             return longest_ascending_sequence(number,max,counter)