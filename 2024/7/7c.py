#!/usr/bin/python3

plans = {}
fileHandle = open("everybody_codes_e2024_q07_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
track = '+=+++===-+++++=-==+--+=+===-++=====+--===++=-==+=++====-==-===+=+=--==++=+========-=======++--+++=-++=-+=+==-=++=--+=-====++--+=-==++======+=++=-+==+=-==++=-=-=---++=-=++==++===--==+===++===---+++==++=+=-=====+==++===--==-==+++==+++=++=+===--==++--===+=====-=++====-+=-+--=+++=-+-===++====+++--=++====+=-=+===+=====-+++=+==++++==----=+=+=-S'
lenTrack = len(track)
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	plan = fileLine.split(':')[0]
	actions = fileLine.split(':')[1].split(',')
	n = len(actions)
	power = 10
	totalPower = 0
	for i in range(0,lenTrack*2024):
		x = i % n
		action = actions[x]
		if track[i%lenTrack] == '+':
			action = '+'
		if track[i%lenTrack] == '-':
			action = '-'
		if action == '+':
			power += 1
		if action == '-' and power > 0:
			power -= 1
		totalPower += power
	plans[plan] = totalPower
minPower = plans['A']
print(minPower)
winningPlans = 0
for z in range(0,3**11):
	plan = ''
	z1 = z
	for i in range(0,11):
		if z1 % 3 == 0:
			plan += '+'
		if z1 % 3 == 1:
			plan += '-'
		if z1 % 3 == 2:
			plan += '='
		z1 //= 3
	if plan.count('+') == 5 and plan.count('-') == 3 and plan.count('=') == 3:
		actions = list(plan)
		n = len(actions)
		power = 10
		totalPower = 0
		for i in range(0,lenTrack*2024):
			x = i % n
			action = actions[x]
			if track[i%lenTrack] == '+':
				action = '+'
			if track[i%lenTrack] == '-':
				action = '-'
			if action == '+':
				power += 1
			if action == '-' and power > 0:
				power -= 1
			totalPower += power
		win = False
		if totalPower > minPower:
			win = True
			winningPlans += 1
		print([z, plan, totalPower, win])
print(winningPlans)