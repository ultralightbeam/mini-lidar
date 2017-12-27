#!/usr/bin/env python

import matplotlib.pyplot as plt
import serial
import sys
import time
import numpy as np

BAUDRATE = 115200


if __name__ == '__main__':

	serial_port = sys.argv[1]
	ser = serial.Serial(serial_port, timeout=0)
	print(ser.name)
	ser.baudrate = BAUDRATE
	#plt.figure

	print('go')

	fig = plt.figure()

	while 1:
		ser.write('N')
		line = ser.readline()
		time.sleep(.1)
		#print ' '
		print(line)
		v = np.array(line.split(',')[:-1]).astype(float)
		v = v[50:300]
		#print(v)
		plt.clf()
		plt.plot(v)
		plt.draw()
		plt.pause(1e-17)


	ser.close()
		#plt.plot(v)
		#plt.show()
