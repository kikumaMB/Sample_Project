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


class do_action:

    def back_tap(self):
        wait = WebDriverWait(self.driver, 10)
        back = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'android.widget.ImageButton')))
        back.click()

    def do_down_Single_Scroll(self):
            i = 1
            while i < 2:
                actions = ActionChains(self.driver)
                actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                actions.w3c_actions.pointer_action.move_to_location(547, 2545)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.move_to_location(564, 536)
                actions.w3c_actions.pointer_action.release()
                actions.perform()
                i += 1
    def do_down_scroll_twice(self):
            i = 1
            while i < 3:
                actions = ActionChains(self.driver)
                actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                actions.w3c_actions.pointer_action.move_to_location(547, 2545)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.move_to_location(564, 536)
                actions.w3c_actions.pointer_action.release()
                actions.perform()
                i += 1

    def do_down_scroll_thrice(self):
            i = 1
            while i < 4:
                actions = ActionChains(self.driver)
                actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                actions.w3c_actions.pointer_action.move_to_location(547, 2545)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.move_to_location(564, 536)
                actions.w3c_actions.pointer_action.release()
                actions.perform()
                i += 1

    def do_down_scroll_four(self):
        i = 1
        while i < 5:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(547, 2545)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(564, 536)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            i += 1

    def do_scroll_to_Bottom(self):
        i = 1
        while i < 8:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(547, 2545)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(564, 536)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            i += 1

    def do_Top_scroll(self):
        i = 1
        while i < 8:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(523, 494)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(515, 1871)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            i += 1
