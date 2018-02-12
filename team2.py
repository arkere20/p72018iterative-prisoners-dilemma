####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Andrew' # Only 10 chars displayed.
strategy_name = 'Best Chance'
strategy_description = 'Determine the likelihood that an opponent will betray based on their previous moves.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    if (len(their_history) == 0):
        # This is the first move against a new opponent
        return 'b' # Always betray on the first move
    else:
        if (determine_betray_percentage(their_history) == 50):
            return 'c' # If they only betray half the time, collude so we both gain 100 points(this does not help against the current opponent, but a point advantage will help overall if all rounds are tallyed up). 
        elif (determine_betray_percentage(their_history) <= 50):
            return 'b' # They are likely to collude, so I should betray them to win(and gain 250 points in the process)
        else:
            return 'b' # They are likely to betray, so my best option is to also betray(I would only lose 100 points vs losing 250 if I colluded).

def determine_betray_percentage(their_history):
    history_list = list(their_history) #Convert their_history to an iterable list.
    betray_amount = 0 #Check how many times they've betrayed and colluded.
    collude_amount = 0
    for letter in history_list: #Loop through each previous result...
        if (letter == 'b'): #If they betrayed...
            betray_amount += 1 #Increase their betray count.
        elif (letter == 'c'):  #If they colluded...
            collude_amount += 1 #Increase their collude count.
    if ((betray_amount == collude_amount)): #If they've colluded and betrayed an equal amount of times...
        return 50 #Return 50 (percent).
    elif ((betray_amount > collude_amount)): #If they've betrayed more than they've colluded...
        return round(betray_amount / (betray_amount + collude_amount)) #Determine their betray percentage and round it to a whole number.
    else: #If they've colluded more than they've betrayed...
        round(collude_amount / (betray_amount + collude_amount)) #Determine their betray percentage and round it to a whole number.

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             