from Tools import assembleVideo

print("Sestavljanje img-jev ")
print("različnih velikosti v Video posnetka")
print("Napiši interval izmenjava Posnetkov: (cca 0.5-6)")
intervarlString = input()
if intervarlString == '':
    assembleVideo('Images')
else:
    intervarl = float(intervarlString)
    assembleVideo('Images', intervarl)
