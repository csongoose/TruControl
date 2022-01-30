

import serial
import json
import yaml
from urllib.request import urlopen

def printDebug(msg):
    global debugMode
    if (debugMode == True):
        print(msg)

def getTruckPrevStateIO(chckState):
    response = urlopen(url) # open the url

    data_json = json.loads(response.read()) # load the response into a dictionary

    data_truck = data_json.get('truck') # get the values from the truck

    if (data_truck.get(chckState) == True):
        return 1
    else:
        return 0

def writeArduino(msg):
    arduino.write(msg)
    arduino.write(b'\n')

# begin file reading from config.yml

with open('config.yml', 'r') as ymlRead:
    configFile = yaml.safe_load(ymlRead)

    # read the configuration section
cfg = configFile['CONFIGURATION']

    # read the url from config file
urlRead = cfg['urlfortelemetry']

    # read the arduino port from the config file
portRead = cfg['arduinoport']

    # read if the debug mode is active
debugMode = cfg['debugmode']

    # command output for debugging
print('Url read from config.yml: ', urlRead)
print('Port read from config.yml:', portRead)

print('')
print('Establishing connection with Arduino...')

url = urlRead   # telemetry server's output url
loop = 5    # used for the infinite loop (used an integer for the possibility of later expansion)
arduino = serial.Serial(port=portRead, baudrate=9600, timeout=.1)     # open the port with the arduino

print('Arduino connection established!')

printDebug('Setting initial variable values...')

# set initial states of variables (used for saving the amount of commands on the serial port)
prevGameState = 1
blPrevState = 3
hbPrevState = getTruckPrevStateIO('lightsBeamHighOn')
parkingLightPrevState = getTruckPrevStateIO('lightsParkingOn')
lowBeamPrevState = getTruckPrevStateIO('lightsBeamLowOn')
airPressureWarningPrevState = getTruckPrevStateIO('airPressureWarningOn')
batteryWarningPrevState = getTruckPrevStateIO('batteryVoltageWarningOn')
parkingBrakePrevState = getTruckPrevStateIO('parkBrakeOn')
fuelWarningPrevState = getTruckPrevStateIO('fuelWarningOn')
retarderPrevState = 5

print('Connecting to telemetry server... (if an error or exception occurs after this, check if your telemetry server is running and/or config file is set correctly)')
response = urlopen(url)         # working on a better method
print('Url connection succeeded!')
print('Checking for game...')

# check if game is running (counts as connected, if the player is spawned in)
while True:
    response = urlopen(url)
    data_json = json.loads(response.read())
    data_game = data_json.get('game')
    gameState = data_game.get('connected')
    if ((prevGameState == 1) and (gameState == False)):
        print('Game is not connected (or not running).')
        prevGameState = 0
    elif (gameState == True):
        print('Game is connected and running, you are good to go!')
        prevGameState = 1
        break

printDebug('Begin printing the game output: (if you want to disable this, set the debugmode to False in the config.yml')

while loop > 0: # begin the infinite loop
    response = urlopen(url) # open the url

    data_json = json.loads(response.read()) # load the response into a dictionary

    data_truck = data_json.get('truck') # get the values from the truck

    # get left blinker state
    leftBlinkerState = data_truck.get('blinkerLeftOn')

    # get right blinker state
    rightBlinkerState = data_truck.get('blinkerRightOn')

    # get high beam state
    highBeamState = data_truck.get('lightsBeamHighOn')

    # get parking lights state
    parkingLightState = data_truck.get('lightsParkingOn')

    # get low beams state
    lowBeamState = data_truck.get('lightsBeamLowOn')

    # get air pressure warning light state
    airPressureWarningState = data_truck.get('airPressureWarningOn')

    # get battery warning light state
    batteryWarningState = data_truck.get('batteryVoltageWarningOn')

    # get parking brake state
    parkingBrakeState = data_truck.get('parkBrakeOn')

    # get fuel warning state
    fuelWarningState = data_truck.get('fuelWarningOn')

    # get retarder state
    retarderState = data_truck.get('retarderBrake')

    if ((leftBlinkerState == False) and (rightBlinkerState == False) and (blPrevState !=0)):  # test for none on
        writeArduino(b'boff')
        blPrevState = 0           # set the state                 # repeated every cycle
        printDebug('Blinkers are off, code sent!')
    if ((leftBlinkerState == True) and (rightBlinkerState == False) and (blPrevState !=1)):   # test for left on
        writeArduino(b'lbon')
        blPrevState = 1
        printDebug('Left blinker on, code sent!')
    if ((leftBlinkerState == False) and (rightBlinkerState == True) and (blPrevState !=2)):   # test for right on
        writeArduino(b'rbon')
        blPrevState = 2
        printDebug('Right blinker on, code sent!')
    if ((leftBlinkerState == True) and (rightBlinkerState == True) and  (blPrevState !=3)):   # test for both (hazards) on
        writeArduino(b'hzon')
        blPrevState = 3
        printDebug('Hazards on, code sent!')

    if ((highBeamState == False) and (hbPrevState !=0)):    # test for high beams off
        writeArduino(b'hboff')
        hbPrevState = 0
        printDebug('High beams off, code sent!')
    if ((highBeamState == True) and (hbPrevState !=1)):     # test for high beams on
        writeArduino(b'hbon')
        hbPrevState = 1
        printDebug('High beams on, code sent!')

    if ((parkingLightState == False) and (parkingLightPrevState !=0)):    # test for parking lights
        writeArduino(b'ploff')
        parkingLightPrevState = 0
        printDebug('Parking lights off, code sent!')
    if((parkingLightState == True) and (parkingLightPrevState !=1)):
        writeArduino(b'plon')
        parkingLightPrevState = 1
        printDebug('Parking lights on, code sent!')

    if ((lowBeamState == False) and (lowBeamPrevState !=0)):              # test for low beams
        writeArduino(b'lowboff')
        lowBeamPrevState = 0
        printDebug('Low beams off, code sent!')
    if ((lowBeamState == True) and (lowBeamPrevState !=1)):
        writeArduino(b'lowbon')
        lowBeamPrevState = 1
        printDebug('Low beams on, code sent!')

    if ((airPressureWarningState == False) and (airPressureWarningPrevState !=0)): # test for air pressure warning
        writeArduino(b'apoff')
        airPressureWarningPrevState = 0
        printDebug('Air pressure warning off, code sent!')
    if ((airPressureWarningState == True) and (airPressureWarningPrevState !=1)):
        writeArduino(b'apon')
        airPressureWarningPrevState = 1
        printDebug('Air pressure warning on, code sent!')

    if ((batteryWarningState == False) and (batteryWarningPrevState !=0)):          # test for battery warning
        writeArduino(b'bwoff')
        batteryWarningPrevState = 0
        printDebug('Battery voltage warning off, code sent!')
    if ((batteryWarningState == True) and (batteryWarningPrevState !=1)):
        writeArduino(b'bwon')
        batteryWarningPrevState = 1
        printDebug('Battery voltage warning on, code sent!')

    if ((parkingBrakeState == False) and (parkingBrakePrevState !=0)):            # test for parking brake
        writeArduino(b'pboff')
        parkingBrakePrevState = 0
        printDebug('Parking brake off, code sent!')
    if ((parkingBrakeState == True) and (parkingBrakePrevState !=1)):
        writeArduino(b'pbon')
        parkingBrakePrevState = 1
        printDebug('Parking brake on, code sent!')

    if ((fuelWarningState == False) and (fuelWarningPrevState !=0)):
        writeArduino(b'fuwoff')
        fuelWarningPrevState = 0
        printDebug('Fuel warning off, code sent!')
    if ((fuelWarningState == True) and (fuelWarningPrevState !=1)):
        writeArduino(b'fuwon')
        fuelWarningPrevState = 1
        printDebug('Fuel warning on, code sent!')

    if ((retarderState == 0) and (retarderPrevState !=0)):
        writeArduino(b'retoff')
        retarderPrevState = retarderState
        printDebug('Retarder off, code sent!')
    if ((retarderState > 0) and (retarderPrevState < 1)):
        writeArduino(b'reton')
        retarderPrevState = retarderState
        printDebug('Retarder on, code sent!')