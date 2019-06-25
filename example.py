import chopper,time

ch = chopper.CHOPPER(verbose=True)
ch.printTerminal()
ch.setSpinValue(100)
ch.startSpin()
time.sleep(10)#Allow time for chopper motor to reach stable spin speed
ch.stopSpin()
ch.close()
