# F(6,20) -> 3 Done 3/6/2020
# Given F(A,B) return the number of integers from the range [A,B] that can be expressed as a product of 2 consequtive numbers
# F(6,20) = 3 because 6=3*2, 12=3 * 4 and 20 = 4* 5

# neat question, can be done in O(B-A)
# actually can be done in O(1) 
import math

def product_range_old(num1, num2):
    count = 0
    for num in range(1,(math.ceil(num2**.5)+1)):
        if num1 <= (num * (num + 1)) <= num2:
            count += 1
    return count

print(product_range_old(6,20)) # returns 3
print(product_range_old(1,3)) # 1

def product_range(num1, num2):
    return len([x*(x+1)for x in range(math.ceil(num2**.5)) if (x*(x+1)) >= num1])

print(product_range(6,20)) # returns 3
print(product_range(1,3)) # 1