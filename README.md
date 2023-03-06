# openspectrym
add multicolor to a 3d printer by coating its filament with ink

There are many different mechanisms that are able to dispense ink onto filament.

Passive
Servo and marker
Peristaltic pump
Syringe pump
Inkjet

This repo contains two variations of a peristaltic pump mechanism (3mmSpectrym and 4mmSpectrym). 

The difference betweent these two is the guage of silicone tube that they accept and the size of their bearings. 3mmSpectrym accepts a 1mm ID x 3mm OD silicone tube with a 1/2in bearing and 4mmSpectrym accepts a 2mm ID x 4mm OD tube with a 3/4in bearing. On top of this 4mmSpectrym requires a 1mmID x 3mm OD silicone tube to serve as an adapter as well as a 1mm ID x 3mm OD PTFE tube to serve as a nozzle. 

Both pumps require a .6mm ID x 1mm OD PTFE tube that is insterted into an ink bottle to create a leak proof seal.

There are tradeoffs between these two pumps. 3mmSpectrym is smaller, easier to print, more precise. On the other hand 4mm spectrym might have more reliability due to larger pump components.

Both pumps currently suffer from a "backflow" issue.

Imagine a straw is sitting flat on a desk and its filled with water. What direction does the water flow when you pinch the center of the straw? The answer is both ways. Now imagine you quit pinching the straw. What direction does the water flow? The answer is back to the center. This concept holds true for a peristaltic pump. There is a section inside a peristaltic pump where the rollers dont make contact with the tube. When a roller enters this section it quits displacing fluid which draws the fluid back into the tube. Normally with a bigger pump this isnt an issue, but when you are dispensing fractions of MLs at a time this creates time gaps where ink is not being dispensed.

This issue could potentially be solved with a small check valve. Alternatively it could be solved by counting stepper motor steps or using a sensor to speed up the rotor during backflow periods. 

Parts list
https://www.amazon.com/shop/blake3dcake/list/3DG12XG11M4M1?ref_=cm_sw_r_cp_ud_aipsflist_aipsfblake3dcake_S4P14D43RQJ0KXA37WWG

Setting up A4988 stepper motor drivers
https://lastminuteengineers.com/a4988-stepper-motor-driver-arduino-tutorial/

Schematic
![spectrym (1)](https://user-images.githubusercontent.com/127003963/223009756-63e2231f-26ce-4845-9071-10230715e386.png)
