import requests
import regex as re

r = requests.session()
def chkEmail(email):
	params = {'em': email,
'hl': 'checkeremail.com',
'frm': 'example@gmail.com'}
	b = r.post('https://checkeremail.com/checker-validation.php',data=params)
	resp = re.findall('>(.+)<',b.text)[0]
	print(email,':',resp)
chkEmail('pziko099@moist.gq')
# chkEmail('yhcryygxjmjcc@baybabes.com')
# chkEmail('pziko0as99@masst.gq')
chkEmail('pzikass99@moist.gq')