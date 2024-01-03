import random

def game():
	player = input('rock, paper, scissors? > ')
	ai = random.randint(1, 3)
	
	if player == 'rock':
		if ai == int(1):
			print('draw')
			
		
		if ai == int(2):
			print('loose')
			
		
		if ai == int(3):
			print('win')
	
	if player == 'paper':
		if ai == int(1):
			print('win')
			
		if ai == int(2):
			print('draw')
		
		if ai == int(3):
			print('loose')
			
		if player == 'scissors':
			if ai == int(1):
				print('loose')
				
			if ai == int(2):
				print('win')
				
			if ai == int(3):
				print('draw')
				
		
				
				
game()
