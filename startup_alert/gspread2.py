from apiclient import discovery
import httplib2

__author__ = "Yada Pruksachatkun"

class GoogleSpreadsheets(object):

    """ This class communicates with the Google API and does not rely on the latest version of OpennPyssl.
        Basic get, clear, update, and append to a worksheet.
        The authorize() and get_credentials() function was adapted from the source code for pygsheets.
    """
    def __init__(self, auth):
        self.auth = auth
        http = auth.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')
        self.service = discovery.build('sheets', 'v4', http=http,
                          discoveryServiceUrl=discoveryUrl)

    def get(self, spreadsheetId, rangeName, spreadSheetName):
        rangeOutput = spreadSheetName + "!" + rangeName
        res = self.service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId,
            range=rangeOutput ).execute()
        return res

    def clear_worksheet(self, spreadsheetId):
        myBody = {
          "requests": [
            {
              "updateCells": {
                "range": {
                  "sheetId": 0
                },
                "fields": "userEnteredValue"
              }
            }
          ]
        }
        response = self.service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId,
                                                       body=myBody).execute()

    def update(self, data, spreadsheetId, rangeName):
        myBody = {u'range': rangeName, u'values': data, u'majorDimension': u'ROWS'}
        res = self.service.spreadsheets().values().update(
        spreadsheetId=spreadsheetId,
        range=rangeName,
        valueInputOption='RAW',
        body=myBodsy ).execute()


    def append(self, data, spreadsheetId, rangeName):
        values = {u'range': rangeName, u'values': data , u'majorDimension': u'ROWS'}
        res = self.service.spreadsheets().values().append(
            spreadsheetId=spreadsheetId,
            range=rangeName,
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',
            body=values ).execute()
