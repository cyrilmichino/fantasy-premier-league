cache = dict() ## (budget, prices): whatever the knapsack computes

def knapsack(budget, ids, prices, points, choices):
    '''Given a fixed budget for players in a particular position,
    and the number of players you can choose (abstracted as choices);
    as well as data on players, their prices and their expected points,
    return the maximum points as well as the IDs of players in the selection.
    (0-1 knapsack problem that can be applied universally for all positions)'''
    
    ##Base Cases
    if choices == 0:
        return (0,[])
    if choices == 1:
        if len(ids) == 0:
            return (float('-inf'),[])
        if len(ids) == 1:
            return (float('-inf'),[]) if prices[0] > budget else (points[0],[ids[0]])
    if choices > 1 and len(ids) <= 1:
        return (float('-inf'),[])

    ## Retrieve from precomputed responses
    if (budget,tuple(ids),choices) in cache.keys():
        return cache[(budget,tuple(ids),choices)]

    ### Repetitive Subproblem
    if prices[-1] > budget:
        cache[(budget,tuple(ids),choices)] = knapsack(budget, ids[:-1], prices[:-1],points[:-1],choices)
        return cache[(budget,tuple(ids),choices)]
    else:
        a = knapsack(budget, ids[:-1],prices[:-1],points[:-1],choices)  #ignore the last item
        b = knapsack(budget-prices[-1],ids[:-1],prices[:-1],points[:-1],choices-1) #include the last item
        if a[0] >= b[0]+points[-1]:
            cache[(budget,tuple(ids),choices)] = a
        else:
            cache[(budget,tuple(ids),choices)] = (b[0]+points[-1],b[1]+[ids[-1]])    
        return cache[(budget,tuple(ids),choices)]


if __name__ == "___main__":
    print(knapsack(budget=8,ids=[0,1,2,3],prices=[1,3,5,7],points=[2,4,7,10],choices=2))