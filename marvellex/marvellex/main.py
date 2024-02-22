import requests
import sqlite3

con = sqlite3.connect("marvellex_wallet.db")
cur = con.cursor()
# cur.execute("CREATE TABLE Accounts(adress TEXT, balance TEXT, stale TEXT)")

flag = True
page = 26999


while flag:
    response = requests.get(f"https://explorer.marvellex.com/api?module=account&action=listaccounts&page={str(page)}")
    page += 1
    response_json = response.json()
    if response_json["result"] != []:
        print(response.url)
        print(response.status_code)
        data = response_json["result"]
        for item in data:
            cur.execute("INSERT INTO Accounts (adress, balance, stale) VALUES ('{0}','{1}','{2}')".format(item["address"], item['balance'], item['stale']))
            con.commit()

    else:
        flag = False
        

con.close()