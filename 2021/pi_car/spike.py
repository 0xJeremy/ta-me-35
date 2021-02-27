import hub
import time

commands: {
	b'f': [1, 1, -1, -1],
	b'l': [1, -1, 1, -1],
	b'r': [-1, 1, -1, 1],
	b'b': [-1, -1, 1, 1]
}
motors = [hub.port.B.device, hub.port.F.device, hub.port.a.Device, hub.port.E.device]

pi = hub.port.D
pi.mode(hub.port.MODE_FULL_DUPLEX)
pi.baud(115200)

for motor in motors:
	motor.pwm(0)

while True:
	cmd = pi.read(1)
	if cmd is None:
		print("no command...")
		time.sleep(1)
		continue

	motorDirections = commands.get(cmd, False)
	if motorDirections:
		for motorDirection, motor in zip(motorDirections, motors):
			motor.pwm(100*motorDirection)
	else:
		print("unable to find command in lookup table...")

	time.sleep(1)
