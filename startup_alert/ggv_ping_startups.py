from __future__ import unicode_literals
import smtplib
import scrapy
from scrapy.selector import Selector
import csv
import datetime
import re
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
from gspread2 import GoogleSpreadsheets
import json
import oauth2client
from oauth2client import client
from oauth2client import tools
try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

APPLICATION_NAME = 'Golden Gate Ventures Scraping'
__author__ = "Yada Pruksachatkun with credits to the creator of pygsheets for their authorize and get_credentials function"
SPREADSHEET_ID = '1Vfk-gmYLl_wqJmpEANAy1QhcPYt_bUBvmOqlj0WXw0M'
LIMIT = '500'


def get_credentials(client_secret_file):
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def authorize(file = 'client_secret.json',credentials = None):
    """Login to Google API using OAuth2 credentials.
    This is a shortcut function which instantiates :class:`Client`
    and performs login right away.
    :returns: :class:`Client` instance.
    """
    if not credentials:
        credentials = get_credentials(file)
    rclient = GoogleSpreadsheets(auth=credentials)
    return rclient


def upload():
      """ Input: Contents - Array of newly scraped contents to
          put into CSV file
          This function separates the newly scraped contents into
          content that has been scraped before last week and new
          content this week and updates accordingly.
      """
      scope = ['https://spreadsheets.google.com/feeds']
      gc = authorize()
      last_week = gc.get(SPREADSHEET_ID, 'A1:E6', 'Investments')
      print(last_week)
      return


def create_message(message_text):
 
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("yadacmis@gmail.com", "th1nk428H!")
  msg = message_text
  server.sendmail("yadacmis@gmail.com", "ypruksac@wellesley.edu", msg)
  server.quit()

upload()