from pynput.mouse import Listener
from PIL import ImageGrab


def record(start_x, start_y, end_x, end_y):
    frame_numbers: int = 5
    frame: int = 1
    while 1:
        # Take a screenshot
        # ImageGrab.grab(bbox=(left, top, right, bottom))
        print('CREATED IMAGE ({0}, {1},{2}, {3})'.format(
            start_x, start_y, end_x, end_y))
        screenshot = ImageGrab.grab(bbox=(start_x, start_y, end_x, end_y))

        # Save the screenshot as an image file

        frame_string = str(frame)
        file_name = "Output/"+"scrShot"+frame_string+'.jpg'
        screenshot.save(file_name)
        frame = frame+1
        if frame > frame_numbers:
            break


def assembleVideo():
    pass
