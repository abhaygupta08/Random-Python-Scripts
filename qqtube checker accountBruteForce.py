import requests
from pprint import pprint
import brotli

r = requests.session()
# cookie: __cfduid=dfd22dbcbccbba91176caa39bd0436de51615694567; PHPSESSID=mr7bnjhpnbeo80que85kliukrr; f2ba620a7704401e34bf16ab4f548007=hPCaWPzjNFegciPm4LTycCY7GGNDts1VuMObzhiCbP%2FRvduC%2Fu%2BEcq7uvDxTnastqH9NRzTfCgsNdZePI5gWRj1HclE24xkQlNORnZjOhCr4Dj%2FV6XFV2XCP4jGzGc3r3MxINcsE1CHxjqXMnYRW%2FgzVHpUOETPzbZcbMjHB52Y%3D000121; __cflb=04dToVLgBGqGxGSZKow1nkWV8ww6UdTM3KabdHH2Di; _ga=GA1.2.1571346212.1615694587; _gid=GA1.2.1816393781.1615694587; _fbp=fb.1.1615694589588.1188647891; __mmapiwsid=d19cafc6-cbad-4023-8d6d-7850e77bcb62:a510bdffd7d42f18f4892b57f9826335241d22e2

head = {
	'authority': 'www.qqtube.com',
'method': 'POST',
'path': '/en/authentication',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'content-length': '62',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://www.qqtube.com',
'referer': 'https://www.qqtube.com/en/authentication',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

params ={
	'SubmitLogin': '1',
'email': 'yhcryygxjmjcc@baybabes.com',
'passwd': 'sdfdsf'
}

a = r.post('https://www.qqtube.com/en/authentication',data=params)
# texter = a.text.encode(encoding='UTF-8',errors='strict')
# brotli.decompress(a.content)

if 'Email does not exist' in a.text:
	print('Email does not exist')
else:
	print('gotit ')