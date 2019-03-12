'''

Created on 25.02.2019



@author: ED, AH

'''




class TMCM_1160(object):

     

     AP_TargetPosition               = 0

     AP_ActualPosition               = 1

     AP_TargetSpeed                  = 2

     AP_ActualSpeed                  = 3

     AP_MaxVelocity                  = 4

     AP_MaxAcceleration              = 5

     AP_MaxCurrent                   = 6

     AP_StandbyCurrent               = 7

     AP_PositionReachedFlag          = 8

     AP_HomeSwitchState              = 9

     AP_RightLimitSwitchState        = 10 

     AP_LeftLimitSwitchState         = 11

     AP_RightLimitSwitchDisable      = 12

     AP_LeftLimitSwitchDisable       = 13

     AP_MinimumSpeed                 = 130

     AP_ActualAcceleration           = 135

     AP_RampMode                     = 138

     AP_MicrostepResolution          = 140

     AP_SoftStopFlag                 = 149

     AP_EndSwitchPowerDownMode       = 150

     AP_RampDivisor                  = 153

     AP_PulseDivisor                 = 154

     AP_StepInterpolationEnable      = 160

     AP_DoubleStepEnable             = 161

     AP_ChopperBlankTime             = 162

     AP_ConstantTOffMode             = 163

     AP_DisableFastDecayComperator   = 164

     AP_ChopperHysteresisEnd         = 165

     AP_ChopperHysteresisStart       = 166

     AP_ChopperOffTime               = 167

     AP_SmartEnergyCurrentMinimum    = 168

     AP_SmartEnergyCurrentDownStep   = 169

     AP_SmartEnergyHysteresis        = 170

     AP_SmartEnergyCurrentUpStep     = 171

     AP_SmartEnergyHysteresisStart   = 172

     AP_StallGuard2FilterEnable      = 173

     AP_StallGuard2Threshold         = 174

     AP_SlopeControlHighSide         = 175

     AP_SlopeControlLowSide          = 176

     AP_ShortProtectionDisable       = 177

     AP_ShortDetectionTimer          = 178

     AP_VSense                       = 179

     AP_SmartEnergyActualCurrent     = 180

     AP_StopOnStall                  = 181

     AP_SmartEnergyThresholdSpeed    = 182

     AP_SmartEnergySlowRunCurrent    = 183

     AP_RandomTOffMode               = 184

     AP_ReferenceSearchMode          = 193

     AP_ReferenceSearchSpeed         = 194

     AP_ReferenceSwitchSpeed         = 195

     AP_EndSwitchDistance            = 196

     AP_LastReferencePosition        = 197

     AP_BoostCurrent                 = 200

     AP_Freewheeling                 = 204

     AP_ActualLoadValue              = 206

     AP_ExtendedErrorFlags           = 207

     AP_TMC262ErrorFlags             = 208

     AP_EncoderPosition              = 209

     AP_EncoderPrescaler             = 210

     AP_MaximumEncoderDeviation      = 212

     AP_PowerDownDelay               = 214

     AP_AbsoluteResolverValue        = 215

     AP_ExternalEncoderPosition      = 216

     AP_ExternalEncoderPrescaler     = 217

     AP_MaxExternalEncoderDeviation  = 218

     AP_StepDirectionMode            = 254




     FLAG_POSITION_END               = 0x00004000



     def __init__(self, connection):

        self.connection = connection

        self.motor = 0

        self.variables = 2




    # axis parameter access 

     def axisParameter(self, apType):
          return self.connection.axisParameter(apType, self.motor)

     def setAxisParameter(self, apType, value):
          self.connection.setAxisParameter(apType, self.motor, value)

     # global parameter access 

     def globalParameter(self, gpType):
          return self.connection.globalParameter(gpType, self.motor)

     def setGlobalParameter(self, gpType, value):
          self.connection.setGlobalParameter(gpType, self.motor, value)

     def userVariable(self, variableNo):
          return self.connection.globalParameter(variableNo, self.variables)

     def setUserVariable(self, variableNo, value):
          self.connection.setGlobalParameter(variableNo, self.variables, value)  


     # standard functions 

     def moveToPosition(self, position):
          self.setAxisParameter(self.AP_TargetPosition, position)

     def targetPosition(self):
          return self.axisParameter(self.AP_TargetPosition)

     def actualPosition(self):
          return self.axisParameter(self.AP_ActualPosition)
   
     def setActualPosition(self, position):
          return self.setAxisParameter(self.AP_ActualPosition, position)

     def rotate(self, velocity):
          self.setAxisParameter(self.AP_TargetSpeed, velocity)

     def actualSpeed(self):
          return self.axisParameter(self.AP_ActualSpeed)


     # Stallguard functions 
     def motorRunCurrent(self, runCurrent):
          self.setAxisParameter(self.AP_MotorRunCurrent, runCurrent)

     def motorStandbyCurrent(self, standbyCurrent):
          self.setAxisParameter(self.AP_MotorStandbyCurrent, standbyCurrent)

     def stallguard2Filter(self, filter):
          self.setAxisParameter(self.AP_StallGuard2FilterEnable, filter)

     def stallguard2Threshold(self, threshold):
          self.setAxisParameter(self.AP_StallGuard2Threshold, threshold)

     def stopOnStall(self, stopValue):
          self.setAxisParameter(self.AP_StopOnStall, stopValue)



     # helpful functions 




     def maxVelocity(self):
          return self.axisParameter(self.AP_MaxVelocity)

     def setMaxVelocity(self, maxVelocity):
          self.setAxisParameter(self.AP_MaxVelocity, maxVelocity)

     def maxAcceleration(self):
          return self.axisParameter(self.AP_MaxAcceleration)

     def setMaxAcceleration(self, maxAcceleration):
          self.setAxisParameter(self.AP_MaxAcceleration, maxAcceleration)

     def maxCurrent(self):
          return self.axisParameter(self.AP_MaxCurrent)

     def setMaxCurrent(self, maxCurrent):
          self.setAxisParameter(self.AP_MaxCurrent, maxCurrent)

     def acceleration(self):
          return self.axisParameter(self.AP_Acceleration)

     def setTargetSpeed(self, speed):
          return self.axisParameter(self.AP_SetTargetSpeed, speed)

     def setAcceleration(self, acceleration):
          self.setAxisParameter(self.AP_Acceleration, acceleration)

     def targetReachedSpeed(self):
          return self.axisParameter(self.AP_TargetReachedSpeed)

     def setTargetReachedSpeed(self, velocity):
          self.setAxisParameter(self.AP_TargetReachedSpeed, velocity)

     def positionReached(self):
          return ((self.statusFlags() & self.FLAG_POSITION_END) != 0)

     def setRampMode(self, mode):
          return self.axisParameter(self.AP_RampMode, mode)

     def statusFlags(self):
          return self.axisParameter(self.AP_StatusFlags)

     def analogInput(self, x):
          return self.connection.analogInput(x)

     def digitalInput(self, x):
          return self.connection.digitalInput(x)

     def showMotionConfiguration(self):
          print("Motion configuration:")
          print("\tMax velocity: " + str(self.maxSpeed()))
          print("\tAcceleration: " + str(self.acceleration()))
          print("\tRamp mode: " + ("position" if (self.rampEnabled()==0) else "velocity"))
          print("\tTarget reached velocity: " + str(self.targetReachedSpeed()))
