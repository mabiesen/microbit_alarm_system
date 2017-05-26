# microbit_alarm_system

Created a basic alarm system using the microbit.  Alarm system is intended for use while I am at home, particularly when I am sleeping.

### Software Required:

1.  Micropython text editor for the Micro bit.  For this activity I used Mu.

THIS CODE REQUIRES ALTERATION OF THE MY ID VARIABLE TO WORK AS INTENDED.

Note: the editor isn't really required, you can connect in other ways, but this is easy

Note: I had issues installing Mu on Ubuntu, but great success on the Raspberry Pi and Windows 10.

### Materials Required: 

1. One BBC microbit for each door/window in your house that you would like to track and perhaps one for the bedroom.
2. 2 triple A batter pack for each microbit (or power via usb).  battery pack comes with the kit!  
3. 1 or more buzzers (roughly $2.50)
4. Tools/matl to mount the microbit and battery pack to a door.

### What it looks like in action:

Each micro bit is mounted to a door.  Micro bit constantly scans for changes in z matrix value using the built in accelerometer.  If a motion is detected, the microbit will alert you via its led screen; all other microbits using the code will be alerted using the radio feature.  Each alerted micro bit will display the id of the door that was moved (stored in the "my_id" variable in code).

Obviously leds will not wake you in the night, so we use a buzzer on at least one microbit; if it has been moved or received radio indication that another microbit has been moved, the buzzer will sound.  I used the sunfounder active buzzer for this project and it worked like a charm.  I used pin zero for the signal.  This buzzer is pretty loud, I only needed one.

There may come a time where you want to disable the alarm (during the day, having people over, etc) because the buzzer is really annoying.  To address this issue, press the "a" button on the microbit which holds your buzzer: the alarm for that micro bit will no longer be active until the "a" button is pressed again.

If you find that the alarm is ringing and you don't want to wait to shut the sound off, press the "b" button.

### Important Code Comments:

You will want to assign an appropriate "my_id" variable in the python code of the microbits to reflect alarm location; otherwise you will not be getting the most value from this project.  For the microbit using a buzzer, make sure to set the "has_buzzer" variable to True.`

### Going Further

You could connect one of the microbits to a pc and use it as a hub to transfer data to the pc (see my microbit laser pointer repo, microbit hub code.).  You could then use python code to transmit a text message or email to your mobile device for on-the-go alerts.
