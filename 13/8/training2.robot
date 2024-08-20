*** Settings ***
# SeleniumLibrary
Library     SeleniumLibrary
Library    collections
Library    String
Library    OperatingSystem

Suite Setup    Open Make My Trip As
Suite Teardown    Close Browser

Test Setup    Search Buses    ${from}    ${to}
Test Teardown    Clear Filter
*** Variables ***
${from}    Coimbatore
${to}      Trivandrum

*** Test Cases ***
TC-001 Verify if a user is able to filter bus according to their drop point
    Select Filter     Drop point     Pattam
    Verify Filter    Pattam

TC-002 Verify if a user is able to filter bus according to their drop point

    Select Filter     Drop point     Ulloor
    Verify Filter    Ulloor


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

    Run Keyword And Ignore Error    Click Element    travelDate      #date picker/calender will open up
    Wait Until Element Is Visible     //div[contains(text(), 'August')]/ancestor::div[@class="DayPicker-Month"]//div[text()='19']     10s
    Click Element    //div[contains(text(), 'August')]/ancestor::div[@class="DayPicker-Month"]//div[text()='21']
    Click Element    search_button
    Wait Until Element Is Visible     //div[@class="busListingContainer"]//p[contains(text(),'found')]




Select Filter
    [Arguments]     ${filterType}     ${filterExactText}
    # take the initial count
    Click Element     toggle_buses
    ${initialCount}    Get Element Count     //div[@class="busCardContainer "]     # maximum bus in search result, no filter applied
    Click Element    //div[contains(text(),'${filterType}')]/../..//span[text()='${filterExactText}']
    Wait Until Element Is Not Visible     //div[@class="busListingContainer"]//p[contains(text(),'found') and contains(text(),'${initialCount}')]
    #wait till its not the previous count or wait till elemnt disappears.
    sleep   6s


# Get All Bus Id


#     @{allBusId}    Create List
#     run keyword and ignore error     Click Element     //div[@id="toggle_buses" and not(contains(@class,'active'))]
#     ${numberOfBuses}     Get Element Count    //div[starts-with(@id,"bus_")]
#     ${numberOfBuses}    Evaluate     $numberOfBuses+1
#     FOR    ${index}    IN RANGE     1    ${numberOfBuses}
#     ${busId}     Get Element Attribute       (//div[starts-with(@id,"bus_")])[${index}]        id  # node with id in it, exact 16 matches.
#     Append To List     ${allBusId}    ${busId}


#     END
#     Log    ${allBusId}



Verify Filter
    [Arguments]    ${filtertext}
    run keyword and ignore error     Click Element     //div[@id="toggle_buses" and not(contains(@class,'active'))]
    Wait Until Element Is Visible    //div[@class="busCardContainer "]
    ${numberOfBuscard}     Get Element Count    //div[@class="busCardContainer "]
    ${numberOfBuses}    Evaluate     $numberOfBuscard+1
    FOR    ${index}    IN RANGE     1    ${numberOfBuses}
        Scroll Element Into View     (//div[contains(@class,"busCardFooter")]//span[text()="Pickups & Drops"])[${index}]
        Click Element    (//div[contains(@class,"busCardFooter")]//span[text()="Pickups & Drops"])[${index}]
        sleep    2s
        Element Should Be Visible    //ul[@class="btnSelectBusWithoutRadio"]//span[@title="${filtertext}"]    
        Click Element    (//div[contains(@class,"busCardFooter")]//span[text()="Pickups & Drops"])[${index}]
        # ${count}    Evaluate    ${count}+1
    END
    # Should Be Equal As Numbers    ${numberOfBuscard}    ${finalcount}
    # Should Be Equal    ${numberOfBuscard}    ${count}
    Sleep    3s

Clear Filter
    run keyword and ignore error    Click Element    //div[@class="filterContainer"]//p[ text()="CLEAR ALL" and notcontains(@class,"disabledGrey")]
    