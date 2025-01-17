import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cv2
import numpy as np
import time
from PIL import ImageGrab
from pytesseract import pytesseract
import pyautogui as pa



pytesseract.tesseract_cmd= "D:\\Uygulamalar\\tes\\tesseract.exe"
pa.FAILSAFE = False
pa.click(0,0)
img = ImageGrab.grab(bbox=(950,200,1350,280))
img_np = np.array(img)
frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
word = pytesseract.image_to_string(frame)
word = word.upper()
print(word)
word =word.replace("HINT", "")
word =word.replace("SKIP", "")
word =word.replace("-E", "")
word =word.replace("- E", "")
word =word.replace("-", "")
word =word.replace("-S", "")
word =word.replace("-SEE", "")
word =word.replace("-SEEE", "")
word =word.replace("— (ES", "")
word =word.replace("♀", "")
word =word.replace("|", "")
word =word.replace("!", "I")
word =word.replace("\n", "")
word =word.strip()

print(word)
ser = word + " black-and-white 2d"
print(ser)





driver = webdriver.Chrome('D:\Yazilim\OpenCV\gartic\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get('https://www.google.com.tr/imghp?hl=tr&ogbl')
box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
box.send_keys(word + " vector 2D")
box.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div/div/div').click()
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[1]/div/div[1]').click()
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[4]/div').click()
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]').click()
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').screenshot('D:\Yazilim\OpenCV\gartic\hop.png')
driver.close()
driver.quit()

time.sleep(1)
try:
    img_found = cv2.imread("hop.png")
except:
    try:
        img_found = cv2.imread("hop.jpg")
    except:
        print("no img")
        pass
img_found = cv2.resize(img_found,(120,120))
#img_found = cv2.blur(img_found,(3,3),0)
ret,img_found = cv2.threshold(img_found,127,255,cv2.THRESH_BINARY_INV)
img_found = cv2.Canny(img_found,40,150)
gap = 6
lastPoint = (0,0)
for i in range(img_found.shape[0]-1):
    for k in range(img_found.shape[1]-1):
        if (img_found[i,k] == [255, 255,255]).all():
            if ((((lastPoint[0] - (950+k))**2) + ((lastPoint[1]-(320+i))**2) )**0.5)>gap:
                pa.click(x=950+k, y=320+i)
                lastPoint = (950+k, 320+i)


try:
    os.remove("hop.jpg")
except:
    os.remove("hop.png")

cv2.waitKey(0)
cv2.destroyAllWindows()