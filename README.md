OWI/Maplin Robotic Arm
==========
Very Simple Tk GUI Added instead of website for computers without apache installed
==========

Buy an OWI or Maplin robotic arm (looks like the one https://github.com/lizquilty/roboticarm/blob/master/usb-robot-arm.png ). Its cheap, around $50USD or so

Purchase the USB kit to connect it to a PC


Get Linux based PC to hook up to it (this is debian/ubuntu specific probably)

Set up pyusb
Install the custom pyUSB
pyusb http://sourceforge.net/projects/pyusb
```
 wget "http://downloads.sourceforge.net/project/pyusb/PyUSB%201.0/1.0.0-alpha-3/pyusb-1.0.0a3.zip?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpyusb%2F&ts=1377736820&use_mirror=hivelocity"
 unzip pyusb-1.0.0a3.zip
 cd pyusb
 python setup.py build
 python setup.py install
```


