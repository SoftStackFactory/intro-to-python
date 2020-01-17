
# coding: utf-8

# In[1]:


from collections import defaultdict


# ### Sample Hands
# 
# Sample data for each possible winning combination has been created for testing your functions. The hands can be used individually or a list has been created allowing you to loop thru the hands if you choose.
# 
# A dict has been created called card_order_dict, this will represent the values assisgned to each card and will be used to map values to cards that are above 9.
# 
# [Example](https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python.html)

# In[2]:


no_pair = ["3D", "JS", "QD", "5D", "AD"]
pair = ["3D", "JD", "QD", "Ah", "AD"]
two_pair = ["3S", "JS", "JD", "3H", "AD"]
trips = ["3D", "3H", "3S", "5D", "AD"]
straight = ["3D", "4D", "5H", "6D", "7S"]
full_house = ["3D", "3C", "3H", "5D", "5C"]
flush = ["3D", "JD", "QD", "5D", "AD"]
quads = ["3D", "3H", "QD", "3S", "3C"]
straight_flush = ["3D", "4D", "5D", "6D", "7D"]
royal_flush = ["TD", "JD", "QD", "KD", "AD"]

hands = [
    # no_pair, # Not yet implemented
    pair,
    two_pair,
    trips,
    straight,
    flush,
    full_house,
    quads,
    straight_flush,
    royal_flush
]

card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}

SCORING = {
    # 0 : 'NO_PAIR', # not yet implemented 
    1 : 'PAIR',
    2 : 'TWO_PAIR',
    3 : 'THREE_OF_KIND',
    4 : 'STRAIGHT',
    5 : 'FLUSH',
    6 : 'FULL_HOUSE',
    7 : 'FOUR_OF_KIND',
    8 : 'STRAIGHT_FLUSH',
    9 : 'ROYAL_FLUSH'
}


# ### Check for pair
# 
# ###### Purpose: 
# 
#     This function checks a given hand to see if any pairs exist.
#     
#     This is accomplished by first creating a list called values. Using list comprehensions, the suits are removed
#     and we're left with a list of card values.
#         - values example: ['3', 'J', 'Q', '5', 'A']
#     
#     A dict is created called value_counts. 
#     
#     We then loop over the values list, setting each item as the dict key and its value equal to the number of 
#     occurances that value shows in the list.
#         - value_counts example: {'3': 1, 'J': 1, 'Q': 1, '5': 1, 'A': 1}
#         
#     Once we have the value_counts dict, with the use of a conditional statement, we're able to check the count values     to confirn if a value appears twice.
#         - value_counts.values example: dict_values([1, 1, 1, 1, 1])
# 
# ###### Params:
# 
#     hand: List of stings representing card values & suit
#     example hand: ['3D', 'JS', 'QD', '5D', 'AD']
# 
# ###### Return:
# 
#     True if pair found else False

# In[3]:


def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    
    for v in values:
        value_counts[v]+=1
    
    if 2 in value_counts.values():
        return True
    else:
        return False


# ### Check for two pairs
# 
# ###### Purpose: 
# 
#     This function checks a given hand to see if 2 pairs exist.
#     
#     This is accomplished by first creating a list called values. Using list comprehensions, the suits are removed
#     and we're left with a list of card values.
#         - values example: ['3', 'J', 'J', '3', 'A']
#     
#     A dict is created called value_counts. 
#     
#     We then loop over the values list, setting each item as the dict key and its value equal to the number of 
#     occurances that value shows in the list.
#         - value_counts example: {'3': 2, 'J': 2, 'A': 1}
#         
#     Once we have the value_counts dict, with the use of a conditional statement, we're able to check the dict 
#     values to see if two pairs are detected.
#         - value_counts.values example: dict_values([2, 2, 1])
# 
# ###### Params:
# 
#     hand: List of stings representing card values & suit
#     example hand: ['3S', 'JS', 'JD', '3H', 'AD']
# 
# ###### Return:
# 
#     True if 2 pairs found else False

# In[4]:


def check_two_pairs(hand):
    values = [i[0] for i in hand] 
    value_counts = defaultdict(lambda:0) 
    
    # loop values
    for v in values:
        # set value item as key and value is equal to count 
        value_counts[v]+=1
    
    # condition checking for two pairs
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False
    


# ### Check for trips
# 
# ###### Purpose: 
# 
#     This function checks a given hand to see if it contains 3 of a kind.
#     
#     This is accomplished by first creating a list called values. Using list comprehensions, the suits are removed
#     and we're left with a list of card values.
#         - values example: ['3', '3', '3', '5', 'A']
#     
#     A dict is created called value_counts. 
#     
#     We then loop over the values list, setting each item as the dict key and its value equal to the number of 
#     occurances that value shows in the list.
#         - value_counts example: {'3': 3, '5': 1, 'A': 1}
#         
#     Once we have the value_counts dict, with the use of a conditional statement, we're able to check the dict 
#     values to see if two pairs are detected.
#         - value_counts.values example: dict_values([3, 1, 1])
# 
# ###### Params:
# 
#     hand: List of stings representing card values & suit
#     example hand: ['3D', '3H', '3S', '5D', 'AD']
# 
# ###### Return:
# 
#     True if 3 of a kind found else False

# In[84]:


def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    
    for v in values:
        value_counts[v]+=1

    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False
    

# ### Check for straight
# 
# ###### Purpose: 
# 
#     This function checks a given hand to see if its cards are in order.
#     
#     This is accomplished by first creating a list called values. Using list comprehensions, the suits are removed
#     and we're left with a list of card values.
#         - values example: ['3', '4', '5', '6', '7']
#     
#     A dict is created called value_counts. 
#     
#     A list called rank_values is created and contains each cards value. A global dict above named card_order_dict 
#     is used to map values for cards that are above 9 (T, J, Q, K, A).
#         - rank_values example: [3, 4, 5, 6, 7]
#         
#     With a list of rank_values we now create a variable called value_range, this variable will hold an integer     
#     representing the max value in the rank_values list minus the minimum value in the list. For any given straight, 
#     the (max_value - min_value) will equal 4 with the exception of ["A", "2", "3", "4", "5"], this condition will 
#     be handled in the event value_range != 4.
#         - value_range example: 7-3=4
#         
#     Once we have the value_range we're able to use a conditional statement to verify a length of 1 and 
#     verify that the value_range is equal to 4. If either value is false, we'll do one last check to see if the hand 
#     represents ["A", "2", "3", "4", "5"], if so returns True.
#     
#     
# 
# ###### Params:
# 
#     hand: List of stings representing card values & suit
#     example hand: ['3D', '4D', '5H', '6D', '7S']
# 
# ###### Return:
# 
#     True if straight found else False

# In[93]:


def check_straight(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    
    for v in values:
        value_counts[v] += 1

    rank_values = [card_order_dict[i] for i in values]
    
    value_range = max(rank_values) - min(rank_values)

    if len(set(value_counts.values())) == 1 and (value_range==4):
        return True
    else: 
        #check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True
        return False
    


# ### Check for flush
# 
# ###### Purpose: 
# 
#     This function checks a given hand to see if it contains all the same suits.
#     
#     This is accomplished by first creating a list called suits. Using list comprehensions, the values are removed
#     and we're left with a list of card suits.
#         - suits example: ['D', 'D', 'D', 'D', 'D']
#         
#     Once we have the suits list, we'll take the set of that list, if the length of the set==1, return True.
#         - len(set(suits)) example: 1
#         - set(suits) example: {'D'}
# 
# ###### Params:
# 
#     hand: List of stings representing card values & suit
#     example hand: ['3D', 'JD', 'QD', '5D', 'AD']
# 
# ###### Return:
# 
#     True if flush found else False

# In[6]:


def check_flush(hand):
    suits = [i[1] for i in hand]

    if len(set(suits))==1:
        return True
    else:
        return False
    


# ### Check for full house
# 
# ###### Purpose: 
# 
#     This function checks a given hand to see if it contains a full house (3 of a kind with a pair).
#     
#     This is accomplished by first creating a list called values. Using list comprehensions, the suits are removed
#     and we're left with a list of card values.
#         - values example: ['3', '3', '3', '5', '5']
#         
#     A dict is created called value_counts. 
#     
#     We then loop over the values list, setting each item as the dict key and its value equal to the number of 
#     occurances that value shows in the list.
#         - value_counts example: {'3': 3, '5': 2}
#         
#     Once we have the value_counts dict, with the use of a conditional statement, we're able to check the dict 
#     values to see if a pair with 3 of a kind are detected.
#         - value_counts.values example: dict_values([3, 2])
# 
# ###### Params:
# 
#     hand: List of stings representing card values & suit
#     example hand: ['3D', '3C', '3H', '5D', '5C']
# 
# ###### Return:
# 
#     True if full house found else False

# In[97]:


def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    
    for v in values: 
        value_counts[v]+=1
   
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False



# ### Check for quads
# 
# ###### Purpose: 
# 
#     This function checks a given hand to see if it contains four of a kind.
#     
#     This is accomplished by first creating a list called values. Using list comprehensions, the suits are removed
#     and we're left with a list of card values.
#         - values example: ['3', '3', 'Q', '3', '3']
#         
#     A dict is created called value_counts. 
#     
#     We then loop over the values list, setting each item as the dict key and its value equal to the number of 
#     occurances that value shows in the list.
#         - value_counts example: {'3': 4, 'Q': 1}
#         
#     Once we have the value_counts dict, with the use of a conditional statement, we're able to check the dict 
#     values to see if a pair with 3 of a kind are detected.
#         - value_counts.values example: dict_values([4, 1])
# 
# ###### Params:
# 
#     hand: List of stings representing card values & suit
#     example hand: ['3D', '3H', 'QD', '3S', '3C']
# 
# ###### Return:
# 
#     True if four of a kind found else False

# In[99]:


def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    
    for v in values: 
        value_counts[v]+=1
    
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False


# ### Check for straight flush
# 
# ###### Purpose: 
# 
#     This function checks a given hand to see if it contains a straight flush.
#     
#     This is accomplished by using two functions that we previously created, check_flush & check_straight.
# 
# ###### Params:
# 
#     hand: List of stings representing card values & suit
#     example hand: ['3D', '4D', '5D', '6D', '7D']
# 
# ###### Return:
# 
#     True if straight and flush found else False

# In[100]:


def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False

# In[7]:


def check_royal_flush(hand):
    values = [i[0] for i in hand]
    if set(values) == set(["T", "J", "Q", "K", "A"]) and check_flush(hand):
        return True
    else:
        return False



def check_hands():
    poker_hand_checking_functions = [
        check_royal_flush,
        check_straight_flush,
        check_four_of_a_kind,
        check_full_house,
        check_flush,
        check_straight,
        check_three_of_a_kind,
        check_two_pairs,
        check_one_pairs,
        # check_high_card # Not implemented yet
    ]

    for i, hand in enumerate(hands):

        print("Current hand is ", SCORING[i+1], ": ", hand)
        
        # Interate over functions to see if the hand is a high_card
        for i,f in enumerate(poker_hand_checking_functions):
            # create a scoring index based on the current value of i
            scoring_idx = len(SCORING) - i            
            print("{} : {} {} ".format(f(hand), hand, SCORING[scoring_idx])) 
            
        print()




# %%
if __name__ == "__main__":
    check_hands()
