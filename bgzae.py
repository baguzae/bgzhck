# module
from os import system
from time import sleep
import sys, datetime
import os,sys,time
import requests, json, time, threading, os, sys
from colorama import Fore, init


# Config
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.WHITE


def login():
  url ="https://pastebin.com/raw/gUJqbQLW"
  response = requests.get(url)
  html = response.text
  username_1 = html
  username_2 = input(f'\n [TATO] {red} M̴A̴S̴U̴K̴K̴A̴N̴ ̴P̴A̴S̴S̴W̴O̴R̴D̴:{blue} ')
  if username_2 == username_1:
      time.sleep(2)
      os.system("cls||clear")
      print("""\33[0;35m==========================\33[0;36m=========================""")
      time.sleep(2)
      print("""\r\t \33[0;35m𝐌𝐲 𝐓𝐞𝐚𝐦:\33[0;36m Ⴆɠȥ ƈყႦҽɾ҉""")
      time.sleep(2)
      print("""\r\t \33[0;35m𝐇𝐚𝐜𝐤 𝐁𝐲:\33[0;36m 𝕭𝖆𝖌𝖚𝖟𝕬𝖊̷""")
      time.sleep(2)
      print("""\33[0;35m==========================\33[0;36m=========================""")
  else:
       print(f"{blue}--------------------------------------------")
       print(f'{red}       𝗦𝗖𝗥𝗜𝗣𝗧 𝗘𝗫𝗣𝗜𝗥𝗘𝗗 𝗦𝗜𝗟𝗔𝗛𝗞𝗔𝗡 𝗛𝗨𝗕𝗨𝗡𝗚𝗜 𝗔𝗗𝗠𝗜𝗡 𝕭𝖆𝖌𝖚𝖟𝕬𝖊')
       print(f"{green}--------------------------------------------")
       time.sleep(5)
       os.system("cls||clear")
       time.sleep(5)
       login()
login()


#menu 
def ketik(c):
    for e in c + "\n" :
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.010)
ketik("ˢᶜᴿᴵᴾᵀ ᴮᵁˢˢᴵᴰ ⱽ⁴.⁰.³")   
system("clear")
kal = datetime.datetime.now()
ketik(f"""
╔═\033[1;33;41m • \033[1;37mBUSSID VERSION V.4.0.3\033[1;33m• \033[0m\033[═
║\33[0;32m𝗔𝗨𝗧𝗢𝗥:\33[0;36mBaguz Ae\33[0;0m
║\33[0;32m𝗖𝗥𝗘𝗗𝗜𝗧𝗦:\33[0;36mBaguz Ae
\33[0;34m╠═════════════════════════════
\33[0;34m║\33[0;31m𝗠𝗢𝗢𝗡:\33[0;32m{kal:%B} \33[0;31m𝗗𝗔𝗬:\33[0;32m{kal:%A}\33[0;31m 𝗧𝗚𝗟:\33[0;32m{kal:%d}
\33[0;34m╠══════════════════════════════
\33[0;34m║\33[0;31m[1]:\33[0;32m𝗧𝗢𝗣 𝗨𝗣 𝗨𝗕 𝗕𝗨𝗦𝗦𝗜𝗗
\33[0;34m║\33[0;31m[2]:\33[0;32m𝗛𝗔𝗖𝗞 𝗗𝗨𝗜𝗧 𝟭𝗝𝗧
\33[0;34m║\33[0;31m[3]:\33[0;32m𝗡𝗢𝗠𝗢𝗥 𝗔𝗗𝗠𝗜𝗡
\33[0;34m║\33[0;31m[4]:\33[0;32m𝗘𝗫𝗜𝗧
\33[0;34m╠══════════════════════════════
""")

contoh = input ("𝗣𝗜𝗟𝗜𝗛 𝗧𝗢𝗗::=>")
if contoh =="1":
   os.system("xdg-open  https://m.youtube.com/channel/UClwzxSe9PHPlaldtU0O2Qsw?feature=applinks")
   auth = input("𝗬𝗢𝗨 𝗧𝗢𝗞𝗘𝗡::")
elif contoh =="2":
   os.system("xdg-open  https://baguzae.github.io/")
   ketik("\33[0;32m𝗛𝗔𝗖𝗞 𝗨𝗔𝗡𝗚 𝗧𝗔𝗡𝗣𝗔 𝗕𝗘𝗥𝗞𝗨𝗥𝗔𝗡𝗚")
   auth = input("𝗧𝗢𝗞𝗘𝗡::")
elif contoh =="3":
     os.system("xdg-open  https://wa.me/6285732972016")
elif contoh =="4":    
     sys.exit()


record = [{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'BKL'], 'activityRewards': None}, 'Value': 40},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'BKL'], 'activityRewards': None}, 'Value': 18},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 50},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 13},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'BKL'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'BKL', 'routePassed': ['BKL', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'CBN'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SMG'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'P_Merak'], 'activityRewards': None}, 'Value': 5}, {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'JKT'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SMG'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SBY'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'BKL'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'P_Merak'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SMG'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PLB', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 55},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 11},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'JKT'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'PLB'], 'activityRewards': None}, 'Value': 50},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'LPG'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'JMB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JMB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'PLB'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'LPG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'BKL'], 'activityRewards': None}, 'Value': 1},{"Key":{"sourceCity":"PBR","destinationCity":"BKT","routePassed":["BKT","PBR"],"activityRewards":None},"Value":50},{"Key":{"sourceCity":"PBR","destinationCity":"PDG","routePassed":["PDG","BKT","PBR"],"activityRewards":None},"Value":9},{"Key":{"sourceCity":"BKT","destinationCity":"PDG","routePassed":["PDG","BKT"],"activityRewards":None},"Value":50},]                                            
headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '223','Host': '4ae9.playfabapi.com'}
def create_mission():
	game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			return None
		elif parser['code'] == 200:
			data = parser['data']
			if "apiError" in str(data):
				return None
			else:
				carrer = data['FunctionResult']['careerSession']
				return carrer
	else:
		return None

def skip_mission(token):
	data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
				gugun = backend_data['MemoryConsumedBytes']
				print(f"{yellow}𝐒𝐔𝐂𝐂𝐄𝐒 𝐀𝐃𝐃 1Jt ->{green} $.{logs}")
				print(f"{yellow}𝐌𝐞𝐦𝐨𝐫𝐲𝐂𝐨𝐧𝐬𝐮𝐦𝐞𝐝𝐁𝐲𝐭𝐞𝐬 ->{green} :{gugun}")
				chat = backend_data['Logs']
				uang= chat[len(chat)-1]['Message'].split()[5]
				print(f"{yellow}𝗧𝗢𝗧𝗔𝗟 𝗨𝗔𝗡𝗚 ANDA ->{green} $.{uang}")
				scs = parser['status']
				print(f"{yellow}𝗦𝘁𝗮𝘁𝘂𝘀: ->{green}{scs}")

def pass_mission():
	carrer = create_mission()
	if carrer != None:	
		token = carrer['token']
		skip_mission(token)
		



headers['X-Authorization'] = auth

while True:
 pass_mission()
 
