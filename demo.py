import pyRAPL
import datetime, time


pyRAPL.setup() 
rapl_meter = pyRAPL.Measurement('bar')

rapl_meter.begin_long()
while True:
	cmd = input()
	if cmd == 'q':
		break

rapl_meter.end_long()
print(rapl_meter.result)
