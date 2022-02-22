from gpiozero import Button 
import os, time


btn1 = Button(5)                              # assign each button to a variable
btn2 = Button(6)                              # by passing in the pin number
btn3 = Button(13)                             # associated with the button
btn4 = Button(19)          


def linuxCmd(cmd):
    import subprocess
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')



def handleBtnPress(btn):
    
    # get the button pin number
    pinNum = btn.pin.number 
    if pinNum == 5:
        os.system('mpc next > /dev/null')
    if pinNum == 6:
        mpcText = linuxCmd('mpc')
        if mpcText.splitlines()[0][0:12] == 'NPO Radio2: ':
            os.system('amixer set Headphone toggle > /dev/null')
        else:
            os.system('mpc toggle > /dev/null')
    if pinNum == 13:
        os.system('amixer set Headphone 500+ > /dev/null')
    if pinNum ==19:
        os.system('amixer set Headphone 500- > /dev/null')
    



    
btn1.when_pressed = handleBtnPress
btn2.when_pressed = handleBtnPress
btn3.when_pressed = handleBtnPress
btn4.when_pressed = handleBtnPress


def yourFunction():
    pass

while True:
    yourFunction()
    time.sleep(5)
