from pynput.mouse import Listener
from PIL import ImageGrab

start_x, start_y, end_x, end_y = 0, 0, 0, 0


def on_click(x, y, button, pressed):
    global start_x, start_y, end_x, end_y
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
            # Take a screenshot
            # ImageGrab.grab(bbox=(left, top, right, bottom))
            screenshot = ImageGrab.grab(bbox=(start_x, start_y, end_x, end_y))

            # Save the screenshot as an image file
            screenshot.save('scrShot.jpg')
            return False  # Stop listener


print("Program za PrintScreen. Začni.")

# Start mouse listener
with Listener(on_click=on_click) as listener:
    listener.join()  # Blocking call
