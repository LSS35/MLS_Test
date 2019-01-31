from selenium import webdriver
import datetime
import io

driver = webdriver.Chrome()
driver.get("https://yandex.ru/time/")

ya = driver.title
yas = ya[0:5]

now = datetime.datetime.now()
loc = now.strftime("%H:%M")


str = u"≠"
file =  io.open("log.txt", "w+", encoding="utf-8") 

if loc == yas:
    file.write(now.strftime("%H:%M:%S")+" - УСПЕХ: "+loc+" = "+yas)
else:
    file.write(now.strftime("%H:%M:%S")+" - ОШИБКА: "+loc+" "+str+" "+yas)

file.close()        
driver.close()
