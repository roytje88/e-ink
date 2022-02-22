from time import sleep
import time , os, textwrap
import epd2in7
from PIL import Image,ImageDraw,ImageFont
from gpiozero import Button
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

epd = epd2in7.EPD()
epd.init()

def PrintToDisplay(string):
    HBlackImage = Image.new('1', (epd2in7.EPD_HEIGHT,epd2in7.EPD_WIDTH), 255)
    draw = ImageDraw.Draw(HBlackImage)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 17)
    #font = ImageFont.truetype('/usr/share/fonts/opentype/3270/3270Medium.otf', 17)
    draw.text((5, 5), string, font = font, fill = 0)
    epd.display(epd.getbuffer(HBlackImage))

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "./text.txt": # in this example, we only care about this one file
            #PrintToDisplay(open('./text.txt','r').read())
            print('text.txt is veranderd')
        if event.src_path == './mpdStatus.txt':
            print('mpdStatus.txt is veranderd')

observer = Observer()
observer.schedule(Handler(), ".") # watch the local directory
observer.start()

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()