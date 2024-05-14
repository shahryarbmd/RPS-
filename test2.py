'''
basically we need to have user input as rock paper or scissors
then we need an opponent whose choice depends on users last games experiences
but if its the first game it has to be random
then there are win conditions depending on both current user and opp choices
each one win lose or tie changes a variable basically storing the info
thus with the info opponent makes better choices

but if the user figures the pattern out they will get winstreaks since they know
the opponent will counter their most winning choice
so if the user has a streak of 2 wins in a row with any choice the opponent
has to counter the counter to the winning choice
like
if user_(rps)_streak >= 2:
   opp = RPS list value
'''