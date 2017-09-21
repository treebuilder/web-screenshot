#!/usr/bin/env python
import sys
from selenium import webdriver
from depot.manager import DepotManager
# Usage: grabscreen.py http://www.example.com 
depot = DepotManager.get()
driver = webdriver.PhantomJS()
driver.set_window_size(1024,768)
driver.get(sys.argv[1])
fqdn = sys.argv[1].split('//')[1]
driver.save_screenshot('%s.png' % fqdn)
