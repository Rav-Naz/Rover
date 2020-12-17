import ev3_dc as ev3
import struct

class NXTSensors(object):
    def ConstructCommand(self, daisyChainLayer, port, sensorType, sensorMode, values = 1, values1 = 0):
        return b''.join((
                        ev3.opInput_Device,  # operation
                        ev3.READY_SI,  # CMD
                        ev3.LCX(daisyChainLayer),  # LAYER
                        ev3.LCX(port),  # NO
                        ev3.LCX(sensorType),          # TYPE
                        ev3.LCX(sensorMode),          # MODE
                        ev3.LCX(values),          # VALUES
                        ev3.GVX(values1),          # VALUE1
                    ))

    class UltrasonicSensor(object):

        def __init__(self, ev3Instance, port, daisyChainLayer):
            self.ev3Instance = ev3Instance
            self.port = port - 1
            self.daisyChainLayer = daisyChainLayer
            
        def GetDistanceInCm(self):
            command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 5, 0)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

        def GetDistanceInInch(self):
            command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 5, 1)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

    class TouchSensor(object):

            def __init__(self, ev3Instance, port, daisyChainLayer):
                self.ev3Instance = ev3Instance
                self.port = port - 1
                self.daisyChainLayer = daisyChainLayer

            def isTouching(self):
                command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 1, 0)
                reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                return bool(struct.unpack('<f', reply)[0])
    
    class LightSensor(object):

            def __init__(self, ev3Instance, port, daisyChainLayer):
                self.ev3Instance = ev3Instance
                self.port = port - 1
                self.daisyChainLayer = daisyChainLayer

            def LightReflected(self):
                command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 2, 0)
                reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                return struct.unpack('<f', reply)[0]
            
            def LightAmbient(self):
                command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 2, 1)
                reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                return struct.unpack('<f', reply)[0]

    class SoundSensor(object):

                def __init__(self, ev3Instance, port, daisyChainLayer):
                    self.ev3Instance = ev3Instance
                    self.port = port - 1
                    self.daisyChainLayer = daisyChainLayer

                def SoundDB(self):
                    command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 3, 0)
                    reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                    return struct.unpack('<f', reply)[0]
                
                def SoundDBA(self):
                    command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 3, 1)
                    reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                    return struct.unpack('<f', reply)[0]

    class ColorSensor(object):

                def __init__(self, ev3Instance, port, daisyChainLayer):
                    self.ev3Instance = ev3Instance
                    self.port = port - 1
                    self.daisyChainLayer = daisyChainLayer

                def ColorReflected(self):
                    command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 4, 0)
                    reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                    return struct.unpack('<f', reply)[0]
                
                def ColorAmbient(self):
                    command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 4, 1)
                    reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                    return struct.unpack('<f', reply)[0]
                
                def Color(self):
                    command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 4, 2)
                    reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                    return struct.unpack('<f', reply)[0]
                
                def ColorGreen(self):
                    command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 4, 3)
                    reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                    return struct.unpack('<f', reply)[0]

                def ColorBlue(self):
                    command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 4, 4)
                    reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                    return struct.unpack('<f', reply)[0]

                def ColorRaw(self):
                    command = NXTSensors.ConstructCommand(self, self.daisyChainLayer, self.port, 4, 5)
                    reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
                    return struct.unpack('<f', reply)[0]

class EV3Sensors(object):
    def ConstructCommand(self, daisyChainLayer, port, sensorType, sensorMode, values = 1, values1 = 0):
        return b''.join((
                        ev3.opInput_Device,  # operation
                        ev3.READY_SI,  # CMD
                        ev3.LCX(daisyChainLayer),  # LAYER
                        ev3.LCX(port),  # NO
                        ev3.LCX(sensorType),          # TYPE
                        ev3.LCX(sensorMode),          # MODE
                        ev3.LCX(values),          # VALUES
                        ev3.GVX(values1),          # VALUE1
                    ))

    class TouchSensor(object):

        def __init__(self, ev3Instance, port, daisyChainLayer):
            self.ev3Instance = ev3Instance
            self.port = port - 1
            self.daisyChainLayer = daisyChainLayer
            
        def isTouched(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 16, 0)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return bool(struct.unpack('<f', reply)[0])

    class ColorSensor(object):

        def __init__(self, ev3Instance, port, daisyChainLayer):
            self.ev3Instance = ev3Instance
            self.port = port - 1
            self.daisyChainLayer = daisyChainLayer
            
        def ColorReflected(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 29, 0)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def ColorAmbient(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 29, 1)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def Color(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 29, 2)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

        def ColorReflectedRaw(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 29, 3)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

        def ColorRGBRaw(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 29, 4)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

        def ColorCalibration(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 29, 5)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

    class UltrasonicSensor(object):

        def __init__(self, ev3Instance, port, daisyChainLayer):
            self.ev3Instance = ev3Instance
            self.port = port - 1
            self.daisyChainLayer = daisyChainLayer
        
        def GetDistanceInCm(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 30, 0)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

        def GetDistanceInInch(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 30, 1)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def Listen(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 30, 2)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def GetDistanceInSICm(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 30, 3)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

        def GetDistanceInSIInch(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 30, 4)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def GetDistanceInDCCm(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 30, 5)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def GetDistanceInDCInch(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 30, 6)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

    class GyroSensor(object):

        def __init__(self, ev3Instance, port, daisyChainLayer):
            self.ev3Instance = ev3Instance
            self.port = port - 1
            self.daisyChainLayer = daisyChainLayer
        
        def GetAngle(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 32, 0)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def GetRate(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 32, 1)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def GetFast(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 32, 2)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def GetRateAndAngle(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 32, 3)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

        def Calibration(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 32, 4)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

    class IRSensor(object):
        def __init__(self, ev3Instance, port, daisyChainLayer):
            self.ev3Instance = ev3Instance
            self.port = port - 1
            self.daisyChainLayer = daisyChainLayer
        
        def Promixity(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 33, 0)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def Seeker(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 33, 1)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]
        
        def Remote(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 33, 2)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

        def RemoteAdvanced(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 33, 3)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]

        def Calibration(self):
            command = EV3Sensors.ConstructCommand(self, self.daisyChainLayer, self.port, 33, 5)
            reply = self.ev3Instance.send_direct_cmd(command, global_mem=4)
            return struct.unpack('<f', reply)[0]