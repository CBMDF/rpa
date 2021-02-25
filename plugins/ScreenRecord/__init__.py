from plugins import Plugin
from plugins.Image import Image as I
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
        pass
        # self.stop_capture()

    def start_capture(self, screen_size=[640, 480], time_limit=60):

        self.recording = True
        frame = 0

        while self.recording:
            time.sleep(0.2)
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            image_name = f'{frame}.png'
            zf_image_name = image_name.zfill(10)
            image_path = f'./video/{zf_image_name}'
            cv2.imwrite(image_path, image)
            frame += 1
            if frame >= (time_limit/0.2):
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

        codec = cv2.VideoWriter_fourcc(*'mp4v')
        # video = cv2.VideoWriter(video_name, 0, 1, (width, height))
        # video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc('X', '2', '6', '4'), 1, (width, height))
        video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(
            'W', 'M', 'V', '2'), 1, (width, height))

        prev_image = None
        i = I()
        for image in images:

            img_path = f'./video/{image}'
            # First cicle
            if prev_image == None:
                prev_image = img_path

            print(f"Previous: {prev_image}")
            print(f"Current: {img_path}")

            difference = i.compare(prev_image, img_path)
            print(f"Difference: {difference}")

            if difference > 0.01:
                video.write(cv2.imread(os.path.join(image_folder, image)))
            prev_image = img_path

        cv2.destroyAllWindows()
        video.release()
