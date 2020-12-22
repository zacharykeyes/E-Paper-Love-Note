#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

cwd = os.getcwd()
picdir = cwd + '/pic'
libdir = cwd + '/lib'

import logging
from lib.waveshare_epd import epd2in9b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in9b V2 Demo")
    
    epd = epd2in9b_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)
    
    # Initializing Drawing on the image
    logging.info("Drawing")    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...") 
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  #298*126
    HRYimage = Image.new('1', (epd.height, epd.width), 255)  #298*126  ryimage: red or yellow image  
    drawblack = ImageDraw.Draw(HBlackimage)
    draw = ImageDraw.Draw(HRYimage)
    time.sleep(1)

    drawblack.text((10, 0), 'hello world', font = font24, fill = 0)
    drawblack.text((10, 20), '2.9inch e-Paper bc', font = font24, fill = 0)
    drawblack.text((150, 0), u'Jme B', font = font24, fill = 0)    
    drawblack.line((20, 50, 70, 100), fill = 0)
    drawblack.line((70, 50, 20, 100), fill = 0)
    drawblack.rectangle((20, 50, 70, 100), outline = 0)    
    draw.line((165, 50, 165, 100), fill = 0)
    draw.line((140, 75, 190, 75), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw.rectangle((80, 50, 130, 100), fill = 0)
    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    time.sleep(10)
    
    # logging.info("Clear...")
    # epd.init()
    # epd.Clear()
    
    logging.info("Goto Sleep...")
    epd.sleep()
    epd.Dev_exit()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in9b_V2.epdconfig.module_exit()
    exit()
