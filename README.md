# TruControl
An external arduino dashboard project for ETS2

***Version 0.1.3***


You will need Funbit's telemetry server for this. https://github.com/Funbit/ets2-telemetry-server

The config.yml file contains the server's access url (that you need to set) and the port for the arduino (COM3 by default).

The project is fully open source, you can do anything what you want with it, although it would be nice if you could send me a message if you do it.

The commandline for the arduino can be found in the arduino directory.

P.S. The software is still under heavy developement.

## PC setup

* First, install Funbit's telemetry server and start it up

* If you simply want to run the software without modifying it, download Trucontrolexec folder

* Set config.yml according to your telemetry server and arduino port

* Start up TruControl_x.x.x.exe and the game

* Enjoy!

## Arduino setup

* Simply upload the .ino file to your arduino. (tested on Leonardo and UNO)

* Current pinout: (can be changed in the arduino file's define block)
  * **13:** Right blinker
  * **12:** Left blinker
  * **11:** High beams
  * **10:** Low beams
  * **9:** Parking lights
  * **8:** Air pressure warning light
  * **7:** Battery warning light
  * **6:** Parking brake
  * **5:** Fuel warning light
  * **4:** Retarder indicator light

## Config.yml

The software settings can be changed within the file. Explanation is provided with every line.

## Changelog

### Version 0.1.0
* Original version

* Only blinkers are integrated

### Version 0.1.1
* Added new high beams output

* Added executable file

### Version 0.1.2
* Cleaned up code

* Added several more outputs:

  * Parking lights
  * Low beams
  * Air pressure warning
  * Battery warning
  * Parking brake
  * Fuel warning light
  * Retarder light

### Version 0.1.3
* Reformatted code
* Added support for automatic retarder (can be changed in config.yml)
* Added support for dashboard indicator lights to work with or independently of the truck ignition (handbrake, retarder, air pressure warning etc.)
* Added support for external lights to work with or independently of the truck ignition

## Known issues
* Periodic lag occurs randomly when reading the telemetry (Still working on what causes it)
* When starting up the software, you have to start with a truck which has everything switched off, to avoid issues
