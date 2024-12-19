from positionknapsack import knapsack


def chooseplayers(df, position, price_cname='Price', position_cname='Pos', pts_cname='total_pts', id_cname='ID'):
    '''Determine the budget range for a specific position;
    run the position knapsack script for every budget point;
    return the points returns and players chosen for all budget types'''
    
    min_,max_,target = generatebudget(predictions, position)
    budgets = list(np.arange(min_,max_+0.1,0.1))

    players = df[[id_cname,price_cname,pts_cname]][df[position_cname]==position]
    returns = list() ## 2D array with every row as budget,return,players

    for budget in budgets:
        budget = round(budget,1)
        budget_return,players_chosen = knapsack(budget, ids=list(players[id_cname]), prices=list(players[price_cname]), points=list(players[pts_cname]), choices=target)
        returns.append([budget,budget_return,players_chosen])

    return returns


'''if __name__ == '__main__':

    '''