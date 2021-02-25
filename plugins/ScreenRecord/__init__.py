import glob
from plugins import Plugin
from plugins.Image import Image as I
import pyautogui
import cv2
from PIL import Image
import numpy as np
import time
import os
import math


class ScreenRecord(Plugin):

    recording = False
    image_folder = './video/'

    def __init__(self):
        super().__init__()

    def __del__(self):
        pass
        # self.stop_capture()

    def start_capture(self, time_limit=60, fps=5, compress=False):

        # Limita o FPS a 24
        if fps > 24:
            fps = 24

        self.recording = True
        frame_number = 0
        max_frames = fps*time_limit

        while self.recording:
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            image_name = f'{frame_number}.png'
            zf_image_name = image_name.zfill(10)
            image_path = f'{self.image_folder}{zf_image_name}'
            cv2.imwrite(image_path, image)
            frame_number += 1
            if frame_number >= max_frames:
                break

        if compress:
            self.compress()

        self.stop_capture(fps=fps)

    def compress(self):

        images = [img for img in os.listdir(
            self.image_folder) if img.endswith(".png")]

        prev_image = None
        i = I()
        for image in images:

            img_path = f'{self.image_folder}{image}'

            # First cicle
            if prev_image == None:
                prev_image = img_path
                continue

            print(f"Previous: {prev_image}")
            print(f"Current: {img_path}")

            difference = i.compare(prev_image, img_path)
            print(f"Difference: {difference}")

            if difference < 0.01:
                print(f'Removendo imagem "{prev_image}"')
                os.remove(prev_image)

            prev_image = img_path

    def stop_capture(self, fps=5):

        self.recording = False
        video_name = 'video.avi'

        images = [img for img in os.listdir(
            self.image_folder) if img.endswith(".png")]

        # resolution
        frame = cv2.imread(os.path.join(self.image_folder, images[0]))
        height, width, layers = frame.shape

        # codec
        # codec = cv2.VideoWriter_fourcc(*'XVID')
        codec = cv2.VideoWriter_fourcc(*'WMV2')
        video = cv2.VideoWriter(video_name, codec, fps, (width, height))

        for image in images:
            video.write(cv2.imread(os.path.join(self.image_folder, image)))

        # Remove screenshots antigos
        files = glob.glob(f'{self.image_folder}*.png', recursive=True)

        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))

        cv2.destroyAllWindows()
        video.release()
