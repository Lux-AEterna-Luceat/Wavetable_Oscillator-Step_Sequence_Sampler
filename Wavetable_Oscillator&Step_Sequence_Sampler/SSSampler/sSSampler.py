import pygame
import time

pygame.init()
pygame.mixer.init()

def init(path, tempo, division):
	global PATH, TIME_DELAY
	PATH		= path
	TIME_DELAY	= 60/(tempo*division[1])

	return

def playKeys(*k):
	for var in k:
		samp=pygame.mixer.Sound(PATH+'/'+var+'.wav')
		samp.play()
	time.sleep(TIME_DELAY)
	return

def releaseKeys():
	pygame.mixer.stop()
	return
