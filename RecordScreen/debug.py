from pynput.mouse import Listener
from PIL import ImageGrab
from scrnRecord import record


start_x, start_y, end_x, end_y = 0, 10, 1000, 1100
default_value: str
number_frame: any
time_frame: any


def snemanje():
    global start_x, start_y, end_x, end_y
    global number_frame, time_frame
    number_frame = int(number_frame)
    time_frame = float(time_frame)
    record(start_x, start_y, end_x, end_y,
           number_frame, time_frame)


print("Število posnetkov")
number_frame = input()
print("Število posnetkov na sekundo")
time_frame = input()
print("Program za PrintScreen. NE OZNAČI CMD ali PowerShell !!!. Začni.")
snemanje()
