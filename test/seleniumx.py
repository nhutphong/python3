from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# ok
# pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager


important = """

class By

    ID = "id"
    NAME = "name"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"



    <html>
         <body>
          <form id="loginForm">
           <input name="username" type="text" />
           <input name="password" type="password" />
           <input name="continue" type="submit" value="Login" />
           <input name="continue" type="button" value="Clear" />
          </form>

            <p class="content">Site content goes here.</p>

            <h1>Welcome</h1>
            <p>Site content goes here.</p>
            <a href="continue.html">Continue</a>


        </body>

    </html>

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
continue = driver.find_element(By.NAME, 'continue')
content = driver.find_element(By.CLASS_NAME, 'content')
heading1 = driver.find_element(By.TAG_NAME, 'h1')
content = driver.find_element(By.CSS_SELECTOR, 'p.content')
continue_link = driver.find_element(By.LINK_TEXT, 'Continue')



class Keys:
    Keys.ADD              Keys.F11              Keys.NUMPAD2
    Keys.ALT              Keys.F12              Keys.NUMPAD3
    Keys.ARROW_DOWN       Keys.F2               Keys.NUMPAD4
    Keys.ARROW_LEFT       Keys.F3               Keys.NUMPAD5
    Keys.ARROW_RIGHT      Keys.F4               Keys.NUMPAD6
    Keys.ARROW_UP         Keys.F5               Keys.NUMPAD7
    Keys.BACKSPACE        Keys.F6               Keys.NUMPAD8
    Keys.BACK_SPACE       Keys.F7               Keys.NUMPAD9
    Keys.CANCEL           Keys.F8               Keys.PAGE_DOWN
    Keys.CLEAR            Keys.F9               Keys.PAGE_UP
    Keys.COMMAND          Keys.HELP             Keys.PAUSE
    Keys.CONTROL          Keys.HOME             Keys.RETURN
    Keys.DECIMAL          Keys.INSERT           Keys.RIGHT
    Keys.DELETE           Keys.LEFT             Keys.SEMICOLON
    Keys.DIVIDE           Keys.LEFT_ALT         Keys.SEPARATOR
    Keys.DOWN             Keys.LEFT_CONTROL     Keys.SHIFT
    Keys.END              Keys.LEFT_SHIFT       Keys.SPACE
    Keys.ENTER            Keys.META             Keys.SUBTRACT
    Keys.EQUALS           Keys.MULTIPLY         Keys.TAB
    Keys.ESCAPE           Keys.NULL             Keys.UP
    Keys.F1               Keys.NUMPAD0          Keys.ZENKAKU_HANKAKU
    Keys.F10              Keys.NUMPAD1          Keys.mro()



main_window= driver.current_window_handle
#Open a new tab in blank

# driver.execute_script("window.open('https://google.com.vn'),'_blank'")

driver.switch_to.new_window('tab')
driver.switch_to.new_window('tab')
driver.switch_to.new_window('tab')
# driver.switch_to.new_window('window')


driver.current_window_handle

    # Opens a new tab and switches to new tab
driver.switch_to.new_window('tab')

    # Opens a new window and switches to new window
driver.switch_to.new_window('window')
  
    #Close the tab or window
driver.close()

    #Switch back to the old tab or window
driver.switch_to.window(original_window)
  

driver.save_screenshot('screenshot.png')
driver.quit()

user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver.get("https://www.facebook.com")

time.sleep(3)
element_email = driver.find_element(By.ID, "email")
# gui user_name toi element 'email' ngoai 'html'
element_email.send_keys(user_name)


time.sleep(3)
element = driver.find_element(By.ID, "pass")
element.send_keys(password)

element.send_keys(Keys.RETURN)

time.sleep(3)
element.close()

"""

def newtab(driver, url='google.com.vn', hint='_blank'):
    driver.execute_script(f"window.open('https://{url}', '{hint}')")
    """
        '_blank' newtab
        '_self' current tab
    """


driver = webdriver.Chrome(ChromeDriverManager().install())