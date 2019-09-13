
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.OperatingSystem import OperatingSystem
import re
import time
import unittest
from unittest import TestCase as TC


kone_link = r'https://koneiot-portal-uat.eu-gb.mybluemix.net'
Kone_title = [r"Sign In",r'Username and Password Login']
kone_button_1 = [r"Cloud_Directory_UAT",r'name="username"']
kone_button_2 = [r"kone-uat",r'name="password"']
kone_username = r"testuser@kone.com"
kone_password = r"testuser12#"
kone_navigate = {"Cloud_Directory_UAT": 'source_id=264',\
                 "kone-uat":'source_id=266'}
kone_searchid = "search-text"
kone_searchkey = 'anylift'
kone_equipid = '10003251'

def validate_url(link):
    '''
    Description    :   Validate the URL being sent to the user
    Input Params   :   <link>     URL LINK
    Output Params  :   1      if URL is valid
                       0      if URL is not valid
    '''
    m = re.search(kone_link,link)
    if m:
        return 1
    else:
        return 0

def validate_username(username):
    '''
    Description    :   Validate the username being sent to the user
    Input Params   :   <username>     username
    Output Params  :   1      if username is valid
                       0      if username is not valid
    '''
    m = re.search(kone_username,username)
    if m:
        return 1
    else:
        return 0

def validate_password(password):
    '''
    Description    :   Validate the password being sent to the user
    Input Params   :   <password>     password
    Output Params  :   1      if password is valid
                       0      if password is not valid
    '''
    m = re.search(kone_password,password)
    if m:
        return 1
    else:
        return 0

def validate_page_signin(page_title,page_source,page_number):
    '''
    Description    :   Validate the page sign-in 
    Input Params   :   <page_title>       Title of the page
                       <page_source>      Source HTML of page
                       <page_number>      Number of steps/hops to
                                          next page
    Output Params  :   1      if password is valid
                       0      if password is not valid
    '''
    page_number = int(page_number)
    if page_number > 0 and page_number<=2:
        m1 = re.search(Kone_title[page_number-1],page_title)
        m2 = re.search(kone_button_1[page_number-1],page_source)
        m3 = re.search(kone_button_2[page_number-1],page_source)
    else:
        return 0
    if m1 and m2 and m3:
        return '1'
    else:
        return '0'

def button_navigator(button_source_links, button):
    '''
    Description    :   Navigate to Sign in page based on link clicked 
    Input Params   :   <button_source_links>       Links for each button
                       <button>                    Button name
    Output Params  :   ele      Links associated with each button
                       0        if invalid button 
    '''
    for key in kone_navigate.keys():
        if key == button:
            for ele in button_source_links:
                m = re.search(kone_navigate[key],ele)
                if m:
                    return ele
    return 0


def OpenWeblink(link):
    '''
    Description    :   Open the Iotportal 
    Input Params   :   <link>           Link for naviagating
    Output Params  :   <browser>        Object of browser
                       <title>          Page Title
                       <page_source>    Page source
                       <message>        if invalid URL link is given
    '''
    val = validate_url(link)
    if val:
        # create a new Firefox session
        browser = webdriver.Chrome()
        browser.implicitly_wait(15)
        browser.maximize_window()
        # Navigate to the application home page
        browser.get(link)
        time.sleep(15)
        title = browser.title
        page_source = browser.page_source
        #browser.quit()
        return (browser,title,page_source)
    else:
        print ("INVALID URL GIVEN ->", link)
        return ('Invalid URL')

def Teardown(browser):
    #function to close the browser object
    browser.quit()

def Navigatelinkbutton(button,link):
    '''
    Description    :   Navigate to link based on button selection 
    Input Params   :   <link>           Link for naviagating
                       <button>         Button for navigation
    Output Params  :   <browser>        Object of browser
                       <message>        Appropriate message
    '''
    browser,title,page_source = OpenWeblink(link)
    links_button = []
    links_button_obj = browser.find_elements_by_xpath("//a[@href]")
    for elem in links_button_obj:
        links_button.append((elem.get_attribute("href")))
    navigator = button_navigator(links_button,button)
    if navigator:
        browser.get(navigator)
        time.sleep(10)
        page_source = browser.page_source
        title = browser.title
        check = validate_page_signin(title,page_source,2)
        if check == '1' :
            return ('Valid page',browser)
        else:
            
            return ('Navigated to invalid page',browser)
    else:
        return ('Invalid button given',browser)

    
def CorrectSignin(browser,username, password):
    '''
    Description    :   This function tests at script level if
                       correct password is being sent 
    Input Params   :   <browser>        Object of browser
                       <username>       Username for login
                       <password>       password for login
    Output Params  :   <browser>        Object of browser
                       <message>        Appropriate message
    '''
    #browser,title,page_source = OpenWeblink(link)
    m_user = validate_username(username)
    if m_user:
        m_pass = validate_password(password)
        if m_pass:
            try:
                user = browser.find_element_by_name("username")
                user.send_keys(username)
                passw = browser.find_element_by_name("password")
                passw.send_keys(password)
                passw.send_keys(Keys.RETURN)
                time.sleep(10)
            except:
                pass
            return ('Logged in to system', browser)
        else:
            return ('Invalid Password',browser) 
    else:
        return ('Invalid Username',browser)

def parser(data, equipmentid):
    '''
    Description    :   Parse the data and find equipment 
    Input Params   :   <data>             Data/ complete source html code
                       <equipmentid>      Equipment ID to verify
    Output Params  :   1      if found
                       0      if not found
    '''
    m1 = re.search(equipmentid, data)
    m2 = re.search(kone_username,data)
    if m1 and m2:
        return 1
    else:
        return 0

def SearchEquipment(browser):
    '''
    Description    :   Navigation to search quipment page
    Input Params   :   <browser>        Object of browser
    Output Params  :   <message>        Appropriate message
    '''
    title = browser.title
    m = re.search(r'IoT Portal',title)
    if m:
        searchbox = browser.find_element_by_id(kone_searchid)
        searchbox.send_keys(kone_searchkey)
        searchbox.send_keys(Keys.RETURN)
        time.sleep(8)
        innerHTML = browser.execute_script("return document.body.innerHTML")
        flag = parser(innerHTML, kone_equipid)
        if flag:
            return 'Equipment found'
        else:
            count = 10
            for i in range(count):
                load = browser.find_element_by_id("id_loadmore")
                load.click()
                time.sleep(6)
                innerHTML = browser.execute_script("return document.body.innerHTML")
                flag = parser(innerHTML, kone_equipid)
                if flag:
                    return 'Equipment found'
            return 'Equipment Not found'
    else:
        return 'Navigated to Invalid Search link'

def username_forgot_validate(browser):
    '''
    Description    :   Validation of forgot username page
    Input Params   :   <browser>        Object of browser
    Output Params  :   <message>        Appropriate message
    '''
    lst = []
    links = browser.find_elements_by_xpath("//a[@href]")
    for link in links:
        lst.append((link.get_attribute("href")))

    for val in lst:
        m = re.search(r'forgot_username', val)
        if m:
            browser.get(val)
            time.sleep(5)
            title  = browser.title
            m2 = re.search (r'Forgot Username',title)
            return 'Forgot Username Page'
    return 'Invalid Page'

def userpassw_forgot_validate(browser):
    '''
    Description    :   Validation of forgot password page
    Input Params   :   <browser>        Object of browser
    Output Params  :   <message>        Appropriate message
    '''
    lst = []
    links = browser.find_elements_by_xpath("//a[@href]")
    for link in links:
        lst.append((link.get_attribute("href")))

    for val in lst:
        m = re.search(r'forgot_password', val)
        if m:
            browser.get(val)
            time.sleep(5)
            title  = browser.title
            m2 = re.search (r'Forgot Password',title)
            return 'Forgot Password Page'
    return 'Invalid Page'
        
def InCorrectSignin(browser,username, password):
    '''
    Description    :   This function tests behaviour in page if
                       incorrect username/password is being sent
    Input Params   :   <browser>        Object of browser
                       <username>       Username for login
                       <password>       password for login
    Output Params  :   1      if password is valid
                       0      if password is not valid
    '''
    #browser,title,page_source = OpenWeblink(link)
    err_msg = r"FBTBLU101E The userid or password that you entered is not correct."
    try:
        user = browser.find_element_by_name("username")
        user.send_keys(username)
        passw = browser.find_element_by_name("password")
        passw.send_keys(password)
        passw.send_keys(Keys.RETURN)
        time.sleep(5)
    except:
        pass

    innerHTML = browser.execute_script("return document.body.innerHTML")
    m = re.search (err_msg,innerHTML)
    if m:
        return '1'
    else:
        return '0'
    
    
    
    
        
