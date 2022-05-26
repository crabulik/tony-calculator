import time
import numpy as np
from PIL import ImageGrab
import cv2
import os
import pytesseract
import json
from types import SimpleNamespace
from decimal import Decimal

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
if not os.path.exists("tmp"):
    os.mkdir("tmp")

def parseValue(image, do_color_invert, value_name, full_log):
    if full_log :
        print(f'Parsing {value_name}')
    np_array = np.array(image)
    gray = cv2.cvtColor(np_array, cv2.COLOR_BGR2GRAY)

    if do_color_invert :
        processed = (255-gray)
    else:
        processed = gray

    cv2.imwrite(f'tmp/{value_name}.png', processed)

    textValue = pytesseract.image_to_string(processed, lang='eng', config='--psm 6').strip()

    try:
        return Decimal(textValue)
    except:
        raise Exception(f'Cannot parse {value_name}. See the temp directory to verify the captured area.')


print("Calculating: X = A * 1000 ")
print("Calculating: Y = (A * 1000) - (X * B)")

with open("config/cfg.json", "r") as jsonfile:
    cfg = json.load(jsonfile, object_hook=lambda d: SimpleNamespace(**d))
    print("Config loaded.")
print(cfg)

while True :
    try:
        if cfg.fullLog :
            print("Capturing screenshots ...")
        imageA = ImageGrab.grab(bbox=(cfg.valueA.x1, cfg.valueA.y1, cfg.valueA.x2, cfg.valueA.y2), all_screens=True)
        imageB = ImageGrab.grab(bbox=(cfg.valueB.x1, cfg.valueB.y1, cfg.valueB.x2, cfg.valueB.y2), all_screens=True)

        if cfg.fullLog :
            print("Parsing values ...")
        valA = parseValue(imageA, cfg.valueA.doColorInvert, "ValueA", cfg.fullLog)
        valB = parseValue(imageB, cfg.valueB.doColorInvert, "ValueB", cfg.fullLog)

        x = valA * 1000
        y = valA * 1000 + valB * x
        print(f'X = {x}  Y = {y}')
    except Exception as err:
        print(f"{err=}")
        
    time.sleep(cfg.delaySeconds)