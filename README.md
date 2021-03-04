# RLH-ACCU-rota-google-sync
A py script to add google calendar events from a suitably formatted rota CSV file

Assumptions:
1. You have installed Python
2. You have installed the Python Selenium package
3. You have downloaded and placed the appropriate version Chrome Webdriver in a suitable place
4. You have formatted the rota to be like the example CSV file included
5. You initially only had one Google Calendar as only your personal calendar and none others
6. You have then created a separate rota calendar with appears as the 2nd drop down option when creating a new event
7. In the event your number of calendars has changed or differs from this, you will need to adapt the python script xPath links to change to the correct rota to add to
8. You have read syncRota.py, applied your own changes, including entering your loginID and password

Working with the above assumptions as of 23/10/2020

Note: this is a vastly overengineered solution to the problem and liable to break with any format changes to the google calendar website. Made to learn how to web scrape with Selenium. If you actually want to import to your calendar, use the CSV rota creation project
