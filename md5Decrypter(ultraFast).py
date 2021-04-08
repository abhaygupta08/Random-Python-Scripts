import requests
import regex as re

found = 0
ahash = input('Enter Hashed String : ')
ahash = ahash.strip()

if ahash=='':
	ahash = 'Invalid Input !'
	exit()

if len(ahash)!=32:
	print('Not a md5 hash !')
	exit()

# print(hash)

api1 = 'https://md5.gromweb.com/?md5='+ahash

r = requests.get(api1,timeout=2)
if 'succesfully reversed' in r.text:
	dehash = re.findall('<em class="long-content string">(.*)<\/em>',r.text)[0]
	print('[+] Found : ',dehash)
	found = 1
else:
	print("[-] Not Found     Site : Goemweb")

if found:
	exit()

api2 = 'https://md5decrypt.net/en/'
r = requests.session()
a = r.get(api2)
# print(a.text)
captchaName = re.findall('<input id="captcha" type="text" name="([^"]*)',a.text)[0]
temp = re.findall('<input type="hidden" name="(.*)"\svalue="(.*)"\/>',a.text)

# print(temp[0][0],temp[0][1])
data = {'hash': ahash, captchaName: '', 
temp[0][0] : temp[0][1],
'decrypt': 'Decrypt',
}

b = r.post(api2,data=data)
# print(b.text)
if 'Sorry, this hash is not in our database' in b.text:
	print('[-] Not Found   site : md5decrypt.net')
else:
	print('[+] Found : ',end='')
	found = 1
	print(re.findall('<\/div><br\/>(.*)<br\/><br\/>',b.text)[0])




'''
NOT WORKING

r = requests.session()
b = r.get('https://www.dcode.fr/md5-hash')
phpsessid = re.findall('<RequestsCookieJar\[<Cookie PHPSESSID=(.*)\sfor',str(b.cookies))[0]

api3 = 'https://www.dcode.fr/api/'
postData = {
	'tool': 'md5-hash',
'hash': ahash,
'salt1': '', 
'salt2': '' 
}
a = r.post(api3,data=postData,headers={'cookie':'_ga=GA1.2.841216504.1615373096; __qca=P0-574343998-1615373099869; __gads=ID=8ff7dcf12a6a0d12-22a1d2864cc60091:T=1615373105:RT=1615373105:S=ALNI_MYGcvdFlJqKLudnKvdEgWWi_n29iw; PHPSESSID='+phpsessid+'; _gid=GA1.2.837192932.1617852981; _gat_gtag_UA_647045_2=1'})
print(postData)
print(a.text)
'''

if found:
	exit()

#API4
r = requests.session()
a = r.get('https://hashes.com/en/decrypt/hash')
csrf_token = re.findall('<input type="hidden" name="csrf_token" value="([^"]*)',a.text)[0]

postData = {
	'csrf_token': csrf_token,
'hashes': ahash,
'knn': 64,
'submitted': 'true'
}

b = r.post('https://hashes.com/en/decrypt/hash',data=postData)
if 'Left:' in b.text:
	print('[-] Not Found on hashes.com')
else:
	print('[+] Found : ',end='')
	found = 1
	dehash = re.findall(ahash+':([^<]*)',b.text)[0]
	print(dehash)


if found:
	exit()


# API5

a = requests.get('https://hashtoolkit.com/decrypt-hash/?hash='+ahash)
# print(a.text)
if 'No hashes found for' in a.text:
	print('[-] Not Found on hashtoolkit.com')
else:
	try:
		dehash = re.findall('<span title="decrypted md5 hash"><a href="([^"])*">([^<]*)<\/a>',a.text)[1]
		print('[+] Found :',dehash)
		found  = 1  
	except:
		print('[-] Security error on hashtoolkit.com site')

print('\n\tCant Found on all possible sites :(')
