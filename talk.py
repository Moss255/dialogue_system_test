import json

position = 0

with open('C1.json', 'r') as p:
	cData = json.loads(p.read())

while position != -1:

	currentPosition = position

	# Get the player to say their line
	print('Character:' , cData[currentPosition]['line'])


	# Add options to list for player
	if len(cData[currentPosition]['responses']) > 0:
		for index, line in enumerate(cData[currentPosition]['responses']):
			print (index + 1 , ':' , line)
	else:
		# Move to next dialogue on click
		print ('Press 1 to continue')


	# Retrieve the users input
	temp = int(input('>>> '))
	if len(cData[currentPosition]['responses']) > 0:
		print("Player:" , cData[currentPosition]['responses'][temp - 1])
	currentPosition = cData[currentPosition]['responsesJump'][temp - 1]
	position = currentPosition
	

print('Character: See you then')