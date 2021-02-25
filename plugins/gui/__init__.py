from plugins import Plugin
import numpy as np
import pyautogui
import imutils
import cv2
import time
import pytesseract
from PIL import Image


class gui(Plugin):

    def __init__(self):
        super().__init__()

    def find_element(self, reference_image):
        location = pyautogui.locateOnScreen(reference_image)
        return location

    def fill(self, reference_images, text, enter=False):
        if self.click(reference_images):
            pyautogui.write(text)
            if enter:
                pyautogui.press('enter')
            return True
        else:
            return False

    def press_enter(self, reference_images):
        if self.click(reference_images):
            pyautogui.press('enter')
            return True
        else:
            return False

    def click(self, reference_images, right_click=False, Debug=False):

        location = None
        for image in reference_images:
            location = self.find_element(image)
            if location != None:
                print(f'Reference {image} found on screen.')
                break
            else:
                if Debug:
                    print(f'Reference {image} NOT found on screen.')

        if location != None:
            buttonx, buttony = pyautogui.center(location)
            if right_click:
                pyautogui.rightClick(buttonx, buttony)
            else:
                pyautogui.click(buttonx, buttony)
            return True
        return False

    def screenshot(self, interval=2, image_path="./screenshot.png"):
        time.sleep(interval)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imwrite(image_path, image)
