#!/usr/bin/env python3
'''the art of doing nothing'''

import ev3_dc as ev3
import sensors

my_ev3 = ev3.EV3(
    protocol=ev3.USB,
    host='00:16:53:5F:19:24'
)
my_ev3.verbosity = 1
my_ev3.sync_mode = ev3.SYNC
opticsensor = sensors.UltrasonicSensor
opticsensor.GetDistanceInCm(4, 0, my_ev3)  