#Made by worm#0001
#worm6 on github
#Enjoy!



import time, ctypes
import asyncio, aiohttp
import random
import schedule

cookie = open('cookie.txt' , 'r').readline().strip() #opens your cookie and stores it

delay = int(input("How many seconds delay? ")) #determines how long between color changes


success = False
sent_requests = 0
i = 0



#list of all possible BrickColorIds
colors = [361,192,217,153,359,352,5,101,1007,1014,38,18,125,1030,133,106,105,1017,24,334,226,141,1021,28,37,310,317,119,1011,1012,1010,23,305,102,45,107,1018,1027,1019,1013,11,1024,104,1023,321,1015,1031,1006,1026,21,1004,1032,1016,330,9,1025,364,351,1008,29,1022,151,135,1020,1028,1009,1029,1003,26,199,194,1002,208,1,1001]
    
#sends the request to change body colors
async def thread():
    global success, sent_requests, i
    async with aiohttp.ClientSession() as session:
        while success == False:
            async with session.post('https://avatar.roblox.com/v1/avatar/set-body-colors', cookies=cookies, json={"headColorId":random.choice(colors),"torsoColorId":random.choice(colors),"rightArmColorId":random.choice(colors),"leftArmColorId":random.choice(colors),"rightLegColorId":random.choice(colors),"leftLegColorId":random.choice(colors)}, headers=headers, timeout=5) as resp:
                    r = await resp.text()
                    #determines what to output based on response
                    if 'Token' in r:
                        print("Token expired.. Wait one second")
                        await main()
                    if 'Authorization' in r:
                        print("Invalid Cookie! Did you log out?")
                        quit
                    else:
                        i += 1
                        sent_requests += 1
                        print("Success! "+str(i))
                    time.sleep(delay)
    




#checks if the cookie entered is valid
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.roblox.com/mobileapi/userinfo', cookies=cookies, timeout=5) as resp:
            r = str(resp.url)
        if 'mobileapi/user' not in r:
            print('Invalid Cookie.')
            exit()



        #gets the X-CSRF-TOKEN
        async with session.post('https://auth.roblox.com/v2/login', cookies=cookies, timeout=5) as resp:
            r = resp.headers
        xcrsf = r['X-CSRF-TOKEN']



    #just let the token sleep
    start=time.time()
    await asyncio.sleep(3)
    headers['X-CSRF-TOKEN'] =  xcrsf





#main
headers = {'X-CRSF-TOKEN': ''}
cookies = {'.ROBLOSECURITY': cookie}


asyncio.run(main())
asyncio.run(thread())

print('Finished.')
