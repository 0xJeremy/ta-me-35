import hub, utime

dial = hub.port.B.motor
dial.mode(2)
dial.float()

utime.sleep(0.5)
Kp = 200
sonar = hub.port.A.device

while True:
    try:
        pitch = sonar.get()[0]
        hub.sound.beep(Kp*pitch, 100, 1)
        hub.sound.volume((dial.get()[0]))
        utime.sleep(0.05)
    except:
        continue



# import hub, utime
# utime.sleep(0.5)
# Kp = 100
# Kp2 = 10
# sonar1 = hub.port.A.device
# sonar2 = hub.port.B.device
# while True:
#     try:
#         pitch = sonar1.get()[0]
#         duration = sonar2.get()[0]
#         hub.sound.beep(Kp*pitch, Kp2 *duration, 1)
#         hub.sound.volume((dial.get()[0]))
#         utime.sleep(0.05)
#     except:
#         continue
