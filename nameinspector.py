import random
import time 
import requests


#class for defind cheker
class checker:
    def __init__(self) -> None:
        pass
    
    def instacheker(self, characters):
       # this function go to instagram and check if the user it is available 
        if characters == 5:
            while True:
                user = ''
                for character in random.choices('azertyuiopqsdfghjklmwxcvbn1234567890_.',k=5):
                    user = user + character
            
                response = requests.get(f'https://instagram.com/{user}/')
                if (response.status_code == 200):
                    print(f' {user} : is not available in instagram')
                elif (response.status_code == 404):
                    print(f' {user} : is available in instagram' )   
                    break 
                else :
                    print('blocked from instagram wait 2 minuts')
                    time.sleep(120)
        elif characters == 6:
            while True:
                user = ''
                for character in random.choices('azertyuiopqsdfghjklmwxcvbn1234567890_.',k=6):
                    user = user + character
            
                response = requests.get(f'https://instagram.com/{user}/')
                if (response.status_code == 200):
                    print(f' {user} : is not available in instagram')
                elif (response.status_code == 404):
                    print(f' {user} : is available in instagram' )   
                    break 
                else :
                    print('blocked from instagram wait 2 minuts')
                    time.sleep(120) 
        
                        
    #tik tok username cheker                           
    def tikcheker (self, charctesrs):
        if charctesrs == 4:
            while True:
                user = ''
                for character in random.choices('azertyuiopqsdfghjklmwxcvbn1234567890_.',k=4):
                    user = user + character
            
                response = requests.get(f'https://tiktok.com/@{user}/')
                if (response.status_code == 200):
                    print(f' {user} : in not available in tiktok')
                elif (response.status_code == 404):
                    print(f'the {user} : is available in tiktok')   
                    break 
                else :
                    print('blocked from tiktok wait 2 minuts')
                    time.sleep(120)    
        elif charctesrs == 5:
             while True:
                user = ''
                for character in random.choices('azertyuiopqsdfghjklmwxcvbn1234567890_.',k=5):
                    user = user + character
            
                response = requests.get(f'https://tiktok.com/@{user}/')
                if (response.status_code == 200):
                    print(f' {user} : in not available in tiktok')
                elif (response.status_code == 404):
                    print(f'the {user} : is available in tiktok')   
                    break 
                else :
                    print('blocked from tiktok wait 2 minuts')
         
                    time.sleep(120)    
        elif charctesrs == 6:
             while True:
                user = ''
                for character in random.choices('azertyuiopqsdfghjklmwxcvbn1234567890_.',k=6):
                    user = user + character
            
                response = requests.get(f'https://tiktok.com/@{user}/')
                if (response.status_code == 200):
                    print(f' {user} : in not available in tiktok')
                elif (response.status_code == 404):
                    print(f'the {user} : is available in tiktok')   
                    break 
                else :
                    print('blocked from tiktok wait 2 minuts')
                    time.sleep(120)                
    def xcheker(self):
        while True:
            user = ''
            for character in random.choices('azertyuiopqsdfghjklmwxcvbn1234567890._', k=5):
                user = user + character

            response = requests.get(f'https://x.com/{user}/')
            if (response.status_code == 200):
                    print(f' {user} : in not available in X')
            elif (response.status_code == 404):
                    print(f'the {user} : is available in X')   
                    break     




    def generator(self):
        generated = ''
        for c in random.choices('azertyuiopqsdfghjklmwxcvbn1234567890_.',k=6):
            generated = generated + c
               
        print(generated)  

        
    
def main():
    title = """
                              _                           _             
 _ __   __ _ _ __ ___   ___  (_)_ __  ___ _ __   ___  ___| |_ ___  _ __ 
| '_ \ / _` | '_ ` _ \ / _ \ | | '_ \/ __| '_ \ / _ \/ __| __/ _ \| '__|
| | | | (_| | | | | | |  __/ | | | | \__ \ |_) |  __/ (__| || (_) | |   
|_| |_|\__,_|_| |_| |_|\___| |_|_| |_|___/ .__/ \___|\___|\__\___/|_|   
                                         |_|                            
""" 
    print(title)      
    ch = checker()
    
    # maininput = input('[1]- instagram checker\n[2]- tiktok checker\n[3]- twitter checker \n[4]- generate username(6 characters)\n[5]- about\n\n')
    try : 
        maininput = input('[1]- instagram checker\n[2]- tiktok checker\n[3]- generate username \n[4]- check a usernam\n\n')
        if int(maininput) == 1:
                characters = input('choose how many characters you want to inspect\n\n[5]- 5 characters username\n[6]- 6 characters username \n\n ')
                if characters == '5':
                    ch.instacheker(characters=5)
                elif characters == '6':
                    ch.instacheker(characters=6)    
                else :
                    print('please a valid number (5 or 6)')    
        elif int(maininput) == 2:
                
                character = input('Choose how many characters you want to inspect\n\n[4]- 4 characters username (rare)\n[5]- 5 characters username\n[6]- 6 characters username\n\n')
                character = int(character)
                if character == 4 or character == 5 or character == 6:
                    ch.tikcheker(charctesrs=character)
                else:
                    print('Please enter a valid number (4, 5, or 6)')    
        elif int(maininput) == 3:
                print('there is only check for 5 characters username')
                ch.xcheker()   
        elif int(maininput) == 4:
                ch.generator()    
        elif int(maininput) == 5:
                print('that tool is devloped and publicated by https://t.me/NS8_b')    
        else :
                print('thats not an option')    
    except: print('ERROR : something went wrong')


if __name__== '__main__':
    
    main()        
       