
# Hare and Tortise Algorithm
# https://www.youtube.com/watch?time_continue=1&v=-YiQZi3mLq0&feature=emb_title

# Use to dectect if a linked likst has a loop in a linked list

# ex: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> back to 2

# Tortise moves 1 node per iteration
# Hare moves 2 nodes per iteration
# Both start at 0. After 1 iteration the T is at the first node and Hare is on
# the secound node. After the 2nd iteration the hare is at node 4 
# and the tortise as at node 2 etc.

# if hare and tortise point to the same node there is a loop.
# if the hare reaches the end of the linked list, there is no loop

# in this case the tortise and hare first meet at node 4

# We want to find out were the loop starts

# N is the total number of nodes the tortise has moved after N iterations
# 2N is the total number of nodes the hare has moved after N iterations
# D is the part of the linked list up to the loop
# K  is the point in which the tortise and hare (first) meet from the start of the loop
# C is the length of nodes in 1 complete cycle of the loop 
# i is the number of cycles of the loop the tortise has done before meeting
# j is the number of cycles the hare has done before meeting

# In this case:
# D = dist node(0) to node(2) - the size of list not including the cycle
# K = dist node (3) to node(4) - dist from start of the loop (after D) to where they meet


# N  = D + K + C(i) #[Tortise]
# 2N = D + K + C(j) # [Hare]

# substitute the value of N in the first (tortise) line to the value of N in the 2nd (hare) line

        #   2*N = 2N
# 2D + 2K + 2iC = D + K + jC

#=> D + K + (2i-j)C = 0
#=> D + K = (j-2i)C    #gets you to meeting point
#=> D  = (j-2i)C - K

# T moves D nodes from the start and H moves D nodes from K
# They meet at the start of the loop

## K is the same distance from the start of the loop as the head is from the start of the loop 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def tortise_and_hare(head):
    if not head:
        return None
    tortise = hare = head
    while hare and hare.next:
        tortise, hare = tortise.next, hare.next.next
        if tortise == hare:
            while head != tortise:
                head, tortise = head.next, tortise.next
            return head
    return None

# '''
e1 = ListNode(3)
e2 = ListNode(2)
e1.next = e2
e3 = ListNode(0)
e2.next = e3
e4 = ListNode(-4)
e3.next = e4
e4.next = e2
# e1 --> e2 --> e3 --> e4 --> back to e2 
# '''

'''
e1 = ListNode(1)
e2 = ListNode(2)
e1.next = e2
e2.next = e1
# e1 --> e2 --> back to e1 
'''

'''
e1 = ListNode(1)
# e1 --> None 
'''
result = tortise_and_hare(e1)
print(None) if result == None else print(result.val)