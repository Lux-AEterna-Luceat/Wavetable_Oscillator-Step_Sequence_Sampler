import WtOsc.wtOsc as wtOsc


MODULE_NAME	= 'Lead'
PATH		= 'Shapes/HQ/HQ_SmoothInvSaw_2.wav'
TEMPO		= 150
DIVISION	= [4,4]
VOLUME		= 0.2


def playKey(key, steps):
	print(MODULE_NAME+": (Key: '"+key+"')")
	wtOsc.playKey(key, VOLUME, steps)
	return

def play():
	wtOsc.init(PATH, TEMPO, DIVISION)

	playKey('A4', 2)
	playKey('B4', 2)
	playKey('C5', 2)
	playKey('D5', 2)

	# 0:
	playKey('E5', 8)

	# 1:
	playKey('C5', 2)
	playKey('E5', 2)
	playKey('C5', 1)
	playKey('E5', 1)
	playKey('B4', 2)

	# 2:
	playKey('A4', 10)
	
	# 3:
	playKey('A4', 2)
	playKey('C5', 2)
	playKey('E5', 2)

	# 4:
	playKey('A5', 8)

	# 5:
	playKey('G5', 2)
	playKey('A5', 2)
	playKey('G5', 1)
	playKey('A5', 1)
	playKey('D5', 2)
	
	# 6:
	playKey('E5', 12)
	
	# 7:
	playKey('B5', 4)

	# 8:
	playKey('C6', 8)

	# 9:
	playKey('B5', 2)
	playKey('C6', 2)
	playKey('E6', 2)
	playKey('A5', 2)

	# 10:
	playKey('D6', 2)
	playKey('A5', 2)
	playKey('F#5', 2)
	playKey('D6', 2)

	# 11:
	playKey('A5', 2)
	playKey('F#5', 2)
	playKey('B5', 4)

	# 12:
	playKey('C6', 2)
	playKey('A5', 2)
	playKey('F5', 2)
	playKey('C6', 2)
	
	# 13:
	playKey('B5', 2)
	playKey('G5', 2)
	playKey('D5', 2)
	playKey('B5', 8)
	
	# 14:
	playKey('A5', 8)

	return
