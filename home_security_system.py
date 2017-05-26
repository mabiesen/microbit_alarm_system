from microbit import *
import radio

#Global variables
# CHANGE THE MY ID VARIABLE TO REPRESENT THE DOOR OR WINDOW
# CHANGE THE HAS BUZZER VARIABLE IF THIS SPECIFIC MICROBIT WILL BE CONNECTED TO A BUZZER
# optionally edit my_alarm_length to change how long the alarm is sounded

alarm_is_active = True
my_id = "Bck"
has_buzzer = False
my_alarm_length = 5

#Lets immediately turn on the radio
radio.on()

# Detect motion? lets use the z accelerometer value
# The z axis refers to up down direction if you are holding the microbit horizontally relative to the gorund.
# If you turn the microbit on its side, z axis would therefore be left and right
# Therefore, for this code to work, you will have to mount the microbit upright on the door

# Determine whether motion occurred by comparing initial to current z value
def detect_motion(initialzvalue,currentzvalue):
    mybuffer = 200
    difference = currentzvalue - initialzvalue
    display.scroll(str(difference))
    if difference > mybuffer or difference < -1*(mybuffer):
        myreturn = True
    else:
        myreturn = False
    return myreturn

# Display the affected door
def led_alarm(targetdoor):
    display.scroll(targetdoor)

#Show alarm:  flashing screen, buzzer.  only hub has buzzer
def buzzer_alarm():
    pin0.write_digital(1)
    sleep(500)
    pin0.write_digital(0)
    sleep(100)
    
#Toggle alarm ability on or off
def toggle_alarm_ability():
    global alarm_is_active
    if alarm_is_active:
        alarm_is_active = False
    else:
        alarm_is_active = True
        
#############################################################
# Functions below this line are high level and use the functions above

def other_alarm_sequence(targetdoor):
    buzzer_alarm()
    led_alarm(targetdoor)
    

def my_alarm_sequence():
    x=0
    while x < my_alarm_length:
        radio.send(my_id)
        if has_buzzer:
            buzzer_alarm()
        if button_b.was_pressed():
            break
        led_alarm(my_id)
        x = x + 1
        sleep(1000)

    
# MAIN
def main():
    initialzvalue = accelerometer.get_z()
    while True:
        currentzvalue = accelerometer.get_z()
        motion_detected = detect_motion(initialzvalue,currentzvalue)
        if alarm_is_active:
            if motion_detected == True:
                my_alarm_sequence()
                initialzvalue = accelerometer.get_z()
            rcvd = radio.receive()
            if rcvd:
                display.scroll("here")
                other_alarm_sequence(rcvd)
        if button_a.was_pressed():
            toggle_alarm_ability()
        sleep(300)
            
# Start our program!
main()


