#!/usr/bin/python
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
print("Initializing:", os.getpid()) #: Print pid
from multiprocessing import Process


# Instruments:
import default_song.lead	as lead
import default_song.bass	as bass
import default_song.drums	as drums


def play():
	if __name__ == '__main__':
		Process(target = lead.play).start()
		Process(target = drums.play).start()
		Process(target = bass.play).start()

	return


play()
