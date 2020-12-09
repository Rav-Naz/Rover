#!/usr/bin/env python3

import usb.core
import struct

class EV3():
    def __init__(self):
        self._device = usb.core.find(idVendor=ID_VENDOR_LEGO, idProduct=ID_PRODUCT_EV3)
        if self._device is None:
            raise RuntimeError("No Lego EV3 found")
        serial_number = usb.util.get_string(self._device, self._device.iSerialNumber)
        if self._device.is_kernel_driver_active(0) is True:
            self._device.detach_kernel_driver(0)
        self._device.set_configuration()
        self._device.read(EP_IN, 1024, 100)

    def __del__(self): pass

    def send_direct_cmd(self, ops: bytes, local_mem: int=0, global_mem: int=0) -> bytes:
        cmd = b''.join([
            struct.pack('<h', len(ops) + 5),
            struct.pack('<h', 42),
            b'\x00',
            struct.pack('<h', local_mem*1024 + global_mem),
            ops
        ])
        self._device.write(EP_OUT, cmd, 100)
        print_hex('Sent', cmd)
        reply = self._device.read(EP_IN, 1024, 100)[0:5+global_mem]
        print_hex('Recv', reply)
        return reply

def print_hex(desc: str, data: bytes) -> None:
    print(desc + ' 0x|' + ':'.join('{:02X}'.format(byte) for byte in data) + '|')

ID_VENDOR_LEGO = 0x0694
ID_PRODUCT_EV3 = 0x0005
EP_IN  = 0x81
EP_OUT = 0x01
DIRECT_COMMAND_REPLY = b'\x00'
opNop = b'\x01'
my_ev3 = EV3()
ops_nothing = opNop
my_ev3.send_direct_cmd(ops_nothing)