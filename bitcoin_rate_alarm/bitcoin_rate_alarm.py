import requests as rq
from bs4 import BeautifulSoup as bs
import time
import playsound as pl

# out_print = ""
def get_price():
	get_url = rq.get("https://www.google.com/finance/quote/BTC-USD")
	soup = bs(get_url.content, "html.parser")
	get_price = soup.find('div', {'class':'YMlKec fxKbKc'})
	return str(get_price.text).replace(",","")


previuos_price = 0

while True:
	new_price = float(get_price())
	if new_price > previuos_price:
		previuos_price = new_price
		pl.playsound('source/naruto_shadow.mp3')
	elif new_price < previuos_price:
		previuos_price = new_price
		pl.playsound('source/u_suffer.mp3')
	elif new_price == previuos_price:
		previuos_price = new_price
		print("Stable")
	time.sleep(1)


""" 
get price constanly


calculate percentage of price

store result to the previous data

scrap new price every 2 second(for first test) and calculate its percentage

store to the new data

compare value of previous data and new data

if something is less than another -> do something and shift value of new data to previous data

elif something is greate than another -> do something and shift value of new data to previous data

"""

# pl.playsound('source/export_ofoct_uz3AV4x.mp3')