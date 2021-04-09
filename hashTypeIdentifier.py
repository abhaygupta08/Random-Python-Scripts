import requests
import regex as re

ahash = input('Enter Hashed String : ')
ahash = ahash.strip()



r = requests.session()
a = r.get('https://hashes.com/en/tools/hash_identifier')
csrf_token = re.findall('<input type="hidden" name="csrf_token" value="([^"]*)',a.text)[0]
# print(csrf_token)
postData = {
	'csrf_token': csrf_token,
'hashes': ahash,
'submitted': 'true'
}

b = r.post('https://hashes.com/en/tools/hash_identifier',data=postData)
# print(b.text)
print(re.findall(ahash+'([^\S]*-[^\S]*)([^<]*)',b.text)[0][1])