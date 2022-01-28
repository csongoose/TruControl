

import serial
import json
import yaml
from urllib.request import urlopen


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

prevGameState = 1
prevState = 3   # used to save the amount of commands on the serial port (blinkers and hazards)
hbPrevState = 1 # used to save the amount of commands on the serial port (high beams)

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

if (debugMode == True):
    print('Begin printing the game output: (if you want to disable this, set the debugmode to False in the config.yml')

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

    if ((leftBlinkerState == False) and (rightBlinkerState == False) and (prevState !=0)):  # test for none on
        arduino.write(b'd')     # send message to arduino
        prevState = 0           # set the state                 # repeated every cycle
        if (debugMode == True):
            print('Blinkers are off, code sent!')    # send message to console

    if ((leftBlinkerState == True) and (rightBlinkerState == False) and (prevState !=1)):   # test for left on
        arduino.write(b'e')
        prevState = 1
        if (debugMode == True):
            print('Left blinkers are on, code sent!')

    if ((leftBlinkerState == False) and (rightBlinkerState == True) and (prevState !=2)):   # test for right on
        arduino.write(b'f')
        prevState = 2
        if (debugMode == True):
            print('Right blinkers are on, code sent!')

    if ((leftBlinkerState == True) and (rightBlinkerState == True) and  (prevState !=3)):   # test for both (hazards) on
        arduino.write(b'g')
        prevState = 3
        if (debugMode == True):
            print('Hazard lights are on, code sent!')

    if ((highBeamState == False) and (hbPrevState !=0)):    # test for high beams off
        arduino.write(b'b')
        hbPrevState = 0
        if (debugMode == True):
            print('High beams are off, code sent!')

    if ((highBeamState == True) and (hbPrevState !=1)):     # test for high beams on
        arduino.write(b'c')
        hbPrevState = 1
        if (debugMode == True):
            print('High beams are on, code sent!')