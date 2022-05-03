import wave
import pyaudio
import struct
import numpy
import Dict.notes as notes
import time


# Audio Parameters:
CHUNK		= 2048 #: Low to about 20Hz
FORMAT		= pyaudio.paInt16
CHANNELS	= 2
RATE		= 44100


# Audio Initialization:
audio	= pyaudio.PyAudio()
stream	= audio.open(
	format				= FORMAT,
	channels			= CHANNELS,
	rate				= RATE,
	frames_per_buffer	= CHUNK,
	output				= True)


# Wavetable Oscillator Initialization:
def init(sample, tempo, division):
	waveFile	= wave.open(sample, 'r')
	dataIn		= waveFile.readframes(CHUNK*100)


	# Global Variables:
	global TEMPO, DIVISION, TIME_DELAY, TWELVETONE, lenOrig, xOrig, dataOrig

	TEMPO		= tempo
	DIVISION	= division

	TIME_DELAY	= 60/(TEMPO*DIVISION[1])
	TWELVETONE	= 2**(1/12)

	lenOrig		= int(len(dataIn)/2)
	xOrig		= numpy.arange(lenOrig)
	dataOrig	= numpy.array(struct.unpack(str(lenOrig)+'h', dataIn))


	return


def playKey(key, volume, steps):
	lenAft	= int(RATE*2/(440*TWELVETONE**notes.KEY[key]))
	xAft	= numpy.arange(0, lenOrig, lenOrig/lenAft)
	dataAft	= numpy.asarray(numpy.interp(xAft, xOrig, dataOrig)*volume, 'int16')

	dataOut	= bytes(dataAft)

	t = 0
	T = 120*steps*RATE/(lenAft*TEMPO*DIVISION[1])
	while t < T:
		stream.write(dataOut)
		t += 1

	return

def delay(steps):
	time.sleep(TIME_DELAY*steps)
	return
