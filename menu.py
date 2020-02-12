from colorama import Fore

def menuArt():
    print(r"""{0}

     /\  ___\   /\  __ \   /\  ___\   /\ \   /\  __ \   /\ \          /\  == \   
     \ \___  \  \ \ \/\ \  \ \ \____  \ \ \  \ \  __ \  \ \ \____     \ \  __<   
      \/\_____\  \ \_____\  \ \_____\  \ \_\  \ \_\ \_\  \ \_____\     \ \_\ \_\ 
       \/_____/   \/_____/   \/_____/   \/_/   \/_/\/_/   \/_____/      \/_/ /_/


    """.format(Fore.LIGHTGREEN_EX))

def menuArtScull():
    print("{0}[1] {1}Kişinin Sosyal Medya Hesaplarını Ara{2}        ___ (~ )( ~)".format(Fore.YELLOW, Fore.BLUE, Fore.RED))
    print(r"{0}[2] {1}Uygulama Hakkın da Bilgi Al{2}                /   \_\ \/ /".format(Fore.YELLOW, Fore.BLUE, Fore.RED))
    print(r"{0}[99] {1}Exit                      {2}               |   D_ ]\ \/ Developer: {3}pr0xy12".format(Fore.YELLOW, Fore.BLUE, Fore.RED, Fore.YELLOW))
    print(r"""{0}                                              |   D _]/\ \ Git-Hub: {1}www.github.com/pr0xy12""".format(Fore.RED, Fore.YELLOW))
    print(r""" {0}                                              \___/ / /\ \ """.format(Fore.RED))
    print(r"                                                    (_ )( _){0}".format(Fore.RESET))
        
menuArt()
menuArtScull()


