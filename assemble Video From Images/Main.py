from Tools import assembleVideo

print("Sestavljanje img-jev ")
print("različnih velikosti v Video posnetka")
print("Napiši interval izmenjava Posnetkov: (cca 0.5-6)")
print("1 pomeni 1x na sekundo, 5 pomeni 5x na sekundo")
intervarlString = input()
if intervarlString == '':
    assembleVideo('Images')
else:
    intervarl = float(intervarlString)
    assembleVideo('Images', intervarl)
