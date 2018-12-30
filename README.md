# MC1000A-Python
Python wrapper for serial port communication with Thorlabs MC1000A Chopper Motor.

See example.py for a usage example.

Currently, the program assumes that the motor has previously been manually setup with the proper disc parameters. Note that the "spin speeds" used by the motor refer to the repetition rate of the slits on the chopper disc, NOT the actual rotations/sec of the axel, which is why prior calibration is important. See Thorlabs manual (pg 17) for more details on the serial port connection. 
