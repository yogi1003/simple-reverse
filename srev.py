import requests
import socket

banner = """
  _____ _____            
 / ____|  __ \           
| (___ | |__) |_____   __
 \___ \|  _  // _ \ \ / /
 ____) | | \ \  __/\ V / 
|_____/|_|  \_\___| \_/  

Coded by @yogi1003
https://github.com/yogi1003

Reference: https://github.com/justakazh
"""
print(banner)
open("result.txt", "a")
def main(web):
	try:
		for line in web:
			get_site = line.replace("https://","").replace("http://","").replace("/","").strip()
			try:
				site = 'http://api.hackertarget.com/reverseiplookup/?q='+get_site
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
				result = requests.get(site, headers=headers)
				de = result.content.decode()
				lines_seen = set()
				open("result.txt", "a").write(de+"\n")
				with open("result", "r+") as f:
					d = f.readlines()
					f.seek(0)
					for i in d:
						if i not in lines_seen:
							f.write(i)
							lines_seen.add(i)
					f.truncate()
					
			except:
				pass
	except:
		pass

lisweb = open(input("list: "), "r").readlines()
main(lisweb)