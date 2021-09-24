import bs4, requests

def getPrice(url):
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._30jeq3._16Jk6d')
        return elems[0].text.strip()

url = 'https://www.flipkart.com/sandisk-sdddc3-128g-i35-128-otg-drive/p/itm4b9a04e72261c?pid=ACCFMSEVDEHGSVFF&lid=LSTACCFMSEVDEHGSVFFIU2TYD&marketplace=FLIPKART&store=6bo&srno=b_1_2&otracker=hp_omu_Top%2BOffers_4_4.dealCard.OMU_ZVID7GRZ390B_4&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_4_NA_view-all_4&fm=neo%2Fmerchandising&iid=133355c8-38a5-407b-a1e5-6e338a0b928e.ACCFMSEVDEHGSVFF.SEARCH&ppt=browse&ppn=browse&ssid=pt9y2oltds0000001623752828866'
price = getPrice(url)
print('The price is ' + price)
