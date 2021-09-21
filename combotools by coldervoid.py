import os
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
    print('')
    print('[SELECT COMBO FILE]')
    print('')

    while True:
        combo_filename = None

        try:
            combo_filename = easygui.fileopenbox(title='Select combofile', filetypes='*.txt', multiple=False, )
        except:
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
                closing(message="Goodbye!", sleep_time=3)

    sort(combo_filename)  # sortowanie email przez 'gmail.', 'hotmail.', 'yahoo.', 'aol.', 'live.', 'outlook.', 'msn.'


def sort(combo_filename):
    banned_emails = ['gmail.', 'hotmail.', 'yahoo.', 'aol.', 'live.', 'outlook.', 'msn.', '###NULL###']
    sorted_table_wo_banned = []
    semi_loaded_combo = []
    dumped_email = []
    domain_table = []
    split_symbol = ':'
    null_email = 0
    null_pass = 0
    count = 0
    line_counter = 0
    local_line_counter = 0
    end_of_file_check = True
    new_line = bytes([0x0A])

    file = open(combo_filename, encoding='utf-8')
    sorted_combolist = open(str(datetime.date(datetime.now())) + ' [SORTED COMBO].txt', 'wb')

    dumped_combo = open('dumped.txt', 'wb')

    domain_list = open('domains.txt', 'wb')

    # lines = file.read().splitlines()

    while end_of_file_check:

        print('hello')

        while True:
            semi_loaded_combo.append(file.readline())
            local_line_counter += 1
            if local_line_counter > 999:
                local_line_counter += 1
                break
            elif 1000 == local_line_counter < 2000:
                break

        count = 0
        print('apiwgnoiawng')
        count_sorted = 0
        for line in tqdm(semi_loaded_combo, desc="[COMBOS LEFT]", unit=' lines',
                         bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):
            count += 1
            count_sorted += 1

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
                    sorted_combolist.write(o_combo.encode('utf-8', 'ignore') + new_line)
                count_sorted = 0  # reset licznika
                sorted_table_wo_banned = []  # czyszczenie tabeli

        # semi_loaded_combo = []  # wyczyszczenie tabeli

        print(line_counter)
        print(local_line_counter)

        if line_counter == len(file.readlines()):
            end_of_file_check = False

    #
    # END OF WHILE LOOP
    #

    for o_combo in dumped_email:
        dumped_combo.write(o_combo.encode('utf-8', 'ignore') + new_line)

    for o_domain_list in domain_table:
        domain_list.write(o_domain_list.encode('utf-8', 'ignore') + new_line)

    print('')
    print('[EMAIL SORTED]: ' + str(count))
    print('[COMBO ERRORS]: ' + str(null_email + null_pass))
    print('')

    input('Done! Press any key...')


if __name__ == '__main__':
    __title__ = 'combotools by COLDERVOID'
    __version__ = '0.2.5'

    os.system("title " + __title__)

    logo()  # wyswietl logo
    menu()  # menu wyboru
