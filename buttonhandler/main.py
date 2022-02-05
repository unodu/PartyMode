# PARTY HANDLER
# PURPOSE: Interprets Arduino serial data and activates subs equent script.
from datetime import datetime
import serial
import os
now = datetime.now()
current_time = now.strftime("%b-%d-%Y %H:%M:%S")
currentState = "0"
lastState = "0"
button_port = '/dev/cu.usbserial-2230' # MUST CHANGE IF ARDUINO PORT CHANGES

i = 0
while i <= 10:
    lastState = currentState
    arduino = serial.Serial(button_port)
    cc = str(arduino.readline())
    currentState = (cc[2:][:-5])
    print(current_time + " ARDUINO - " + currentState)
    if lastState == "Inactive" and currentState == "Active":
        #Shell
        print(current_time + " HANDLER - " + "Activating...")
        log_output = os.system("automator /Applications/PartyMode/PartyModeActivator.workflow")
        sysout = str(log_output)
        print(current_time + " HANDLER: " + sysout)
    elif lastState == "Active" and currentState == "Inactive":
      pass


    #MICAH BECK
    #FEB 4 2022