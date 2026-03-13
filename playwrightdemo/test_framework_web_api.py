import json
import time
#  pytest playwrightdemo/test_framework_web_api.py --browser_name edge --html=report.html --tracing on
import pytest
from playwright.sync_api import Playwright, expect

from playwrightdemo.Utils.apiBase import ApiBase
from playwrightdemo.pageObjects.dashboard import DashboardPage
from playwrightdemo.pageObjects.login import LoginPage
from playwrightdemo.pageObjects.orderhistory import OrderHistorypage

######## Json file
with open("playwrightdemo/Data/credentails.json") as f:
   test_data = json.load(f)
   print(test_data)
   credentials_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials',credentials_list)
def test_Api(playwright:Playwright,browser_instance,user_credentials):

   userEmail = user_credentials['userEmail']
   userPassword = user_credentials['userPassword']

   #################### Create Order using API
   api = ApiBase()
   order_id = api.createOrder(playwright,user_credentials)

   ################### login
   login = LoginPage(browser_instance)
   login.navigate()
   login.login(userEmail,userPassword)
   dashboard = DashboardPage(browser_instance)
   dashboard.ordersNavLink()
   orderhistory = OrderHistorypage(browser_instance)
   orderhistory.orderhistory(order_id)
   ############### order history









