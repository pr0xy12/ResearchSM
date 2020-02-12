from os import name
from os import system

############################################
###      Research To Social Media        ###
############################################
###  Developer: Pr0xy12 Version: 1.0.0   ###
############################################



_APPNAME_ = "Research Social Media"
_OS_ = "Linux and Windows"
_VERSION_ = "1.0.0"

try:
    from colorama import Fore
    from requests import get
    from requests import status_codes
    from threading import Thread
except:
    print("{0}[!]{1} Modül eksikliği vardır, lütfen{2} 'pip3 install -r requirements.txt'{3} ile gerekli modülleri kurunuz.".format(Fore.RED, Fore.RESET, Fore.RED, Fore.RESET))

try:
    import colorama
    import requests
    import threading
except:
    print("{0}[!]{1} Modül eksikliği vardır, lütfen{2} 'pip3 install -r requirements.txt'{3} ile gerekli modülleri kurunuz.".format(Fore.RED, Fore.RESET, Fore.RED, Fore.RESET))

def ClearMenu():
        if name == "win32" or name == "win64":
            system("cls")
        else:
            system("clear")
ClearMenu()
from menu import menuArt
from menu import menuArtScull

class ResearchSM(object):

    def __init__(self, menuArt, menuArtScull):
        self.menuArt = menuArt
        self.menuArt = menuArtScull
    
    def ResearchInstagram(self, username):
        self.username = username
        link = "https://www.instagram.com/"
        accept = requests.get(link+username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET + "Instagram hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}Instagram hesabı bulunamadı.".format(Fore.RED, Fore.RESET))

    def ResearchTwitter(self, username):
        self.username = username
        link = "https://www.twitter.com/"
        accept = requests.get(link + username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET +  "Twitter hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}Twitter hesabı bulunamadı.".format(Fore.RED, Fore.RESET))
    
    def ResearchPinterest(self, username):
        self.username = username
        link = "https://tr.pinterest.com/"
        accept = requests.get(link + username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET +  "Pinterest hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}Pinterest hesabı bulunamadı.".format(Fore.RED, Fore.RESET))

    def ResearchTwitch(self, username):
        self.username = username
        link = "https://www.twitch.tv/"
        accept = requests.get(link + username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET +  "Twitch hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}Twitch hesabı bulunamadı.".format(Fore.RED, Fore.RESET))

    def ResearchSteam(self, username):
        self.username = username
        link = "https://steamcommunity.com/id/"
        accept = requests.get(link + username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET +  "Steam hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}Steam hesabı bulunamadı.".format(Fore.RED, Fore.RESET))

    def ResearchFacebook(self, username):
        self.username = username
        link = "https://www.facebook.com/"
        accept = requests.get(link + username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET +  "Facebook hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}Facebook hesabı bulunamadı.".format(Fore.RED, Fore.RESET))

    def ResearchTumblr(self, username):
        self.username = username
        link = "https://www.tumblr.com/blog/"
        accept = requests.get(link + username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET +  "Tumblr hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}Tumblr hesabı bulunamadı.".format(Fore.RED, Fore.RESET))

    def ResearchReddit(self, username):
        self.username = username
        link = "https://www.reddit.com/user/"
        accept = requests.get(link + username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET +  "Reddit hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}Reddit hesabı bulunamadı.".format(Fore.RED, Fore.RESET))

    def ResearchYoutube(self, username):
        self.username = username
        link = "https://www.youtube.com/channel"
        accept = requests.get(link + username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET +  "Youtube hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}Youtube hesabı bulunamadı.".format(Fore.RED, Fore.RESET))

    def ResearchDailymotion(self, username):
        self.username = username
        link = "https://www.dailymotion.com/channel"
        accept = requests.get(link + username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET +  "Dailymotion hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}Dailymotion hesabı bulunamadı.".format(Fore.RED, Fore.RESET))

    def ResearchLinkedIn(self, username):
        self.username = username
        link = "https://www.linkedin.com/in"
        accept = requests.get(link + username)
        if accept.status_code == 200:
            print(Fore.GREEN+ "[200] " + Fore.RESET +  "LinkedIn hesabı bulundu > "+ Fore.LIGHTGREEN_EX + f"{link+username}")
        else:
            print("{0}[404] {1}LinkedIn hesabı bulunamadı.".format(Fore.RED, Fore.RESET))

if __name__ == "__main__":
    s = ResearchSM(menuArt, menuArtScull)
    yourchoice = input("{0}Seçiminiz: {1}".format(Fore.MAGENTA, Fore.RESET))
    if yourchoice.isdigit():
        yourchoice = int(yourchoice)
        if yourchoice == 1:
            username = input("{0}[?] {1}Kişinin kullanıcı adını giriniz: ".format(Fore.YELLOW, Fore.RESET))
            Thread(target=s.ResearchInstagram(username), args=username,).start()
            Thread(target=s.ResearchTwitter(username), args=username,).start()
            Thread(target=s.ResearchPinterest(username), args=username,).start()
            Thread(target=s.ResearchTwitch(username), args=username,).start()
            Thread(target=s.ResearchSteam(username), args=username,).start()
            Thread(target=s.ResearchFacebook(username), args=username,).start()
            Thread(target=s.ResearchTumblr(username), args=username,).start()
            Thread(target=s.ResearchReddit(username), args=username,).start()
            Thread(target=s.ResearchYoutube(username), args=username,).start()
            Thread(target=s.ResearchDailymotion(username), args=username,).start()
            Thread(target=s.ResearchLinkedIn(username), args=username,).start()
        elif yourchoice == 2:
            print("{0}[*] {1}Girdiğiniz kullanıcı adını popüler sosyal medya ve diğer platformlarda aramaktadır.".format(Fore.YELLOW, Fore.RESET))
        elif yourchoice == 3:
            print("{0}[!] {1}Çıkış yapılıyor, tekrar görüşmek üzere :)".format(Fore.RED, Fore.RESET))
        