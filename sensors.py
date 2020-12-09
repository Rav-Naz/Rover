import ev3_dc as ev3
import struct

class UltrasonicSensor:

    def GetDistanceInCm(port, daisyChainLayer, ev3Instance: ev3):
        port = port -1
        ops = b''.join((
            ev3.opInput_Device,  # operation
            ev3.READY_SI,  # CMD
            ev3.LCX(daisyChainLayer),  # LAYER
            ev3.LCX(port),  # NO
            ev3.LCX(5),  # TYPE (EV3-Touch)
            ev3.LCX(0),  # MODE (Touch)
            ev3.LCX(1),  # VALUES
            ev3.GVX(0)  # VALUE1 (output)
        ))
        reply = ev3Instance.send_direct_cmd(ops, global_mem=4)
        distance = struct.unpack('<f', reply)[0]
        print(distance)