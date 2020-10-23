import csv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="c:\WebDriver\chromedriver.exe")

driver.get("https://calendar.google.com/calendar/u/0/r")
driver.implicitly_wait(15)

# CONSTANTS
# PLEASE FILL IN YOUR OWN LOGIN AND PASSWORD
loginID = ''
password = ''
sStart = '08:00'
sEnd = '17:00'
cStart = '08:00'
cEnd = '20:30'
lStart = '14:00'
lEnd = '22:00'
nStart = '20:00'
nEnd = '08:30'
eventDescription = '#work'
eventDescriptionBoxId = "T2Ybvb"
startingEventDescriptionBoxId = 2

# Find and send login ID
id_box = driver.find_element_by_id('identifierId')
id_box.send_keys(loginID)

# Find and click next page from ID login
login_button = driver.find_element_by_id('identifierNext')
login_button.click()

# Find password box
passWordBox = driver.find_element_by_xpath(
    '//*[@id ="password"]/div[1]/div / div[1]/input')
passWordBox.send_keys(password)
# Log in
nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
nextButton[0].click()


def addShift(inputShiftType, inputDate, inputStartTime, inputEndTime):
    # Click create
    createButton = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/button')
    createButton.click()

    # More options
    moreOptions = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[1]/span/span')
    hover = ActionChains(driver).move_to_element(moreOptions)
    hover.perform()
    moreOptions.click()

    # Adding a title
    eventTitle = driver.find_element_by_xpath('//*[@id="xTiIn"]')
    eventTitle.send_keys(inputShiftType)

    # Adding a date and time
    dateField = driver.find_element_by_id('xStDaIn')
    dateField.send_keys(Keys.CONTROL, 'a')
    dateField.send_keys(Keys.BACKSPACE)
    dateField.send_keys(inputDate)
    dateField.send_keys(Keys.ENTER)

    startTime = driver.find_element_by_xpath('//*[@id="xStTiIn"]')
    startTime.send_keys(Keys.CONTROL, 'a')
    startTime.send_keys(Keys.BACKSPACE)
    startTime.send_keys(inputStartTime)
    startTime.send_keys(Keys.ENTER)

    endTime = driver.find_element_by_xpath('//*[@id="xEnTiIn"]')
    endTime.send_keys(Keys.CONTROL, 'a')
    endTime.send_keys(Keys.BACKSPACE)
    endTime.send_keys(inputEndTime)
    endTime.send_keys(Keys.ENTER)

    # every time a new event is created, the id for the description box in the next
    # create event window is incremented by 3. hence making a dynamic id tag for the
    # event decription box. incrementing is done in the addShift loop
    eventBoxId = 'T2Ybvb' + str(startingEventDescriptionBoxId)
    inputEventDescription = driver.find_element_by_id(eventBoxId)
    inputEventDescription.send_keys(eventDescription)

    # Click on Calendar to change it to the COVID Rota
    rotaName = driver.find_element_by_xpath('//*[@id="xCalSel"]')
    hover = ActionChains(driver).move_to_element(rotaName)
    hover.perform()
    rotaName.click()

    # This is the likeliest element to break depending on an individual's google calendar setup
    # Select the COVID rota from the drop down list of Calendar options
    selectCovidRota = driver.find_element_by_xpath('//*[@id="xCalSel"]/div[2]/div[2]/span/div/div')
    hover = ActionChains(driver).move_to_element(selectCovidRota)
    hover.perform()
    selectCovidRota.click()

    # Click Save button
    saveButton = driver.find_element_by_xpath('//*[@id="xSaveBu"]')
    hover = ActionChains(driver).move_to_element(saveButton)
    hover.perform()
    saveButton.click()


# A loop to go through the rows on the rotadata CSV
with open('rotadata.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:

        # Create a Date object
        date = row[0]

        # Quirk of a mistake in the covid rota, doesnt change to 2021 when the new year starts
        # if month is jan or feb, changes year from 2020 to 2021
        if (date[5] == '0' and date[6] == '1') or (date[5] == '0' and date[6] == '2'):
            # In python strings are immuntable. converting string to a list of individual characters
            listString = list(date)
            # Changing the year to 2021
            listString[3] = '1'
            # Rejoining the list as a string to be used for the addShift function
            date = "".join(listString)

        print(date)

        # Create a shiftType object
        shiftType = row[1]
        print(shiftType)

        # Initialise some start and end times
        startTime = ''
        endTime = ''

        if shiftType == 'S':
            shiftType += ' Shift'
            startTime = sStart
            print(startTime)
            endTime = sEnd
            print(endTime)
            addShift(shiftType, date, startTime, endTime)
            startingEventDescriptionBoxId += 3
        elif shiftType == 'C':
            shiftType += ' Shift'
            startTime = cStart
            print(startTime)
            endTime = cEnd
            print(endTime)
            addShift(shiftType, date, startTime, endTime)
            startingEventDescriptionBoxId += 3
        elif shiftType == 'L':
            shiftType += ' Shift'
            startTime = lStart
            print(startTime)
            endTime = lEnd
            print(endTime)
            addShift(shiftType, date, startTime, endTime)
            startingEventDescriptionBoxId += 3
        elif shiftType == 'N':
            shiftType += ' Shift'
            startTime = nStart
            print(startTime)
            endTime = nEnd
            print(endTime)
            addShift(shiftType, date, startTime, endTime)
            startingEventDescriptionBoxId += 3
