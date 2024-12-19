import pandas as pd


def generatebudget(df,position,price_cname='Price',position_cname='Pos'):
    '''Generate the budget range for a particular FPL position given:
    data on the player prices and defaults on how many players are required per position;
    return a tuple of min budget, max budget, and target number of players'''
    
    n_players = {'GK':2,'DEF':5,'MID':5,'FWD':3} ##player count required in team
    target = n_players[position]

    prices = df[price_cname][df[position_cname]==position].sort_values()

    min_budget = 0
    for i in range(target):
        min_budget += prices.iloc[i]

    max_budget = 0
    for i in range((-1*target),0):
        max_budget += prices.iloc[i]

    return min_budget, max_budget, target #minimum budget, maximum budget, target number of players


if __name__ == '__main__':
    predictions = pd.read_csv("data/predictedpoints.csv") '''Use OS to peg file'''
    start_gw = 17 #Enter the starting gameweek for your team selection
    gw_count = 5 #Up to how many gameweeks in the future would you like to consider

    ## Compute the total expected points for the next gw_count weeks  the starting gameweek
    predictions['total_pts'] = predictions[str(start_gw) + '_with_prob']
    for gw in range(start_gw+1,start_gw+gw_count):
        predictions['total_pts'] += predictions[str(gw) + '_with_prob']

    predictions = predictions[predictions.total_pts != 0] #Drop all players with 0 expected points
    predictions['pts_per_price'] = predictions['total_pts']/predictions['Price'] #Compute total points per price
    
    print(generatebudget(df=predictions, position = 'MID'))