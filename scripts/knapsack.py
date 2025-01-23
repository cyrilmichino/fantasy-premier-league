cache = dict() ##Cache for the position knapsack algorithm
memo = dict() ##Cache for the team knapsack algorithm

def positionalknapsack(budget, ids, prices, points, choices):
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
        cache[(budget,tuple(ids),choices)] = positionalknapsack(budget, ids[:-1], prices[:-1],points[:-1],choices)
        return cache[(budget,tuple(ids),choices)]
    else:
        a = positionalknapsack(budget, ids[:-1],prices[:-1],points[:-1],choices)  #ignore the last item
        b = positionalknapsack(budget-prices[-1],ids[:-1],prices[:-1],points[:-1],choices-1) #include the last item
        if a[0] >= b[0]+points[-1]:
            cache[(budget,tuple(ids),choices)] = a
        else:
            cache[(budget,tuple(ids),choices)] = (b[0]+points[-1],b[1]+[ids[-1]])    
        return cache[(budget,tuple(ids),choices)]


def teamknapsack(budget,points_grid,prices_grid,players_grid):
    ## Base cases
    if budget == 0:
        return [0,[]] if len(prices_grid) == 0 else [float('-inf'),[]]
    if len(prices_grid) == 0:
        return [0,[]]
    if len(prices_grid[0]) == 0:
        return [float('-inf'),[]]
                
    ## Retrieve solutions from the memo
    if (budget,len(prices_grid), len(prices_grid[0])) in memo.keys():
        return memo[(budget,len(prices_grid),len(prices_grid[0]))]
    
    ## Repetitive sub-problem
    if prices_grid[0][0] > budget:
        points_grid[0] = points_grid[0][1:]
        prices_grid[0] = prices_grid[0][1:]
        players_grid[0] = players_grid[0][1:]
        memo[(budget,len(prices_grid), len(prices_grid[0]))] = teamknapsack(budget,points_grid,prices_grid,players_grid)
        return memo[(budget,len(prices_grid), len(prices_grid[0]))]
    else:
        a = teamknapsack(budget-prices_grid[0][0],points_grid[1:],prices_grid[1:],players_grid[1:])
        c = [points_grid[0][0],[players_grid[0][0]]]

        points_grid[0] = points_grid[0][1:]
        prices_grid[0] = prices_grid[0][1:]
        players_grid[0] = players_grid[0][1:]
        b = teamknapsack(budget,points_grid,prices_grid,players_grid)

        if a[0] + c[0] >= b[0]:
            memo[(budget,len(prices_grid), len(prices_grid[0]))] = [a[0]+c[0],a[1]+c[1]]
            return memo[(budget,len(prices_grid), len(prices_grid[0]))]
        else:
            memo[(budget,len(prices_grid), len(prices_grid[0]))] = b
            return memo[(budget,len(prices_grid), len(prices_grid[0]))]


def transferknapsack(team, transfers, optimal_team, ids, prices, points, choices):
    ## Compare current team to determine the players that should not be touched
    ## Loop through the team to find all the combinations of transfer outs if player is not on optimal team
        ### Encode all combinations before starting the knapsack loop
        ### For every loop find the optimal replacement set
            ## Use team max points = points of new players + points of players not transferred
        ### Compare all replacements to see which one has the highest increment in max points

        #HOW CAN WE REFACTOR AND USE THE TEAM KNAPSACK FUNCTION
        #THERE ARE INSTANCE WHERE WE DON'T HAVE TO EXHAUST THE TRANSFERS
        #FOR COMMUNITY SCALE, OPTIMAL TEAM FUNCTIONS SHOULD RUN ON A CRON JOB AND ENCODED IN A BASE


if __name__ == "___main__":
    ## Test position knapsack algorithm
    print(positionalknapsack(budget=8,ids=[0,1,2,3],prices=[1,3,5,7],points=[2,4,7,10],choices=2))

    ## Test team knapsack algorithm
    a = [[2,3,4],[5,6,7],[8,9,10]]
    b = [[2,3,4],[5,6,7],[8,9,10]]
    c = [[[1,1],[2,2],[3,3]],[[1,1],[2,2],[3,3]],[[1,1],[2,2],[3,3]]]
    print(finalknapsack(20,a,b,c))