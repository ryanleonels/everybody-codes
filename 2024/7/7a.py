#!/usr/bin/python3

plans = {}
fileHandle = open("everybody_codes_e2024_q07_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	plan = fileLine.split(':')[0]
	actions = fileLine.split(':')[1].split(',')
	n = len(actions)
	power = 10
	totalPower = 0
	for i in range(0,10):
		x = i % n
		if actions[x] == '+':
			power += 1
		if actions[x] == '-' and power > 0:
			power -= 1
		totalPower += power
	plans[plan] = totalPower
sortedPlans = dict(sorted(plans.items(), key=lambda item: item[1], reverse=True))
result = ''
for plan in sortedPlans:
	result += plan
print(result)