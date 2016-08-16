def start():
	
	print """
	You are in a clearing.
	To the south is a forest.
	To the west is a house.
	To the east is a lake.
	To the north is a dark cave.
	
	What do you do?
	"""
	
	choice = raw_input("> ")
	
	if 'north' in choice:
		cave_test()
	elif 'cave' in choice:
		cave_test()
	elif 'south' in choice:
		forest()
	elif 'forest' in choice:
		forest()
	elif 'east' in choice:
		lake_test()
	elif 'lake' in choice:
		lake_test()
	elif 'west' in choice:
		house()
	elif 'house' in choice:
		house()
	else:
		print "Command not understood."
		start()
	
	
def forest():
	print """
	You are in a deep forest.
	The way ahead is blocked.
	On the ground is a pile of sticks.
	To the north is a clearing.
	
	What do you do?
	"""
	
	choice = raw_input("> ")
	
	if 'sticks' in choice:
		if 'sticks' in inv:
			print "\n\tYou already have sticks. \n"
		else:
			print "\n\t You pick up sticks.\n"
			inv.append('sticks')
		forest()
	elif 'north' in choice:
		start()
	else:
		print "Command not understood."
		forest()

def cave_test():
	if 'torch' not in inv:
		cave_no_torch()
	else:
		cave()
	

def cave_no_torch():
	print """
	The cave is very dark.
	Are you sure you want to go in?
	"""
	choice = raw_input("\n\ty/n?\n")
	
	if 'y' in choice:
		dead('You stumble into the dark cave and something bites your leg.\n\tThe world fades to black.')
	elif 'n' in choice:
		print "\n\tYou return to the clearing."
		start()
	else:
		print "Command not understood."
		cave_no_torch()
		

def cave():
	print """
	Your Torch lights the cave.
	You see a serpent on a pile of gold.
	Do you fight?
	"""
	
	choice = raw_input("\n\ty/n? \n")
	
	if 'y' in choice:
		fight()
		
	elif 'n' in choice:
		cave()
	else:
		print "Command not understood."
		cave()
		
		
def fight():
	if 'sword' in inv:
		win()
	elif 'sword' not in inv:
		dead('\n\tThe serpent bites, and the world fades to black')
	else:
		print "Error. Restart required."
	

def house():
	print """
	You are in a warm house.
	A fire burns in the fireplace.
	On the floor are bundles of cloth.
	If you had some sticks, you could make a torch.
	
	What do you do?
	"""
	
	choice = raw_input("> ")
	
	if 'torch' in choice:
		if 'sticks' in inv:
			print "\n\tYou make a torch.\n"
			inv.append('torch')
			house()
		else:
			dead("\n\tYou burn yourself trying to make a torch with no sticks and die.")
	elif 'east' in choice:
		start()
	elif 'clearing' in choice:
		start()
	else:
		print "Command not understood."
		house()
	
	

def lake_test():
	if 'torch' not in inv:
		print "\n\tA thick fog covers the lake."
		print "\n\tYou can't see a thing."
		print "\n\tYou have to turn back."
		start()
	elif 'torch' in inv:
		lake()
	else:
		print "\n\tSomething has gone wrong with this game." 
		print "\n\tYou should never see this."
		

def lake():
	print"""
	Your torch cuts through the fog.
	You stand on the banks of a cloudy lake.
	In the brush is a wooden chest.
	To the west is the clearing you came from.
	
	What do you want to do?
	"""
	
	choice = raw_input("> ")
	
	if 'open' in choice:
		chest_open()
	
	elif 'chest' in choice:
		chest_open()
			
	elif 'west' in choice:
		start()
	
	elif 'clearing' in choice:
		start()
		
	elif 'swim' in choice:
		dead ('\n\tYou can\'t swim.\n\tYou drown.')
		
	else:
		print "Command not understood."
		lake()
		

def chest_open():
	if 'sword' not in inv:
			print "\n\tInside the chest is a sword."
			print "\n\tYou take it."
			inv.append('sword')
			lake()
			
	else:
		print "\n\tThe chest is already open."
		lake()

	
def dead(reason):
	print reason
	print "\n\tRestart y/n? \n"
	choice = raw_input("> ")
	if choice == 'y':
		start()
	elif choice == 'n':
		quit()
	else:
		print "Command not understood."
		dead(' ')
		

def win():
	print"""
	Congratulations!
	The Gold is yours!
	Stay tuned for an even bigger adventure!
	"""
	print "\n\tPlay again: y/n?"
	
	choice = raw_input ("> ")
	
	if 'y' in choice:
		start()
		
	elif 'n' in choice:
		quit()
		
	else:
		print "Command not understood."
		win()

		
inv = []

print "\n\tYou awaken from a deep sleep."	
start()