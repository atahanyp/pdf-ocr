import cv2
from spire.pdf.common import *
from spire.pdf import *
from PIL import Image 
import pytesseract
import os



# Create a PdfDocument object
doc = PdfDocument()

# Load a PDF document
doc.LoadFromFile(r'c:\Users\ataha\OneDrive\Masaüstü\Code\pyhton\yeter.py\esinavfoto.pdf')
  
images = []

# Loop through the pages in the document
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)

    # Extract images from a specific page
    for image in page.ExtractImages():
        images.append(image)

# Save images to specified location with specified format extension
index = 0
for image in images:
    os.chdir(r'c:\Users\ataha\OneDrive\esinavfotolar2')
    imageFileName = r'c:\Users\ataha\OneDrive\esinavfotolar2\-{0:d}.png'.format(index)
    index += 1
    image.Save(imageFileName, ImageFormat.get_Png())
doc.Close()
path = os.path.dirname(__file__)
newPath = r'c:\Users\ataha\OneDrive\esinavfotolar2'
klasor=newPath
fotos=os.listdir(klasor)
sozluk={}
indeks=0
for foto in fotos:
    print(os.path.join(klasor,foto).replace(os.sep, '/'))
    yol=os.path.join(klasor,foto).replace(os.sep, '/')
    img=cv2.imread(yol)
    
    gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    print(gri.shape)
    filter =cv2.blur(gri,(2,2))
    ret,tresh= cv2.threshold(filter,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret,tresh1= cv2.threshold(gri,150,250,cv2.THRESH_BINARY)


    date1=tresh[105:133,393:600]
    date2=tresh[617:647,393:600]
    date3=tresh[1129:1160,393:600]

    tc1=tresh[130:153,400:520]
    tc2=tresh[642:665,400:520]
    tc3=tresh[1158:1175,400:520]

    custom_config = r'--oem 3 --psm 6'
    
    sozluk[str(pytesseract.image_to_string(tc1, config=custom_config)).replace("\n","")] = str(pytesseract.image_to_string(date1, config=custom_config)).replace("\n","")
    sozluk[str(pytesseract.image_to_string(tc2, config=custom_config)).replace("\n","")] = str(pytesseract.image_to_string(date2, config=custom_config)).replace("\n","")
    sozluk[str(pytesseract.image_to_string(tc3, config=custom_config)).replace("\n","")] = str(pytesseract.image_to_string(date3, config=custom_config)).replace("\n","")
    

cv2.waitKey(0)

print(sozluk)
cv2.destroyAllWindows()
