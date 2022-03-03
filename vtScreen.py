#!/usr/bin/python3
import os
from telnetlib import IP
import os.path
import argparse
import urllib.request as urllib
import urllib.request as urlRequest
import urllib.parse as urlParse
import platform

from PIL import Image
from selenium import webdriver

import time

from selenium.webdriver.chrome.options import Options
from pygments import highlight, lexers, formatters
from pyfiglet import Figlet
from dotenv import load_dotenv

parser = argparse.ArgumentParser(
    description='This program utilizes the VirusTotal.com to perform queries about IP addresses and Hashes and makes a ScreenShot.'
)
# Inputs
required = parser.add_mutually_exclusive_group()

required.add_argument(
    "-i",
    "--ip",
    help="lookup a single IP address",
    action="store")

required.add_argument(
    "--hash",
    help="lookup a single hash",
    action="store")

"""
required.add_argument(
    "-l",
    "--list",
    help="lookup a list of IPs",
    action="store")
"""
args = parser.parse_args()


def imgShow(DATA):
    img="Virustotal_"+DATA+'.png'
    if(platform.system() == "Windows"):
        os.system('start '+img)
    else:
        os.system("shotwell "+img)
     
def takeScreenshot(DATA):
    URL = "https://www.virustotal.com/gui/search/"+DATA
    options = webdriver.ChromeOptions()
    options.headless = True
    if(platform.system() == "Windows"):
        #Windows
        driver = webdriver.Chrome("./chromedrivers/chromedriver.exe")
    else:
        #Linux
        driver = webdriver.Chrome("./chromedrivers/chromedriver")
    driver.get(URL)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    #driver.set_window_size(S('Width'),S('Height'), driver.window_handles[0]) # May need manual adjustment
    #driver.set_window_size(1366,1800, driver.window_handles[0]) # Manual Adjusted, like a phone
    driver.set_window_size(1366,1800) # Manual Adjusted
    time.sleep(2)
    driver.find_element_by_tag_name('body').screenshot('Virustotal_'+DATA+'.png')
    driver.quit()

def main():
    if args.hash:
        takeScreenshot(args.hash)
        imgShow(args.hash)
    
        
    else:
        exit(
            "Error: one of the following arguments are required: -i/--ip, more work in progress")


if __name__ == '__main__':
    main()