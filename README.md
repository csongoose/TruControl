# TruControl
An external arduino dashboard project for ETS2

***Version 1.1***


You will need Funbit's telemetry server for this. https://github.com/Funbit/ets2-telemetry-server

The config.yml file contains the server's access url (that you need to set) and the port for the arduino (COM3 by default).

The project is fully open source, you can do anything what you want with it, although it would be nice if you could send me a message if you do it.

The commandline for the arduino can be found in the arduino directory.

P.S. The software is still under heavy developement.

## PC setup

-First, install Funbit's telemetry server and start it up

-If you simply want to run the software without modifying it, download Trucontrolexec folder

-Set config.yml according to your telemetry server and arduino port

-Start up TruControl.exe and the game

-Enjoy!

## Arduino setup

-Simply upload the .ino file to your arduino. (tested on Leonardo and UNO)

Currently 3 pins are used:

-Left blinker is pin number ***12***

-Right blinker is pin number ***13***

-High beams is pin number ***11***

## Changelog

### Version 1.0
-Original version

-Only blinkers are integrated

### Version 1.1
-Added new high beams output

-Added executable file

## Known issues
-Periodic lag occurs randomly when reading the telemetry (Still working on what causes it)
