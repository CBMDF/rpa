from plugins import Plugin
import pyautogui
import cv2
from PIL import Image
import numpy as np
import time
import os


class ScreenRecord(Plugin):

    recording = False

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.stop_capture()

    async def start_capture(self, screen_size=[640, 480], time_limit=60):

        self.recording = True
        frame = 0

        while self.recording:
            time.sleep(1)
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            cv2.imwrite(f'./video/{frame}-frame.png', image)
            frame += 1
            if frame >= time_limit:
                break

        self.stop_capture()

    def stop_capture(self):
        self.recording = False

        image_folder = './video'
        video_name = 'video.avi'

        images = [img for img in os.listdir(
            image_folder) if img.endswith(".png")]
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, 0, 1, (width, height))

        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()
