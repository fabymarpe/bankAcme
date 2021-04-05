import requests


class TransactionHelper:

    def trm(self):
        url = 'https://s3.amazonaws.com/dolartoday/data.json'
        response = requests.get(url=url)
        trm = response.json()["USDCOL"]["ratetrm"]
        return trm

    def convert_currency(self, money):
        trm = self.trm()
        return money * trm