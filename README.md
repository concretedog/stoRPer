# 

![Alt text](images/hexbin_sticker.png?raw=true "Title")

stoRPer, a modular adaptable AWD Pico based robot rover

![Alt text](images/IMG_20231103_135700.jpg?raw=true "Title")

![Alt text](images/IMG_20231103_135725.jpg?raw=true "Title")

[Check out the youtube video](https://youtu.be/Y8ddx1Og3Xw?feature=shared) with details about the design and the design thinking, at the moment it's probably the best documentation! 



Basic Bill Of Materials, This is just a guide for a basic build as you could build up the PCB in any way you can imagine!

- The PCB, Available on [Tindie](https://www.tindie.com/products/concreted0g/storper/)
- 4* N20 metal gear motors in a gear ratio of your choice rated up to 6V. <br />
- 4* 3D printed motor mount clips to attach the motors (files in the 3D models section or periodically available on the tindie listing as an options)<br />
- 8* 6mm M2 bolts and nuts to attach motor mounts.<br />
- A raspberry pi Pico or Pico W, or equivalent footprint microcontroller board.<br />
- Some N20 compatible wheels (either commercial or home brew/3D printed)<br />
- Some kind of power supply (simplest is a small USB pack, other options are a 14500 or 18650 cell wired into the power input)<br />
- Semi optional, an upper deck to attach power supply too. (Inkscape files for Lasercutting or CNC or heck, cutting out with a saw, are in the Deck Drawing folder, or available lasercut on the Tindie listing)<br />

But that's just a guide, you could use different items or design to the basic PCB/chassis in different ways. <br />

All the KiCad files in the repo were originally made in version 7.xx. 

**Update 28-05-2024**

Added an Addons folder which currently contains 2 new PCB designs. <br />

Bumper can receive an ultrasonic module (HC-SR04) and also have 2 bump switches connected. <br />
The Kludge Deck conforms to the StoRPer main PCB layout with lots of prototyping space and extra holes for mounting stuff! <br />

Bumpers can be added above or below the main PCB with lots of different mount options. Therefore you might need to buy a range of standoffs to accomodate and support your design. If however you have access to a 3D printer there is a FreeCAD file in the 3D models section called STANDOFFS which you can simply adjust the length of a standoff tube that will slot over an M3 bolt. You can make custom lengths to suit your build. 


![Alt text](images/bumper3d.png?raw=true "Title")

![Alt text](images/kludge_deck.jpg?raw=true "Title")


**Tiny Update 29-06-25**

Added a small hex adaptor part to the 3D models section. I ran a workshop recently and wanted to use more affordable mecanum wheels and found some cheap 48mm mecanum wheels available on places like aliexpress etc. However they have a hexagonal axle mount. After numerous iterations and dialling in the 3D printing I made a super simple slip on adaptor part that sits inside the wheel and slots on snugly to the N20 motor mount. Useful for stoRPer of course, but useful for any N20 motor project. 

![Alt text](images/IMG_20250331_123952.jpg?raw=true "Title")



