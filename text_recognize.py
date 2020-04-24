import cv2
import pytesseract

#file path of .exe of tesseract(use for OCR)
#   C:\Program Files\Tesseract-OCR\tesseract.exe

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Read image from which text needs to be extracted
img = cv2.imread("image3.png")

im2 = img.copy()


    # Apply OCR on the cropped image
text = pytesseract.image_to_string(im2)
print(text)

cv2.imshow("text detected",im2)
cv2.waitKey(0)