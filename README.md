# TruControl
an external arduino dashboard project for ETS2


You will need Funbit's telemetry server for this. https://github.com/Funbit/ets2-telemetry-server

The config.yml file contains the server's access url (that you need to set) and the port for the arduino (COM3 by default).

The project is fully open source, you can do anything what you want with it, although it would be nice if you could send me a message when you do it.

The commandline for the arduino can be found in the arduino directory.

P.S. The software is still under heavy developement, and I had zero idea about python until this project, so forgive me for any mistakes I have made.

## Arduino setup

Currently 2 pins are used:
-Left blinker is pin number ***12***
-Right blinker is pin number ***13***

## Known issues

-Periodic lag occurs randomly when reading the telemetry (Still working on what causes it)
