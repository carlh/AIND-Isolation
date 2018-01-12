Long Round 1
NUM_MATCHES = 100

def custom_score(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves_len = len(game.get_legal_moves(player))
    opp_moves_len = len(game.get_legal_moves(game.get_opponent(player)))

    corners = [(0, 0), (0, game.width - 1), (game.height - 1, 0), (game.height - 1, game.width - 1)]

    player_loc = game.get_player_location(player)
    opp_loc = game.get_player_location(game.get_opponent(player))
    if player_loc in corners:
        return -corner_penalty
    if opp_loc in corners:
        return corner_penalty
    if player_loc[0] == 0 or player_loc[0] == game.width - 1 or player_loc[1] == 0 or player_loc[1] == game.height - 1:
        return -edge_penalty
    if opp_loc[0] == 0 or opp_loc[0] == game.width - 1 or opp_loc[1] == 0 or opp_loc[1] == game.height - 1:
        return edge_penalty

    return float(own_moves_len - 2.0 * opp_moves_len)


def custom_score_2(game, player):
    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves_len = len(game.get_legal_moves(player))
    opp_moves_len = len(game.get_legal_moves(game.get_opponent(player)))

    corners = [(0, 0), (0, game.width - 1), (game.height - 1, 0), (game.height - 1, game.width - 1)]

    if game.get_player_location(player) in corners:
        return -4
    if game.get_player_location(game.get_opponent(player)) in corners:
        return 4
    return float(own_moves_len - opp_moves_len)


def custom_score_3(game, player):
    
    #  This is the OpenMove Score from the sample
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return player_moves - 2 * opp_moves

                        *************************                         
                             Playing Matches                              
                        *************************                         

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3 
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost 
    1       Random      166 |  34    154 |  46    168 |  32    171 |  29  
    2       MM_Open     130 |  70    114 |  86    126 |  74    129 |  71  
    3      MM_Center    138 |  62    143 |  57    139 |  61    157 |  43  
    4     MM_Improved   120 |  80    110 |  90    128 |  72    130 |  70  
    5       AB_Open     105 |  95    97  |  103   110 |  90    101 |  99  
    6      AB_Center    113 |  87    89  |  111   115 |  85    119 |  81  
    7     AB_Improved   99  |  101   78  |  122   91  |  109   98  |  102 
--------------------------------------------------------------------------
           Win Rate:      62.2%        56.1%        62.6%        64.6%    

There were 248.0 timeouts during the tournament -- make sure your agent handles search timeout correctly, and consider increasing the timeout margin for your agent.


Your agents forfeited 3138.0 games while there were still legal moves available to play.


Process finished with exit code 0

=================
Short Round 1
=================
def custom_score(game, player):
    # This heuristic penalized the current player for being against an edge
    # It gives a bonus if the opponent is against an edge
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves_len = len(game.get_legal_moves(player))
    opp_moves_len = len(game.get_legal_moves(game.get_opponent(player)))

    player_loc = game.get_player_location(player)
    opp_loc = game.get_player_location(game.get_opponent(player))
    if player_loc[0] == 0 or player_loc[0] == game.width - 1 or player_loc[1] == 0 or player_loc[1] == game.height - 1:
        return -edge_penalty
    if opp_loc[0] == 0 or opp_loc[0] == game.width - 1 or opp_loc[1] == 0 or opp_loc[1] == game.height - 1:
        return edge_penalty

    return float(own_moves_len - 2.0 * opp_moves_len)


def custom_score_2(game, player):
    # This is the Center Score heuristic
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves_len = len(game.get_legal_moves(player))
    opp_moves_len = len(game.get_legal_moves(game.get_opponent(player)))

    corners = [(0, 0), (0, game.width - 1), (game.height - 1, 0), (game.height - 1, game.width - 1)]

    if game.get_player_location(player) in corners:
        return -4.
    if game.get_player_location(game.get_opponent(player)) in corners:
        return 4.
    return float(own_moves_len - 2 * opp_moves_len)


def custom_score_3(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(1.5 * player_moves - 3.6 * opp_moves)
                        *************************                         
                             Playing Matches                              
                        *************************                         

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3 
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost 
    1       Random      38  |  12    34  |  16    40  |  10    41  |   9  
--------------------------------------------------------------------------
           Win Rate:      76.0%        68.0%        80.0%        82.0%    

There were 11.0 timeouts during the tournament -- make sure your agent handles search timeout correctly, and consider increasing the timeout margin for your agent.


Your agents forfeited 36.0 games while there were still legal moves available to play.


Process finished with exit code 0