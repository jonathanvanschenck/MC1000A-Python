"""
Created by: Jonathan Van Schenck
Updated: 12/26/2018
"""

import serial, time

class CHOPPER:
	"""
	Class to control a Thorlabs MC1000A Chopper motor.
	Required Initalization values:
	port:			reference to the serial port used by the computer
	verbose:		Boolean to control if the MC1000A's responses are 
				  echoed into the terminal.
			 
	Class variables:
	.ser:			The pySerial connection to the MC1000A
	.verbose: 		Boolean to control if the MC1000A's responses are
				  echoed into the terminal
	.pauseTime:		A throttle control for the serial port write rate
				  given in seconds. Can modify as needed
	
	Methods:
	.close()		Wrapper for serial.Serial.close(), closes the serial
				  connection
	.printTerminal()	Prints the current MC1000A termial state into the 
				  python termial
	.toggleSpin()		Toggles whether the chopper is spinning
	.startSpin()		Starts chopper rotation, if currently stopped
	.stopSpin()		Ends chopper rotation, if currently spinning
	.getSpinMessage()	Returns True if the chopper is rotating
	.getSpinValue()		Returns an integer with the chopping rate in Hz
				  (NOT the rotation rate)
	.setSpinValue(val)	Sets int(val) as the new chopping rate in Hz
				  (NOT the rotation rate)
	.write(message)		a
	"""
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
			
	def write(self,message):
		for i in str(message):
			time.sleep(self.pauseTime)
			self.ser.write(i.encode())
		time.sleep(self.pauseTime)
		if self.verbose:
			self.printTerminal()
		
