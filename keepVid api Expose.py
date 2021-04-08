import requests
import random
import urllib.parse

inputUrl = input("Enter YT url: ")
print("[+]\t",inputUrl)
print("Working...")

r = requests.session()
url = "https://keepv.id/"+str(random.randint(1,20))+"/"
page = r.get(url,verify=False);
ssid = page.cookies['PHPSESSID']
print(ssid)
head = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'PHPSESSID='+ssid+'; _ga=GA1.2.1154418929.1615288252; _gid=GA1.2.245978578.1615288252; _ga_RZYTG6REG8=GS1.1.1615288247.1.0.1615289202.0',
'Host': 'keepv.id',
'Origin': 'https://keepv.id',
'Referer': url,
'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}
params = {
	'url': urllib.parse.quote_plus(inputUrl),
	'sid': ssid,
}
postUrl = r.post("https://keepv.id/",headers=head,data=params,verify=False)
print(postUrl.text)
print("RTEXT",postUrl.text)
print("\n")
print(postUrl.cookies)

r.close()