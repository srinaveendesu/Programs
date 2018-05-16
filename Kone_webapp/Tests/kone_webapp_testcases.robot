*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported Selenium2Library.

Resource         resources.robot

*** Variables ***
${INVALID_URL1}      https://koneiot-portal-uat.eu-gb.mybluemix
${INVALID_URL2}      https://koneiot-portal-uat.eu-gb.mybluemix
${INVALID_URL3}      https://random.link.which.does.not.exit
${INVALID_URL4}      https://random.link.which.does.not.exit
${INVALID_URL5}      this-is-just-a-random-text
${DELAY}             5
${BUTTON1}           Cloud_Directory_UAT
${BUTTON2}           kone-uat
${INVALID_BUTTON}    RANDOMBUTTON
${USERNAME}          testuser@kone.com
${PASSWORD}          testuser12#
${INVALID_USERNAME}    Random_user
${INVALID_PASSWORD}    Random_password


*** Test Cases ***
Testcase for Invalid URL Accessing portal
    Log    Different types of invalid URL's are given
	${result} =    OpenWeblink    ${INVALID_URL1}
	Should Be Equal    ${result}    Invalid URL
	${result} =    OpenWeblink    ${INVALID_URL2}
	Should Be Equal    ${result}    Invalid URL
	${result} =    OpenWeblink    ${INVALID_URL3}
	Should Be Equal    ${result}    Invalid URL
	${result} =    OpenWeblink    ${INVALID_URL4}
	Should Be Equal    ${result}    Invalid URL
	${result} =    OpenWeblink    ${INVALID_URL5}
	Should Be Equal    ${result}    Invalid URL
	
Testcase for valid URL to access the portal
    Log    Open browser and enter the KONE web link
    ${browser}    ${title}    ${page_source} =    OpenWeblink    ${URL}
	sleep    ${DELAY}
	Log    Verify the obtained page by verifying the title and two buttons
	${result} =    validate_page_signin    ${title}    ${page_source}    1
	Should Be Equal    ${result}    1
	Teardown    ${browser}

Testcase for Navigating across the portal
	Log    Navigation test to kone user page
	${result}     ${browser} =    Navigatelinkbutton    ${BUTTON2}    ${URL}
	Should Be Equal    ${result}    Navigated to invalid page
	Teardown    ${browser}	
	Log    Invalid button given
	${result}     ${browser} =    Navigatelinkbutton    ${INVALID_BUTTON}    ${URL}
	Should Be Equal    ${result}    Invalid button given
	Teardown    ${browser}

Testcase for Logging-In to the portal
    Log    Navigation test to kone user page
    ${result}     ${browser} =    Navigatelinkbutton    ${BUTTON1}    ${URL}
    Should Be Equal    ${result}    Valid page
    Log    logging-In using invalid-user
    ${result}     ${browser} =    CorrectSignin    ${browser}    ${INVALID_USERNAME}    ${PASSWORD}
    Should Be Equal    ${result}    Invalid Username
    Log    logging-In using invalid-password
    ${result}     ${browser} =    CorrectSignin    ${browser}    ${USERNAME}    ${INVALID_PASSWORD}
    Should Be Equal    ${result}    Invalid Password
    Log    logging-In using invalid-user,password
    ${result}     ${browser} =    CorrectSignin    ${browser}    ${INVALID_USERNAME}    ${INVALID_PASSWORD}
    Should Be Equal    ${result}    Invalid Username
    Log    logging-In using valid-user,password
    ${result}     ${browser} =    CorrectSignin    ${browser}    ${USERNAME}    ${PASSWORD}
    Should Be Equal    ${result}    Logged in to system
    Teardown    ${browser}

Testcase for testing Incorrect logging handling in the website
    Log    Navigation test to kone user page
    ${result}     ${browser} =    Navigatelinkbutton    ${BUTTON1}    ${URL}
    Should Be Equal    ${result}    Valid page
    Log    logging-In using invalid-user
    ${result} =    InCorrectSignin    ${browser}    ${INVALID_USERNAME}    ${PASSWORD}
    Should Be Equal    ${result}    1
    Log    logging-In using invalid-password
    ${result} =    InCorrectSignin    ${browser}    ${USERNAME}    ${INVALID_PASSWORD}
    Should Be Equal    ${result}    1
    Log    logging-In using invalid-user,password
    ${result} =    InCorrectSignin    ${browser}    ${INVALID_USERNAME}    ${INVALID_PASSWORD}
    Should Be Equal    ${result}    1
    Teardown    ${browser}

Testcase for validating forgot Username page
    Log    Navigation test to kone user page
    ${result}     ${browser} =    Navigatelinkbutton    ${BUTTON1}    ${URL}
    Should Be Equal    ${result}    Valid page
	Log    Select the forgot username link
    ${result} =    username_forgot_validate    ${browser}
	Should Be Equal    ${result}    Forgot Username Page
	Teardown    ${browser}

Testcase for validating forgot Password page
    Log    Navigation test to kone user page
    ${result}     ${browser} =    Navigatelinkbutton    ${BUTTON1}    ${URL}
    Should Be Equal    ${result}    Valid page
	Log    Select the forgot password link
	${result} =    userpassw_forgot_validate    ${browser}
	Should Be Equal    ${result}    Forgot Password Page
	Teardown    ${browser}

	
Testcase for finding the Equipment-id from the portal
    Log    Navigation test to kone user page
	${result}     ${browser} =    Navigatelinkbutton    ${BUTTON1}    ${URL}
	Should Be Equal    ${result}    Valid page
	Log    logging-In using valid-user,password
	${result}     ${browser} =    CorrectSignin    ${browser}    ${USERNAME}    ${PASSWORD}
    Should Be Equal    ${result}    Logged in to system
    ${result} =    SearchEquipment    ${browser}
    Should Be Equal    ${result}    Equipment found
	Teardown    ${browser}

