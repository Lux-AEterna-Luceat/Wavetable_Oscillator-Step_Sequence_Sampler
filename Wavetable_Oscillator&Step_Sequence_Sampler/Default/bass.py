import WtOsc.wtOsc as wtOsc


MODULE_NAME	= 'Bass'
PATH		= 'Shapes/HQ/HQ_SmoothInvSaw_Dist.wav'
TEMPO		= 150
DIVISION	= [4,4]


def playKey(key, volume, steps):
	print(MODULE_NAME+": (Key: '"+key+"')")
	wtOsc.playKey(key, volume, steps)
	return

def play():
	wtOsc.init(PATH, TEMPO, DIVISION)

	wtOsc.delay(8)

	# 0:
	t = 0
	while t < 2:
		playKey('F2', 0.2, 2)
		playKey('F3', 0.2, 2)
		t += 1

	# 1:
	t = 0
	while t < 2:
		playKey('G2', 0.2, 2)
		playKey('G3', 0.2, 2)
		t += 1

	# 2:
	t = 0
	while t < 2:
		playKey('A2', 0.2, 2)
		playKey('A3', 0.2, 2)
		t += 1

	# 3:
	t = 0
	while t < 2:
		playKey('G2', 0.2, 2)
		playKey('G3', 0.2, 2)
		t += 1
	
	# 4:
	t = 0
	while t < 2:
		playKey('F2', 0.2, 2)
		playKey('F3', 0.2, 2)
		t += 1

	# 5:
	t = 0
	while t < 2:
		playKey('G2', 0.2, 2)
		playKey('G3', 0.2, 2)
		t += 1

	# 6:
	t = 0
	while t < 4:
		playKey('G#2',0.2, 2)
		playKey('G#3',0.2, 2)
		t += 1

	# 8:
	t = 0
	while t < 2:
		playKey('A2', 0.2, 2)
		playKey('A3', 0.2, 2)
		t += 1

	# 9:
	t = 0
	while t < 2:
		playKey('G2', 0.2, 2)
		playKey('G3', 0.2, 2)
		t += 1
	
	# 10:
	t = 0
	while t < 2:
		playKey('F#2',0.2, 2)
		playKey('F#3',0.2, 2)
		t += 1
	
	# 11:
	t = 0
	while t < 2:
		playKey('D2', 0.2, 2)
		playKey('D3', 0.2, 2)
		t += 1

	# 12:
	t = 0
	while t < 2:
		playKey('F2', 0.2, 2)
		playKey('F3', 0.2, 2)
		t += 1

	# 13:
	t = 0
	while t < 2:
		playKey('G2', 0.2, 2)
		playKey('G3', 0.2, 2)
		t += 1

	# 14:
	t = 0
	while t < 4:
		playKey('A2', 0.2, 2)
		playKey('A3', 0.2, 2)
		t += 1

	return
