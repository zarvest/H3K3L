#!usr/bin/python2.7
# coding=utf-8

import requests

class Config:
	def loadCookie(self):
		try:
			file = open('log/cookies.log','r')
			cookie = file.read()
			file.close()
			return cookie.strip()
		except IOError:
			return False

	def banner(self):
		return '''\n

\033[1;91m ┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈┈┈☞☞☞☞☞☞\033[1;92m☜☜☜☜☜┈┈┈┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈
\033[1;91m ┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈┈┈☞☞☞☞☞☞\033[1;92m☜☜☜☜☜┈┈┈┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈
\033[1;91m ┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈┈┈☞☞☞☞☞☞\033[1;92m☜☜☜☜☜┈┈┈┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈
\033[1;91m ┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈┈\033[1;93m𝐃𝐀𝐑𝐊 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊\033[1;92m┈┈┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈
\033[1;91m ┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈┈┈☞☞☞☞☞☞\033[1;92m☜☜☜☜☜┈┈┈┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈
\033[1;91m ┈┈┈╱▔▔▔▔┊┊┊┊▔▔▔▔╲┈┈┈┈┈┈☞☞☞☞☞☞\033[1;92m☜☜☜☜☜┈┈┈┈┈┈┈╱▔▔▔▔┊┊┊┊▔▔▔▔╲┈┈┈
\033[1;91m.....................\033[1;93m𝐌𝐀𝐒𝐋𝐀𝐊𝐇𝐔𝐃𝐈𝐍 𝐋𝐀𝐓𝐈𝐅\033[1;92m......................
\033[1;91m..................\033[1;93m✬𝐀𝐍𝐎𝐍𝐘𝐌𝐎𝐔𝐒 𝐁𝐄𝐍𝐃𝐀 𝐉𝐀𝐘𝐀✬\033[1;92m....................
\033[1;94m────────────────────────────────────────────────────────────────
\033[1;91m             𝐓𝐑𝐈𝐂𝐊𝐄𝐑 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 \033[1;92m 𝐋𝐀𝐌𝐏𝐔𝐍𝐆 𝐒𝐄𝐋𝐀𝐓𝐀𝐍
\033[1;94m────────────────────────────────────────────────────────────────
\033[1;91m$$\      $$\ $$\   $$\ $$\    $$$$$$$$\ $$$$$$\ 
\033[1;91m$$$\    $$$ |$$ |  $$ |$$ |   \__$$  __|\_$$  _|
\033[1;91m$$$$\  $$$$ |$$ |  $$ |$$ |      $$ |     $$ |  
\033[1;91m$$\$$\$$ $$ |$$ |  $$ |$$ |      $$ |     $$ |  
\033[1;97m$$ \$$$  $$ |$$ |  $$ |$$ |      $$ |     $$ |  
\033[1;97m$$ |\$  /$$ |$$ |  $$ |$$ |      $$ |     $$ |  
\033[1;97m$$ | \_/ $$ |\$$$$$$  |$$$$$$$$\ $$ |   $$$$$$\ 
\033[1;97m\__|     \__| \______/ \________|\__|   \______|
                                                

             \033[1;91m $$$$$$\  $$$$$$$\  $$\   $$\  $$$$$$\  $$\   $$\ 
             \033[1;91m$$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\ $$ | $$  |
             \033[1;91m$$ /  \__|$$ |  $$ |$$ |  $$ |$$ /  \__|$$ |$$  / 
             \033[1;91m$$ |      $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  
             \033[1;97m$$ |      $$  __$$< \_____$$ |$$ |      $$  $$<   
             \033[1;97m$$ |  $$\ $$ |  $$ |      $$ |$$ |  $$\ $$ |\$$\  
             \033[1;97m\$$$$$$  |$$ |  $$ |      $$ |\$$$$$$  |$$ | \$$\ 
             \033[1;97m \______/ \__|  \__|      \__| \______/ \__|  \__|
                                                  
                                                                                     
\033[1;91m$$$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
\033[1;91m$$  _____|$$  __$$\ $$  __$$\ $$  _____|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |
\033[1;91m$$ |      $$ /  $$ |$$ /  \__|$$ |      $$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |$$  / 
\033[1;91m$$$$$\    $$$$$$$$ |$$ |      $$$$$\    $$$$$$$\ |$$ |  $$ |$$ |  $$ |$$$$$  /  
\033[1;97m$$  __|   $$  __$$ |$$ |      $$  __|   $$  __$$\ $$ |  $$ |$$ |  $$ |$$  $$<   
\033[1;97m$$ |      $$ |  $$ |$$ |  $$\ $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$$\  
\033[1;97m$$ |      $$ |  $$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  | $$$$$$  | $$$$$$  |$$ | \$$\ 
\033[1;97m\__|      \__|  \__| \______/ \________|\_______/  \______/  \______/ \__|  \__|                                                                                                                                                                                                                                          
\033[1;94m─────────────────────────────────────────────────────────────────────
\033[1;91m𝐒𝐄𝐁𝐄𝐋𝐔𝐌 𝐋𝐎 𝐌𝐔𝐋𝐀𝐈 𝐂𝐑𝐀𝐂𝐊 𝐍𝐘𝐀 𝐋𝐎 𝐌𝐄𝐒𝐓𝐈 \033[1;92m𝐁𝐀𝐂𝐀 𝐁𝐈𝐒𝐌𝐈𝐋𝐋𝐀𝐇 𝐃𝐔𝐋𝐔 𝐁𝐎𝐘 𝐁𝐈𝐀𝐑 𝐇𝐀𝐋𝐀𝐋
\033[1;94m─────────────────────────────────────────────────────────────────────
\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93m𝐀𝐔𝐓𝐇𝐎𝐑 \033[0;91m     : \033[1;96m𝐌𝐚𝐬𝐥𝐚𝐤𝐡𝐮𝐝𝐢𝐧 𝐋𝐚𝐭𝐢𝐟 𝐏𝐮𝐭𝐫𝐚 𝐑𝐚𝐠𝐢𝐞𝐥 𝐁𝐩𝐤. 𝐀.𝐌𝐮𝐳𝐚𝐤𝐢
\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93m𝐆𝐑𝐔𝐏 𝐅𝐁     \033[0;91m: \033[1;96m💜𝐑𝐀𝐓𝐔 𝐄𝐑𝐑𝐎𝐑💜
\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏  \033[0;91m  : \033[1;96m𝟎𝟖𝟗𝟓𝟑𝟐𝟑𝟔𝟎𝟐𝟐𝟕𝟕
\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊    \033[0;91m: \033[1;96m𝐡𝐭𝐭𝐩𝐬://𝐰𝐰𝐰.𝐟𝐚𝐜𝐞𝐛𝐨𝐨𝐤.𝐜𝐨𝐦/𝐌𝐈𝐒𝐓𝐄𝐑.𝐁𝐋𝐀𝐂𝐊.𝟒𝟎𝟒.𝐇𝐀𝐂𝐊𝐄𝐑.𝐓𝐄𝐑𝐌𝐔𝐗.𝐀𝐍𝐎𝐍𝐘𝐌𝐎𝐔𝐒.𝐈𝐍𝐃𝐎𝐍𝐄𝐒𝐈𝐀'''

	def httpRequest(self, url, cookies):
		try:
			return requests.get(url, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestExceptio
			exit('\n\n\033[0;91mKesalahan koneksi, periksa koneksi Anda!!\033[0m')

	def httpRequestPost(self, url, cookies, params):
		try:
			return requests.post(url, data = params, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mKesalahan koneksi, periksa koneksi Anda!!\033[0m')
