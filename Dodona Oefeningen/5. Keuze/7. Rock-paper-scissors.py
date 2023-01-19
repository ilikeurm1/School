"""DIT IS HEEL SLECHTE CODE"""
"""DIT IS HEEL SLECHTE CODE"""
"""DIT IS HEEL SLECHTE CODE"""
"""DIT IS HEEL SLECHTE CODE"""
"""DIT IS HEEL SLECHTE CODE"""

player1 = input('RPC 1: ')
player2 = input('RPC 2: ')
chosen1 = len(player1)
chosen2 = len(player2)
	
if chosen1 == chosen2: #same	    
    print('tie')
elif chosen1 == 4 and chosen2 == 8: #rock against scissors
    print('player1 wins')
elif chosen2 == 4 and chosen1 == 8: #rock against scissors
    print('player2 wins')
elif chosen1 == 8 and chosen2 == 5: #scissors against paper
	print('player1 wins')
elif chosen2 == 8 and chosen1 == 5: #scissors against paper
	print('player2 wins')
elif chosen1 == 5 and chosen2 == 4: #Paper against rock
	print('player1 wins')
elif chosen2 == 5 and chosen1 == 4: #Paper against rock
	 print('player2 wins')