"""
Created by: Jonathan Van Schenck
Updated: 12/26/2018
"""

import serial, time

class CHOPPER:
	def __init__(self,port="COM1",verbose=False):
		self.ser = serial.Serial(port=port,baudrate=19200,timeout=1)
		self.verbose = verbose
    		self.pauseTime = 0.5
		
	def close(self):
		self.ser.close()
		
	def printTermial(self):
		self.ser.write("\r".encode())
		print(self.ser.read(1000).decode())
		
	def toggleSpin(self):
		self.ser.write("R".encode())
		mes = self.ser.read(1000).decode()
		if self.verbose:
			print(mes)
			
	def startSpin(self):
		if not self.getSpinMessage():
			self.toggleSpin()
	
	def stopSpin(self):
		if self.getSpinMessage():
			self.toggleSpin()
		
	def getSpinMessage(self):
		self.ser.write("\r".encode())
		mes = self.ser.read(1000).decode()
		res = (mes.splitlines())[-10][-4:-1]
		if self.verbose:
			print(mes)
		return(res == " On")
		
	def getSpinValue(self):
		self.ser.write("\r".encode())
		mes = self.ser.read(1000).decode()
		res = (mes.splitlines())[-7][-5:-1]
		if self.verbose:
			print(mes)
		return(int(res))	
		
	def setSpinValue(self,val):
		if val>1000 or val<20:
			raise Exception("Unable to Spin at requested speed")
		self.ser.write("I".encode())
		time.sleep(self.pauseTime)
		for i in str(int(val)):
			self.ser.write(i.encode())
			time.sleep(self.pauseTime)
		self.ser.write("\r".encode())
		time.sleep(self.pauseTime)
		mes = self.ser.read(1000).decode()
		if self.verbose:
			print(mes)
