# Given a list of points in time (represented by whole numbers that are increasing) D
# Give the max profit - buy low / sell high


data = [[4, 200],[2,75],[3,500], [1,200], [5,50], [6,300], [7,100], [8,350], [9, 100], [10, 300]]
data2 = [[1,80],[2,30],[3,20],[4,80],[5,30],[6,50],[7,100],[8,80],[9,60],[10,50]]
data3 = [(0,5), (1,10), (2,1), (3,15), (4,1)]


def max_profit(dataset):
    # dataset = sorted(dataset)
    # buy = dataset[0][1]
    # sell = dataset[0][1]
    profit = 0
    data = [i[1] for i in dataset]
    # px_min = min(data)
    # px_max = max(data)
    # if data.index(px_min) < data.index(px_max):
    #     return px_max - px_min
    for i in  range(len(data)):
        mx = max(data[i:])
        p_diff = mx - data[i]
        if p_diff > profit:
            profit = p_diff
    return profit

# This solution is O(n**2) the best solution is O(n) 

# pxs = [x[1] for x in data]
# print(pxs)

# print(max(pxs[3:]))

print(max_profit(data))
print(max_profit(data2))
print(max_profit(data3))