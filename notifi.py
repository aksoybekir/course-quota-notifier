from bs4 import BeautifulSoup
import requests
import time
from pushsafer import init, Client
from urllib.parse import urlencode
from urllib.request import Request, urlopen


while True:
	psy = 'http://registration.boun.edu.tr/scripts/quotasearch.asp?abbr=PSY%20&code=101&section=02&donem=2018/2019-1'

	psyhtml = requests.get(psy)

	psydata = psyhtml.text

	psysoup = BeautifulSoup(psydata, 'html.parser')

	psycurrentstudent = 0

	for current in psysoup.find_all('p')[8]:
		psycurrentstudent = int(current)

	print(psycurrentstudent)

	htr = 'http://registration.boun.edu.tr/scripts/quotasearch.asp?abbr=HTR%20&code=311&section=12&donem=2018/2019-1'

	htrhtml = requests.get(htr)

	htrdata = htrhtml.text

	htrsoup = BeautifulSoup(htrdata, 'html.parser')

	htrcurrentstudent = 0

	for current in htrsoup.find_all('p')[8]:
		htrcurrentstudent = int(current)

	print(htrcurrentstudent)

	if psycurrentstudent<50 or htrcurrentstudent<45:
		break

	time.sleep(60)


url = 'https://www.pushsafer.com/api' # Set destination URL here
post_fields = {                       # Set POST fields here
	"t" : 'Ders',
	"m" : 'empty',
	"s" : '',
	"v" : 3,
	"i" : 100,
	"c" : '#FF0000',
	"d" : 'a',
	"u" : 'https://www.pushsafer.com',
	"ut" : 'Open Link',
	"k" : 'USER_KEY_PUSH_SAFER'
}

if psycurrentstudent<50:
	post_fields["m"] = "PSY KOTA BOŞ"

if htrcurrentstudent<45:
	post_fields["m"] = "HTR KOTA BOŞ"

if htrcurrentstudent<45 and psycurrentstudent<50:
	post_fields["m"] = "HTR ve PSY İKİSİ DE BOŞ"


request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)


print('çıktı')

