# merge index:
# given 2 lists of the same length, there is a point where the lists converge
# give the index where lists converge going forward
# if the lists do not converge after a point return -1

# Done 3/10/2020

# For loop solution

def merge_index(l1, l2):
    for i in range(1,len(l1)+1):
        idx = -i
        if l1[idx] != l2[idx]:
            result = len(l1) + (idx + 1)
            return -1 if result == len(l1) else result
    return 0

# While loop solution
def merge_index2(l1,l2):
    idx = len(l1) -1
    while idx > 0:
        if l1[idx] != l2[idx]:
            result = idx +1
            return -1 if result == len(l1) else result
        idx -= 1
    return 0


l1 = [1,2,3,4,9,3,8,7,3,9]
l2 = [1,2,8,6,9,3,8,7,3,9] # 4

print(merge_index(l1, l2))
print(merge_index2(l1, l2))

l3 = [1,2,3,4,9,3,8,7,3,9]
l4 = [1,2,8,6,9,3,8,7,1,0] # 9

print(merge_index(l3, l4))
print(merge_index2(l3, l4))

l5 = [1,2,3,4,9,3,8,7,3,9]
l6 = [1,2,3,4,9,3,8,7,3,9]

print(merge_index(l5, l6))
print(merge_index2(l5, l6)) 