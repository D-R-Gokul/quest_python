*** Settings ***
# SeleniumLibrary
Library     SeleniumLibrary

*** Variables ***
# ${from}    Coimbatore
# ${to}      Trivandrum
# ${urlCustomer}    https://www.makemytrip.com/
# ${urlOperator}    https://www.operator.makemytrip.com





#source
#destination
#date : different number of buses as per day in a week. 7 dates
#time : 21:15, 22:30, 22:00,    #other verification: operator/user

#number of named travel displayed in search


*** Test Cases ***
TC-001 Verify if a user is able to filter bus according to their seat preference
    Open Make My Trip As
    Search Buses    Coimbatore    Trivandrum
    Sleep     10s




#1. Enter the url www.makemytrip.com
#2. Click on the bus icon in the top nav bar
#
#
#
#
#3. Tap on “Search” button in the center
#4. Enter city from where you want to go in the ‘From’ text box or select from the dropdown menu
#5. Enter city the user want to go to in the ‘To’ text box or select from the dropdown menu
#6. Click the ‘Depart’ box and select a ‘date’ from the dropdown menu
#7. Tap ‘Search’
#8. Select the Seat type on the left side of the page
#
#Expected: Verify if the user is able to see buses according to their preferred seat type

#Sleeper button : //span[contains(text(),'Sleeper')]/ancestor::li//span[text()='Sleeper']
#
#Sleeper bus :
#//span[contains(text(),'Sleeper')]/ancestor::div/*[@class="busCardContainer "]//p[contains(text(),"Sleeper")]



*** Keywords ***
Open Make My Trip As
    Open Browser     browser=chrome
    Maximize Browser Window
    Go To            https://www.makemytrip.com
    Sleep    5s
    Click Element    //span[@data-cy="closeModal"]



Search Buses
    [Arguments]    ${fromCity}        ${toCity}    #${date}
    Click Element    //nav//li[@class="menu_Buses"]

    Wait Until Element Is Visible     fromCity     10s
    Click Element        fromCity
    Wait Until Element Is Visible     //input[@placeholder="From"]     10s
    Input Text       //input[@placeholder="From"]     ${fromCity}
    Wait Until Element Is Visible    //div[contains(@class, 'autosuggest')]//span[contains(text(),'${fromCity},')]
    Click Element    //div[contains(@class, 'autosuggest')]//span[contains(text(),'${fromCity},')]


    Wait Until Element Is Visible     toCity     10s
    Run Keyword And Ignore Error        Click Element        toCity
    Wait Until Element Is Visible     //input[@placeholder="To"]     10s
    Input Text       //input[@placeholder="To"]     ${toCity}
    Wait Until Element Is Visible       //div[contains(@class, 'autosuggest')]//span[contains(text(),'${toCity},') or contains(text(),'(${toCity}),')]
    Click Element    //div[contains(@class, 'autosuggest')]//span[contains(text(),'${toCity},') or contains(text(),'(${toCity}),')]

    Run Keyword And Ignore Error     Click Element    travelDate      #date picker/calender will open up
    Wait Until Element Is Visible    //div[contains(text(), 'August')]/ancestor::div[@class="DayPicker-Month"]//div[contains(@class,"today")]     10s
    Click Element    //div[contains(text(), 'August')]/ancestor::div[@class="DayPicker-Month"]//div[contains(@class,"today")]
    Click Element    search_button






