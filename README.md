# openspectrym
add multicolor to a 3d printer by coating its filament with ink (using markers or pumps)

Marker Version
![20230420_144810](https://user-images.githubusercontent.com/127003963/233473385-92e0e9a6-760b-47e6-aaa7-412ab179710c.jpg)
![20230420_144613](https://user-images.githubusercontent.com/127003963/233476764-a0f7af4e-0024-41f3-bd19-38e2c83b209c.jpg)

This device uses servo motors to position markers precisely so they brush against the filament.

The first step is to 3d print the mechanism (the files should not require support). The 'markerholder' pieces are designed for sharpie brand markers and require an M3 brass inserts as well as the orginal MG90s servo horn screws(theyre tiny so dont lose them!). A soldering iron can be used to heat up an insert and then press it into the plastic. Once inserted, M3 screws can be tightened to hold the markers in place. If you don't have a soldering iron consider using tape. If you want to use different markers consider designing new holders(dont forget to post them here). M3 sccrews and nuts can be used to secure everthing else in place.

The next step is to wire everything up.

Now you can hop into the code and calibrate your servo motors (more detail is commented out inside the code)

The device mounts to the side rail of an ender 3 (I have not tested other printers) https://www.youtube.com/shorts/5oh6Mta2isw

---------------------------------------------------------------------------------------------------------------------------------------------------------
Pump Variations (uses peristaltic pumps instead of markers)

Experimental. Do not expect an easy or seamless experience.

Known issues: 

Both pumps currently suffer from a "backflow" issue. This issue could potentially be solved with a small check valve. Alternatively it could be solved by counting stepper motor steps or using a sensor to speed up the rotor during backflow periods.

Alcohol inks and drying time. Alcohol inks dry very quick which can create longterm problems with clogging of silicone pumps. This issue can potentially be solved with a new formulation of ink. There are many common plastisizers that are used with PLA. A few of them have a very high boiling point. Mixing pigment with a plasticizer could create a very stable carrier of pigment that could be dispensed using the spectrym. Ask chatGPT? 

Things that can be added:

A plugin for octoprint can be created to control the pumps via Raspberry Pi. This method would allow you to integrate the pumps with Gcode and dispense ink precisely.

An integration directly into the hotend. Dispensing ink onto the filament shortly before it reaches the 'meltzone' could reduce the buffer region. (the spectrym mounted on the frame with 3 long tubes that go into the hotend)

![this](https://user-images.githubusercontent.com/127003963/224782383-03cb3734-0345-420c-be27-86226acdcdab.jpg)

This repo contains two variations of a peristaltic pump mechanisms (3mmSpectrym and 4mmSpectrym). 

The difference betweent these two is the guage of silicone tube that they accept and the size of their bearings. 3mmSpectrym accepts a 1mm ID x 3mm OD silicone tube with a 1/2in bearing and 4mmSpectrym accepts a 2mm ID x 4mm OD tube with a 3/4in bearing. On top of this 4mmSpectrym requires a 1mmID x 3mm OD silicone tube to serve as an adapter as well as a 1mm ID x 3mm OD PTFE tube to serve as a nozzle. 

Both pumps require a .6mm ID x 1mm OD PTFE tube that is insterted into an ink bottle to create a leak proof seal.

There are tradeoffs between these two pumps. 3mmSpectrym is smaller, easier to print, more precise. On the other hand 4mm spectrym might have more reliability due to larger pump components.

![spee](https://user-images.githubusercontent.com/127003963/224782675-06ac45fc-f5aa-43c2-ba5e-6577b91a5513.jpg)

Parts list
https://www.amazon.com/shop/blake3dcake/list/3DG12XG11M4M1?ref_=cm_sw_r_cp_ud_aipsflist_aipsfblake3dcake_S4P14D43RQJ0KXA37WWG

Step one is to print everything out. No support is needed.

Next M3 inserts should be added with a soldering iron (this includes the inserts on the rotors). Note that 4mmSpectrym cant accept inserts on its bottom side due to size constraints. This means youll have to thread small M3 screws directly into the plastic.

Next youll need to convert 3 28byj-48 stepper motors from unipolar to bipolar so they will work with the A4988 driver. To do this you need to take the back tab covering off of the motor. Next take a razer bladee and cut the circuit trace directly in the center. This trace should be connceted to the red wire. Cut the red wire so everything is nice and clean. Replace the cover and tape it back on with electrical tape (the tabs will probably be broken).

![spe](https://user-images.githubusercontent.com/127003963/224782807-ace81f34-5e4f-4370-996e-cc15141517da.jpg)

Now you can assemble and screw everything into place.

Next step is to set up current limiting on the A4988 motor driver. The 28byj-48 is rated for .1A continous so if you dont set current limiting on the driver you will fry the motor. This guide should help (also note the micro stepping section if you want to change that)
https://lastminuteengineers.com/a4988-stepper-motor-driver-arduino-tutorial/

Both spectrym models are designed with holders for Pinata alcohol inks. The bottles should fit nicely into the slots. Before inserting the bottles they need to be modified in order to be suitable for the system. The first modification is the nozzle on the ink bottle needs to be widened to 1mm in order to accept a ptfe tube. Use a small drillbit to enlarge the hole. Next you can insert the ptfe tubing (it should be a tight fit). Make sure to leave excess ptfe tubing sticking out in order to attach the silicone tube to it later. Lastly drill a very small hole in the rim of the bottle. This is neccisary to depressurize the bottle as liquid is being drawn out.

![ink](https://user-images.githubusercontent.com/127003963/224785386-740069fb-88d5-4dab-a94a-6ca0435681fb.jpg)

The next steps are to assemble the cirucit, upload the sketch to your Pi Pico, and hook it to the printer frame using locking nuts.

Parts list
https://www.amazon.com/shop/blake3dcake/list/3DG12XG11M4M1?ref_=cm_sw_r_cp_ud_aipsflist_aipsfblake3dcake_S4P14D43RQJ0KXA37WWG

Schematic
![spectrym (1)](https://user-images.githubusercontent.com/127003963/223009756-63e2231f-26ce-4845-9071-10230715e386.png)
