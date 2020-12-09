#!/usr/bin/env python3
'''the art of doing nothing'''

import ev3_dc as ev3
import struct

my_ev3 = ev3.EV3(
    protocol=ev3.USB,
    host='00:16:53:5F:19:24'
)
my_ev3.verbosity = 1
my_ev3.sync_mode = ev3.SYNC
ops = b''.join((
    ev3.opInput_Device,  # operation
    ev3.READY_SI,  # CMD
    ev3.LCX(0),  # LAYER
    ev3.LCX(3),  # NO
    ev3.LCX(5),  # TYPE (EV3-Touch)
    ev3.LCX(0),  # MODE (Touch)
    ev3.LCX(1),  # VALUES
    ev3.GVX(0)  # VALUE1 (output)
))
reply = my_ev3.send_direct_cmd(ops, global_mem=4)
distance = struct.unpack('<f', reply)[0]

print(distance)   