import requests
proxyPOST = ''

filename = 'p.txt'
# change it to your file name

with open(filename,'r') as proxies:
	proxyLine = proxies.readlines()
for proxy in proxyLine:
	proxyPOST += proxy.strip()+','
proxyPOST = proxyPOST[:-1]

r = requests.session()
a = r.post('https://api.proxyscan.io',data={'proxies':proxyPOST})
# print(a.text) myUniqueKey to get Proxies That are processed
getURL = 'https://api.proxyscan.io/?id='+str(a.text)[1:-1]
b = requests.get(getURL)
root = b.json()
for i in range(len(root)):
	if not root[i]["failed"]:
		# all working proxies are here
		ip = root[i]["ip"]
		port = root[i]["port"]
		ping = root[i]["ping"]
		proxyProtocol = root[i]["type"][0]
		anonymityType = root[i]["anonymity"]
		# other data left to add if you want you can add them here
		# such as country residential host bla bla
		print(str(ip)+':'+str(port)+str(proxyProtocol))