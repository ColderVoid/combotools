import os
import pathlib
import sys
from datetime import datetime
from tqdm import tqdm
from colorama import Fore
import time
import easygui


def closing(message, sleep_time):
    print('')
    print(message)
    print('')

    time.sleep(sleep_time)
    sys.exit()


def logo():
    os.system('cls')
    print('')
    print(' __   __        __   ___  __        ___ ___       __   __       ')
    print('/  ` /  \ |    |  \ |__  |__) |\ | |__   |  |  | /  \ |__) |__/ ' + '  ' + 'combotools')
    print('\__, \__/ |___ |__/ |___ |  \ | \| |___  |  |/\| \__/ |  \ |  \ ' + '  ' + 'version: ' + __version__)
    print('')
    print('')


def menu():
    print(Fore.RED + '[EXIT] -> 0')
    print(Fore.CYAN + '[COMBO SORTER] -> 1')
    print(Fore.CYAN + '[DOMAINS to YOPMAIL] -> 2')
    print(Fore.CYAN + '[EMAIL:PASS to USER:PASS] -> 3')
    print(Fore.CYAN + '[COMBO STATS] -> 4')
    print('')
    selection = input(Fore.LIGHTCYAN_EX + '[OPTION]: ')
    print(Fore.RESET)
    return selection


def file_select():
    print('')
    print('[SELECT COMBO FILE]')
    print('')

    while True:
        combo_filename = None

        try:
            combo_filename = easygui.fileopenbox(title='Select combofile', filetypes='*.txt', multiple=False)
        except Exception as e:
            print("Error.. Try again")

        if combo_filename is not None:
            print('')
            print('[SELECTED COMBO FILE] -->  ' + combo_filename)
            print('')
            print('')
            break
        else:
            logo()

            print('')
            print("[CANCELED]")
            option = input('[Try again? y/n]: ')

            if option.lower() == 'y':
                continue

            else:
                closing(message="Goodbye!", sleep_time=2)

    return combo_filename  # sortowanie email przez 'gmail.', 'hotmail.', 'yahoo.', 'aol.', 'live.', 'outlook.', 'msn.'


def splitter(line):
    null_email = 0
    null_pass = 0

    line = line.replace(';', ':')
    table = line.split(':')

    email = table[0]
    email = email.lower()

    try:
        password = table[1]
    except IndexError:
        null_pass += 1
        password = 'null'

    # split domain
    d_split = email.split('@')

    try:
        domain = d_split[1]

    except IndexError:
        null_email += 1
        domain = '###NULL###'

    return email, password, domain, d_split


def check_dir():
    data_folder_name = 'DATA'
    time_folder_name = datetime.now().strftime("%d-%m-%Y %H-%M")
    data_folder = pathlib.Path(data_folder_name)
    if not data_folder.exists():
        os.mkdir('DATA')

    time_folder = pathlib.Path('DATA/' + time_folder_name)
    if not time_folder.exists():
        os.mkdir('DATA/' + datetime.now().strftime("%d-%m-%Y %H-%M"))

    return data_folder, time_folder, data_folder_name, time_folder_name


def checkbox(question):
    title = "COMBOEDITOR"
    listOfOptions = ['gmail.', 'hotmail.', 'yahoo.', 'aol.', 'live.', 'outlook.', 'msn.']

    choice = easygui.multchoicebox(question, title, listOfOptions)

    choice.append('###NULL###')

    return choice


def sort():
    banned_emails = checkbox(question='Choose domains to sort: ')
    sorted_table_wo_banned = []
    dumped_email = []
    domain_table = []
    split_symbol = ':'
    null_email = 0
    null_pass = 0
    count = 0

    data_folder, time_folder, data_folder_name, time_folder_name = check_dir()

    file = open(file_select(), encoding='utf-8')
    sorted_combolist = open(data_folder_name + '/' + time_folder_name + '/COMBOTOOLS.txt', 'wb')
    dumped_combo = open(data_folder_name + '/' + time_folder_name + '/dumped.txt', 'wb')
    domain_list = open(data_folder_name + '/' + time_folder_name + '/domains.txt', 'wb')

    count_sorted = 0
    for line in tqdm(file.readlines(), desc="[COMBOS LEFT]", unit=' lines',
                     bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):
        count += 1
        count_sorted += 1

        email, password, domain, d_split = splitter(line)

        check_ban = 0

        for single_domain in banned_emails:
            if single_domain in domain:
                check_ban = 0
                break

            else:
                check_ban = 1

        if check_ban == 1:
            sorted_table_wo_banned.append(email + split_symbol + password)

        else:
            dumped_email.append(email + split_symbol + password)

        if domain not in domain_table:
            domain_table.append(domain)

            # zapisywanie co 100k do pliku
        if count_sorted > 100000:
            for o_combo in sorted_table_wo_banned:
                sorted_combolist.write(o_combo.encode('utf-8', 'ignore'))
            count_sorted = 0  # reset licznika
            sorted_table_wo_banned = []  # czyszczenie tabeli

    for o_combo in dumped_email:
        dumped_combo.write(o_combo.encode('utf-8', 'ignore'))

    for o_domain_list in domain_table:
        domain_list.write(o_domain_list.encode('utf-8', 'ignore'))

    for combo_line in sorted_table_wo_banned:
        sorted_combolist.write(combo_line.encode('utf-8', 'ignore'))

    sorted_combolist.close()

    print('')
    print('[EMAIL SORTED]: ' + str(count))
    print('[COMBO ERRORS]: ' + str(null_email + null_pass))
    print('')

    input('Done! Press any key...')


def domains_to_yopmail():
    complete = []
    split_symbol = ':'
    count = 0

    data_folder, time_folder, data_folder_name, time_folder_name = check_dir()

    yopmail_domains = open(data_folder_name + '/' + time_folder_name + '/domains to yopmain [COMBOEDITOR].txt', 'wb')
    file = open(file_select(), encoding='utf-8')

    for line in tqdm(file.readlines(), desc="[COMBOS LEFT]", unit=' lines',
                     bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):

        count += 1
        check_error = 0

        email, password, domain, d_split = splitter(line)

        try:
            d_split[1] = 'yopmail.fr'
        except:
            check_error = 1

        try:
            if check_error == 0:
                email = d_split[0] + '@' + d_split[1]
        except:
            check_error = 1

        if check_error == 0:
            complete.append(email + split_symbol + password)

        if count >= 100000:
            for combo_line in complete:
                yopmail_domains.write(combo_line.encode('utf-8', 'ignore'))
            count = 0
            complete = []

    if True:
        for combo_line in complete:
            yopmail_domains.write(combo_line.encode('utf-8', 'ignore'))

    yopmail_domains.close()

    input('Done! Press any key...')


def email_to_user():
    split_symbol = ':'
    count = 0
    complete = []
    valid = ''

    data_folder, time_folder, data_folder_name, time_folder_name = check_dir()

    user_pass = open(data_folder_name + '/' + time_folder_name + '/email to user [COMBOEDITOR].txt', 'wb')
    file = open(file_select(), encoding='utf-8')

    for line in tqdm(file.readlines(), desc="[COMBOS LEFT]", unit=' lines',
                     bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):
        count += 1
        check_error = 0

        email, password, domain, d_split = splitter(line)

        try:
            valid = d_split[0] + split_symbol + password
        except:
            check_error = 1
            print('valid error')

        if check_error == 0:
            complete.append(valid)

        if count >= 100000:
            for combo_line in complete:
                user_pass.write(combo_line.encode('utf-8', 'ignore'))
            count = 0
            complete = []

    if True:
        for combo_line in complete:
            user_pass.write(combo_line.encode('utf-8', 'ignore'))

    user_pass.close()


def stats():
    print("stats")


if __name__ == '__main__':
    __title__ = 'combotools by COLDERVOID'
    __version__ = '0.4.2'

    os.system("title " + __title__)

    logo()  # wyswietl logo

    selector = menu()

    if selector == '1':
        sort()

    elif selector == '2':
        domains_to_yopmail()

    elif selector == '3':
        email_to_user()

    elif selector == '4':
        stats()

    else:
        closing(message="Goodbye!", sleep_time=2)
