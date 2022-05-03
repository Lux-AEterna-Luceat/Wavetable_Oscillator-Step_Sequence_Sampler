import SSSampler.sSSampler as ss


MODULE_NAME	= 'Drums'
PATH		= 'Samples/Drums/default'
TEMPO		= 150
DIVISION	= [4,4]

def playKeys(*k):
	print(MODULE_NAME+':', k)
	ss.playKeys(*k)
	return

def play():
	ss.init(PATH, TEMPO, DIVISION)

	playKeys()
	playKeys()
	playKeys()
	playKeys()
	playKeys()
	playKeys()
	playKeys()
	playKeys()

	# 0:
	t = 0
	while t < 15:
		playKeys('Kick')
		playKeys()
		playKeys('Hat')
		playKeys()
		playKeys('Snare')
		playKeys()
		playKeys('Hat')
		playKeys()
		t += 1

	# 15:
	playKeys('Kick')
	playKeys()
	playKeys('Kick')
	playKeys()
	playKeys('Kick')
	playKeys('Kick')
	playKeys('Kick')
	playKeys('Kick')

	return
