*** Settings ***
# SeleniumLibrary
Library     SeleniumLibrary

*** Variables ***
${from}    Coimbatore
${to}      Trivandrum



*** Test Cases ***
TC-002 Verify if a user is search busess for tommorow
    Open Make My Trip As
    Search Buses    ${from}      ${to}  
    Sleep     10s



*** Keywords ***
Open Make My Trip As
    Open Browser     browser=chrome
    Maximize Browser Window
    Go To            https://www.makemytrip.com
    Sleep    5s
    Click Element    //span[@data-cy="closeModal"]



Search Buses
    [Arguments]    ${fromCity}        ${toCity}   
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
    Wait Until Element Is Visible    //div[contains(text(), 'August')]/ancestor::div[@class="DayPicker-Month"]//div[@aria-selected="true"]     10s
    Click Element    //div[contains(text(), 'August')]/ancestor::div[@class="DayPicker-Month"]//div[@aria-selected="true"] 
    Click Element    search_button