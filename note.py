#! python3
import smtplib, time, os
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)



password = 'PASSWORD'
toAddress = "EXAMPLE@EXAMPLE.COM"
text = "Sorry there are no time slots available at the moment to book first and second dose appointments, please check back later."
textWanted = "If you have not had any COVID-19 vaccinations click below"
#url of the page we want to scrape
url = "https://uma.force.com/covidtesting/s/vaccination"

# initiating the webdriver. Parameter includes the path of the webdriver.
timeTosleep = 5
while True:
    driver.get(url) 
    
    # this is just to ensure that the page is loaded
    time.sleep(timeTosleep)

    html = driver.page_source
    if not text in html or textWanted in html:
        timeTosleep = 90
        conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
        conn.ehlo() # call this to start the connection
        conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
        conn.login('songchenbot@gmail.com', password)
        conn.sendmail('songchen@umass.edu', toAddress, 'Subject: VACCINE IN UMASS\n\nAttention!\n\nVaccine at https://uma.force.com/covidtesting/s/vaccination \nSong Chen')
        conn.quit()
    else:
        timeTosleep = 5


driver.close() 


