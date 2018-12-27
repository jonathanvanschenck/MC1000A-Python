# MC1000A-Python
Python wrapper for serial port communication with Thorlabs MC1000A Chopper Motor.

Usage example:

ch = chopper.CHOPPER(verbose=True
ch.printTermial()
ch.setSpinValue(100)
ch.startSpin()
ch.printTermial()
ch.stopSpin()
ch.close()
