import requests
import time
import datetime

loop = 1

ustonks_debt = 30 #CHANGE THIS TO YOUR NUMBER OF MINTED USTONKS
ustonks_collat = 20000 #CHANGE THIS TO YOUR USDC COLLATERAL

ugas_debt = 42 #CHANGE THIS TO YOUR NUMBER OF MINTED UGAS
ugas_collat = 13 #CHANGE THIS TO YOUR ETH COLLATERAL

while loop == 1:
    hour = datetime.datetime.now().hour
    if hour == 7 or hour == 12 or hour == 21: #CHANGE THESE NUMBERS TO GET ALERTS AT DIFFERENT TIMES EVERY DAY -> 7 REPRESENTS 07:00 UTC
        ustonks = requests.get('https://data.yam.finance/ustonks/index').json() #INDEX PRICE USED CURRENTLY INSTEAD OF THE 2 HOUR TWAP WHILE THE ENDPOINT IS BEING CREATED
        ugas = requests.get('https://data.yam.finance/twap/pair/0x2b5dfb7874f685bea30b7d8426c9643a4bcf5873').json()

        ustonks_t = ustonks['timestamp']
        ustonks_p = round(ustonks['price'],2)

        ugas_t = ugas['timestamp']
        ugas_p = round(int(ugas['price'])/1e18,6)

        ugas_cr = round(ugas_collat/(ugas_debt*ugas_p),2)
        ustonks_cr = round(ustonks_collat/(ustonks_debt*ustonks_p),2)
        #REPLACE THE TWO XXX BELOW WITH YOUR BOT'S TOKEN AND CHAT ID FROM THE TUTORIAL VIDEO IN THE README FILE
        url = f'https://api.telegram.org/botXXX/sendMessage?chat_id=XXX&text=  uStonksAPR21: {ustonks_p} CR: {ustonks_cr} \n uGasJun21: {ugas_p} CR: {ugas_cr}'
        requests.get(url)
    print('Sleeping for an hour...')
    time.sleep(60*60)
