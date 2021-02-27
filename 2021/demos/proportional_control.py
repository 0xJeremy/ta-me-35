import hub, utime, math

# Create motor and make motor pairs
motorB = hub.port.B.motor
motors = hub.port.A.motor.pair(motorB)

# Set motor speed to 0
motors.pwm(0, 0)
​
# Setup up Ultrasonic sensor
sonar = hub.port.C.device
​
# Control parameters
kp = 1.8
setPoint = 10
​
while True:
    try:
        # Get distance
        distance = sonar.get()[0]

        # Find "error" between desired and actual
        error = setPoint - distance

        # Calculate the speed
        # speed = -1 * kp * error
        speed = math.floor(-1 * kp * error)

        # Set the motor speed
        p.pwm(speed, -speed)
        
        utime.sleep(0.005)
    except:
        continue
