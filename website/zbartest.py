import cv2
import numpy
from pyzbar.pyzbar import decode

print("Starting Camera...........")
cap = cv2.VideoCapture(0)

ret,img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
barcode =decode(gray)
print(barcode)
