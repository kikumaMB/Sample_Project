import time
import unittest
from telnetlib import EC
from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Tests_Android.do_actions import do_action


class mb_guide_android_functional_val(unittest.TestCase):

    def setUp(self):
        desired_capabilities = {
            'platformName': 'Android',
            'platformVersion': '13',
            'deviceName': 'S22',
            'appPackage': 'com.daimler.moba.kundenapp.android',
            'appActivity': 'com.daimler.guide.activity.SplashActivity',
            'automationName': 'UiAutomator2',
            'udid': 'RZCT811R6JB',
            'newCommandTimeout': 300,
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }

        self.driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_capabilities)

    def test_install_Guide(self):
        # Launch the app
        wait = WebDriverWait(self.driver, 10)
        Chrome = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@content-desc ="Chrome"]')))
        Chrome.click()
        enter_app_center = wait.until(
            EC.visibility_of_element_located((By.ID, 'com.android.chrome:id/full_url_text_view')))
        enter_app_center.click()

    def back_tap(self):
        wait = WebDriverWait(self.driver, 10)
        back = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'android.widget.ImageButton')))
        back.click()

    def scroll_4(self):
        i = 1
        while i < 4:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(456, 1813)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(507, 414)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(2)
            i += 1

    def test_Validate_App_Version(self):
        wait = WebDriverWait(self.driver, 10)
        Legal_icon = wait.until(
            EC.visibility_of_element_located((By.ID, 'com.daimler.moba.kundenapp.android:id/imprint')))
        app_version = self.driver.find_element(By.XPATH,
                                               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.TextView")
        Current_App_version = app_version.text
        Actual_App_version = ""
        if Current_App_version == Actual_App_version:
            print("App Version Matched")
        else:
            print("App version Did not match")

    def test_Legal_IconValidation(self):
        wait = WebDriverWait(self.driver, 10)
        Legal_icon = wait.until(
            EC.visibility_of_element_located((By.ID, 'com.daimler.moba.kundenapp.android:id/imprint')))
        Legal_icon.click()
        mb_guide_android_functional_val.back_tap(self)

    def test_Accept_Legal(self):
        wait = WebDriverWait(self.driver, 10)
        Legal_icon = wait.until(
            EC.visibility_of_element_located((By.ID, 'com.daimler.moba.kundenapp.android:id/imprint')))
        # Scroll to down bottom
        i = 1
        while i < 4:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(456, 1813)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(507, 414)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(2)
            i += 1

        Deny_btn = wait.until(
            EC.visibility_of_element_located((By.ID, "com.daimler.moba.kundenapp.android:id/deny_button")))
        Deny_btn.click()
        wait.until(
            EC.visibility_of_element_located((By.ID, "com.daimler.moba.kundenapp.android:id/button_text"))).click()
        Accept_btn = wait.until(
            EC.visibility_of_element_located((By.ID, "com.daimler.moba.kundenapp.android:id/accept_button")))
        Accept_btn.click()

        MyGuide_Homepage = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/no_results"))).is_displayed()

        if MyGuide_Homepage == True:
            print("Legal Accepted Successfully")
        else:
            print("Legal Accept Failed")
            self.assertFalse(self)

    def test_Side_Nav_Validation(self):
        wait = WebDriverWait(self.driver, 10)
        # Myguides
        hambergun_menu = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//android.widget.ImageButton[@content-desc='Open navigation drawer']")))
        hambergun_menu.click()
        myguides_opt = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/nav_myguide")))
        myguides_opt.click()

        # Setting
        hambergun_menu = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//android.widget.ImageButton[@content-desc='Open navigation drawer']")))
        hambergun_menu.click()
        setting = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/nav_settings")))
        setting.click()
        mb_guide_android_functional_val.back_tap(self)

        # Legal_icon
        hambergun_menu = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//android.widget.ImageButton[@content-desc='Open navigation drawer']")))
        hambergun_menu.click()
        setting = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/nav_settings")))
        setting.click()
        mb_guide_android_functional_val.back_tap(self)

        # FAQ
        hambergun_menu = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//android.widget.ImageButton[@content-desc='Open navigation drawer']")))
        hambergun_menu.click()
        FAQ = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/nav_about")))
        FAQ.click()
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(67, 1440)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(1323, 1434)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def test_online_browse_guide(self):
        wait = WebDriverWait(self.driver, 10)
        AddGuide_btn = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/button_add")))
        AddGuide_btn.click()

        i = 1
        while i < 3:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(456, 1813)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(507, 414)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(2)
            i += 1

        carline_name = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@text='X-Class']")))
        carline_name.click()

        # Tap on online
        Open_Online = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/btn_summary_online")))
        Open_Online.click()

        # Tap on Need more Info
        Tap_on_Need_info = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/needMoreInfo")))
        Tap_on_Need_info.click()
        mb_guide_android_functional_val.back_tap(self)
        Open_Online = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/btn_summary_online")))
        Open_Online.click()

        # Tap on Confirm
        Tap_on_cfrm = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/ok")))
        Tap_on_cfrm.click()

    def test_browse_QucikStart(self):
        wait = WebDriverWait(self.driver, 10)
        mb_guide_android_functional_val.test_online_browse_guide(self)

        self.driver.implicitly_wait(3)
        Tap_on_QucikStart = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@text='Operating Instructions']")))
        Tap_on_QucikStart.click()

        Tap_on_OM = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/txt_document_topic")))
        Tap_on_OM.click()

        Tap_on_Content = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@text='At a glance']")))
        Tap_on_Content.click()

        Tap_on_in_Con = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@text='Cockpit']")))
        Tap_on_in_Con.click()
        mb_guide_android_functional_val.scroll_4(self)

        Tap_on_Top = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/button_text")))
        Tap_on_Top.click()

        Tap_on_More_lnk = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//android.view.View[@content-desc='more'])[1]")))
        Tap_on_More_lnk.click()

        Tap_on_topmenu = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/toolbar_spinner")))
        Tap_on_topmenu.click()

        Tap_on_homepage = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@text='Guide homepage']")))
        Tap_on_homepage.click()

        Tap_on_Search = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@text ='Search']")))
        Tap_on_Search.click()

        enter_keyword = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/search_src_text")))
        enter_keyword.send_keys("AIR")

        Tap_Search_res = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@text ='Air filter (white display message)']")))
        Tap_Search_res.click()

        mb_guide_android_functional_val.scroll_4(self)
        mb_guide_android_functional_val.back_tap(self)
        mb_guide_android_functional_val.back_tap(self)


    def test_Download_guide_offline(self):
        wait = WebDriverWait(self.driver, 10)
        AddGuide_btn = wait.until(EC.visibility_of_element_located(
            (By.ID, "com.daimler.moba.kundenapp.android:id/button_add")))
        AddGuide_btn.click()

        i = 1
        while i < 3:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(456, 1813)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(507, 414)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(2)
            i += 1

        carline_name = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@text='X-Class']")))
        carline_name.click()

        tap_on_Download = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "")))
        tap_on_Download.click()








