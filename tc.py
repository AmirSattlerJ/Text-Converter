import platform
from os import system
from text_converter import text_converter
from colorama import ( 
    init, 
    Fore, 
    Style, 
)
init()
with open('banner1.txt') as banner: 
    x = banner.read()
plat_form = input(f'{Fore.GREEN}{x}{Style.RESET_ALL}')
w = '''
What you want?
    [1]Translate
    [2]text-to-speech
    Enter Number:'''
if plat_form == '1':
    system('clear')
    work = input(f'{Fore.CYAN}{w}{Style.RESET_ALL}')
    txt = input(f'{Fore.CYAN}Write Your text: ')
    worker = text_converter(txt)
    if work == '1':
        target_lang,file_name  = input(f"{Style.RESET_ALL}Enter the language code: "), input("file name? ")
        worker.translater_text(target_language=target_lang, output_file=file_name)
    elif work == '2':
        target_lang, file_name, slow = input(f'{Style.RESET_ALL}Enter target language: '), input("file name? "), input('slow? Y/N')
        if slow.lower() == 'yes' or 'y' or 'yea' or 'yeap':
            worker.android_tts(lang=target_lang, output_file=file_name, slow=True)
        elif slow.lower() == 'n' or 'no' or 'not':
            worker.android_tts(lang=target_lang, output_file=file_name, slow=False)
        else:
            exit()
    else:
        print(f'{Fore.RED}1 or 2{Style.RESET_ALL}')
        exit()
elif plat_form == '2':
    if platform.system() == 'Linux':
        system('clear')
        work = input(f'{Fore.CYAN}{w}{Style.RESET_ALL}')
        txt = input(f'{Fore.CYAN}Write Your text: ')
        worker = text_converter(txt)
        if work == '1':
            target_lang,file_name  = input(f"{Style.RESET_ALL}Enter the language code(default `en`): "), input("file name? ")
            worker.translater_text(target_language=target_lang, output_file=file_name)
        elif work == '2': 
            rate, volume, voice, file_name = input(f'{Style.RESET_ALL}Enter rate voice: (1..200) '), input("volume? (0..1.0)"), input('voice? (male or female)'), input("file name? (with .mp3)")
            worker.PC_tts(rate=rate, volume=volume, voice=voice, output_file=file_name)
        else:
            print(f'{Fore.RED}1 or 2{Style.RESET_ALL}')
            exit()
    elif platform.system() == 'Windows':
        system('cls')
        work = input(f'{Fore.CYAN}{w}{Style.RESET_ALL}')
        txt = input(f'{Fore.CYAN}Write Your text: ')
        worker = text_converter(txt)
        if work == '1':
            target_lang,file_name  = input(f"{Style.RESET_ALL}Enter the language code(default `en`): "), input("file name? ")
            worker.translater_text(target_language=target_lang, output_file=file_name)
        elif work == '2': 
            rate, volume, voice, file_name = input(f'{Style.RESET_ALL}Enter rate voice: (1..200) '), input("volume? (0..1.0)"), input('voice? (male or female)'), input("file name? (with .mp3)")
            worker.PC_tts(rate=rate, volume=volume, voice=voice, output_file=file_name)
        else:
            print(f'{Fore.RED}1 or 2{Style.RESET_ALL}')
            exit()
    else:
        print(f'{Fore.RED}sorry{Style.RESET_ALL}')
        exit()
else:
    print(f'{Fore.RED}sorry 1 or 2{Style.RESET_ALL}')
    exit()
