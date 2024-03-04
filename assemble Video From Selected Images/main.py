from pynput.mouse import Listener
from PIL import ImageGrab
from scrnRecord import record

start_x, start_y, end_x, end_y = 0, 0, 0, 0
default_value: str
number_frame: any
time_frame: any


def on_click(x, y, button, pressed):
    global start_x, start_y, end_x, end_y
    global number_frame, time_frame
    if button == button.left:
        if pressed:
            start_x, start_y = x, y
            print('Označi')
        else:
            end_x, end_y = x, y
            print('Left mouse button pressed at ({0}, {1})'.format(
                start_x, start_y))
            print('Left mouse button released at ({0}, {1})'.format(
                end_x, end_y))
            if default_value.upper() == 'Y':
                record(start_x, start_y, end_x, end_y)
            else:
                number_frame = int(number_frame)
                time_frame = float(time_frame)
                record(start_x, start_y, end_x, end_y,
                       number_frame, time_frame)

            return False  # Stop listener


print("Ali se uporabijo prednatstavljene vrednosti. (Y) or (N)")
default_value = input()
if not default_value.upper() == 'Y':
    print("Število posnetkov (Default: 900)")
    number_frame = input()
    print("Število posnetkov na sekundo (cca 0.5 -7 ; Default:25)")
    time_frame = input()
print("Program za PrintScreen. NE OZNAČI CMD ali PowerShell !!!. Začni.")

# Start mouse listener
with Listener(on_click=on_click) as listener:
    listener.join()  # Blocking call
