#   ______________________
#  /\                     \
# /  \    _________________\
# \   \   \                /
#  \   \   \__________    /
#   \   \   \    /   /   /
#    \   \   \  /   /   /
#     \   \   \/   /   /   Sleep well, and take care.
#      \   \  /   /   /  ~coldervoid
#       \   \/   /   /
#        \      /   /
#         \    /   /
#          \  /   /
#           \/___/

import hashlib
import os
import pathlib
import sys
from datetime import datetime
from tqdm import tqdm
from colorama import Fore
from math import sin, cos
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
    print('/  ` /  \ |    |  \ |__  |__) |\ | |__   |  |  | /  \ |__) |__/ ' + '  ' + __index__)
    print('\__, \__/ |___ |__/ |___ |  \ | \| |___  |  |/\| \__/ |  \ |  \ ' + '  ' + 'version: ' + __version__)
    print('')
    print('')


def menu():
    print(Fore.RED + '[EXIT] -> 0')
    print(Fore.CYAN + '[COMBO SORTER] -> 1')
    print(Fore.CYAN + '[EMAIL:PASS to USER:PASS] -> 2')
    print(Fore.CYAN + '[COMBO STATS] -> 3')
    print(Fore.CYAN + '[COMBO MERGE] -> 4')
    print(Fore.CYAN + '[DOMAIN CHANGE] -> 5')
    print(Fore.CYAN + '[FILE SPLIT] -> 6')
    print(Fore.CYAN + '[DUPLICATE REMOVER] -> 7')
    print(Fore.CYAN + '[DONUT] -> 8')

    if __DEBUG__:
        print(Fore.CYAN + '[DOMAINS to YOPMAIL] -> x')
        print(Fore.CYAN + '[WORDLIST COMBO] -> y')

    print('')

    while True:
        selection = input(Fore.LIGHTCYAN_EX + '[OPTION]: ')

        if len(selection) == 1:
            break

        print('Please enter only one character')
        print('')

    print(Fore.RESET)

    return selection


def file_select(multiple, title):
    if not title:
        title = 'Select combofile'

    print('')
    print('[SELECT COMBO FILE]')
    print('')

    while True:
        combo_filename = None

        try:
            combo_filename = easygui.fileopenbox(title, filetypes='*.txt', multiple=multiple)
        except:
            print("Error.. Try again")

        if combo_filename is not None:
            if not multiple:
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

    return combo_filename


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
    data_folder = pathlib.Path(data_folder_name)
    if not data_folder.exists():
        os.mkdir('DATA')

    time_folder_name = datetime.now().strftime("%d-%m-%Y %H-%M")
    time_folder = pathlib.Path('DATA/' + time_folder_name)
    if not time_folder.exists():
        os.mkdir('DATA/' + datetime.now().strftime("%d-%m-%Y %H-%M"))

    return data_folder, time_folder, data_folder_name, time_folder_name


def checkbox(question, single):
    title = "COMBOTOOLS"
    listOfOptions = ['gmail.', 'hotmail.', 'yahoo.', 'aol.', 'live.', 'outlook.', 'msn.']

    if __DEBUG__:
        listOfOptions.append('yopmail.')

    while True:
        choice = None

        try:
            if single:
                choice = easygui.choicebox(question, title, listOfOptions)

            else:
                choice = easygui.multchoicebox(question, title, listOfOptions)
                choice.append('###NULL###')
        except:
            print("Error.. Try again")

        if choice is not None and single:
            print('[SELECTED DOMAIN] -->  ' + choice)
            print('')
            print('')
            break

        elif choice is not None and not single:
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

    return choice


def inputbox(question):
    title = "COMBOTOOLS"
    dot_symbol = '.'
    at_symbol = '@'

    while True:
        error = 0
        var_check = 0
        var = ''
        choice = easygui.enterbox(question, title)

        if choice is None:
            error = 1

        if choice is not None:
            if at_symbol in choice or choice == '' or dot_symbol not in choice:
                error = 1
                logo()

                if at_symbol in choice and var_check == 0:
                    var = '   @ symbol detected!'
                    var_check = 1

                if choice == '' and var_check == 0:
                    var = '   blank line detected!'
                    var_check = 1

                if dot_symbol not in choice and var_check == 0:
                    var = '   domain does not contain dot!'

                print('[INPUT ERROR]' + var)
                option = input('[Try again? y/n]: ')

                if option.lower() == 'y':
                    continue

                else:
                    closing(message="Goodbye!", sleep_time=2)

        if choice is not None and error == 0:
            print('[TYPED DOMAIN] -->  ' + choice)
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

    return choice


def round_func(prec):
    n_digits = 0
    z_digits = 0
    place = 0

    for digit in str(prec):

        try:
            digit = int(digit)
        except:
            digit = 9

        if digit == 0:
            z_digits += 1
        else:
            n_digits += 1
            if n_digits > 1:
                place = n_digits + z_digits - 1
                break

    return place


def memory_access(file, file_dest):
    try:
        memory_access_a = file.readlines()
    except:
        print(Fore.RED + '[!TOO BIG FILE!]')
        print(Fore.RED + '[SIZE OF FILE]: ' + str(os.path.getsize(file_dest)) + ' bytes')
        print('')
        print(Fore.RED + '[EMERGENCY MODE]')
        print('')
        print(Fore.RED + '[NUMBER OF LINES NOT DETECTED]')
        print(Fore.RESET + '')
        memory_access_a = file

    return memory_access_a


def donut():
    a = 0
    b = 0

    height = 24
    width = 80

    clear = "cls"
    if os.name == "posix":
        clear = "clear"

    os.system(clear)
    while True:
        z = [0 for _ in range(4 * height * width)]
        screen = [' ' for _ in range(height * width)]

        j = 0
        while j < 6.28:
            j += 0.07
            i = 0
            while i < 6.28:
                i += 0.02

                sinA = sin(a)
                cosA = cos(a)
                cosB = cos(b)
                sinB = sin(b)

                sini = sin(i)
                cosi = cos(i)
                cosj = cos(j)
                sinj = sin(j)

                cosj2 = cosj + 2
                mess = 1 / (sini * cosj2 * sinA + sinj * cosA + 5)
                t = sini * cosj2 * cosA - sinj * sinA

                x = int(40 + 30 * mess * (cosi * cosj2 * cosB - t * sinB))
                y = int(11 + 15 * mess * (cosi * cosj2 * sinB + t * cosB))
                o = int(x + width * y)
                N = int(8 * ((
                                     sinj * sinA - sini * cosj * cosA) * cosB - sini * cosj * sinA - sinj * cosA - cosi * cosj * sinB))
                if 0 < y < height and 0 < x < width and z[o] < mess:
                    z[o] = mess
                    screen[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

        os.system(clear)
        for index, char in enumerate(screen):
            if index % width == 0:
                print()
            else:
                print(char, end='')

        a += 0.04
        b += 0.02


def sort():
    banned_emails = checkbox(question='Choose domains to sort: ', single=False)
    sorted_table_wo_banned = []
    dumped_email = []
    domain_table = []
    split_symbol = ':'
    null_email = 0
    null_pass = 0
    count = 0

    data_folder, time_folder, data_folder_name, time_folder_name = check_dir()

    file = open(file_select(multiple=False, title=False), encoding='utf-8')
    sorted_combolist = open(data_folder_name + '/' + time_folder_name + '/single domain [COMBOTOOLS].txt', 'wb')
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

    yopmail_domains = open(data_folder_name + '/' + time_folder_name + '/domains to yopmain [COMBOTOOLS].txt', 'wb')
    file = open(file_select(multiple=False, title=False), encoding='utf-8')

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

    user_pass = open(data_folder_name + '/' + time_folder_name + '/email to user [COMBOTOOLS].txt', 'wb')
    file = open(file_select(multiple=False, title=False), encoding='utf-8')

    for line in tqdm(file.readlines(), desc="[COMBOS LEFT]", unit=' lines',
                     bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):
        count += 1
        check_error = 0

        email, password, domain, d_split = splitter(line)

        try:
            valid = d_split[0] + split_symbol + password
        except:
            check_error = 1

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
    input('Done! Press any key...')


def email_stats():
    count = 0
    domain_dict = {}

    file = open(file_select(multiple=False, title=False), encoding='utf-8')

    for line in tqdm(file.readlines(), desc="[COMBOS LEFT]", unit=' lines',
                     bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):
        count += 1

        email, password, domain, d_split = splitter(line)

        try:
            number = domain_dict[domain] + 1
        except:
            number = 1

        domain_dict.update({domain: number})

    domain_dict = sorted(domain_dict.items(), key=lambda item: item[1], reverse=True)

    show = input('[LINES TO SHOW]: ')

    try:
        show = abs(int(show))
    except:
        print(Fore.RED + '[INPUT ERROR]')
        print(Fore.RED + '[DEFAULT NUMBER]: 10')
        print(Fore.RESET)
        show = 10

    count_stat = 0
    print(Fore.RESET + '')
    for one_stat in domain_dict:
        count_stat += 1

        quotient = int(one_stat[1]) / count
        prec = quotient * 100

        print(Fore.GREEN + '[' + '@' + one_stat[0] + ']: ' + str(one_stat[1]) + ' (' + str(
            round(prec, round_func(prec))) + '%)')

        if count_stat == show:
            break

    print(Fore.RESET + '')
    input('Done! Press any key...')


def combo_merge():
    count = 0
    final_count = 0
    c_error = 0
    complete = []

    print(Fore.RED + '[SELECT ALL FILES TO MERGE]')
    print(Fore.RESET + '')
    files = file_select(multiple=True, title='Select multiple combofiles')

    data_folder, time_folder, data_folder_name, time_folder_name = check_dir()
    combo_final = open(data_folder_name + '/' + time_folder_name + '/merged combo [COMBOTOOLS].txt', 'wb')

    for file_dest in files:

        file = open(file_dest, encoding='ISO-8859-1')

        print('')
        print(Fore.GREEN + "File: " + file_dest + Fore.RESET)

        memory_access_a = memory_access(file, file_dest)

        for line in tqdm(memory_access_a, desc="[COMBOS LEFT]", unit=' lines',
                         bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):
            count += 1
            final_count += 1

            try:
                complete.append(line)
            except:
                c_error += 1

            if count >= 100000:
                for combo_line in complete:
                    combo_final.write(combo_line.encode('utf-8', 'ignore'))
                count = 0
                complete = []

    if True:
        for combo_line in complete:
            combo_final.write(combo_line.encode('utf-8', 'ignore'))

    # stats
    print('')
    print('[LINES MERGED]: ' + str(final_count))
    print('[ERRORS]: ' + str(c_error))
    print('')

    combo_final.close()
    input('Done! Press any key...')


def domain_change():
    count = 0
    count_sorted = 0
    complete = []
    split_symbol = ':'
    combo = ''

    data_folder, time_folder, data_folder_name, time_folder_name = check_dir()

    file = open(file_select(multiple=False, title=False), encoding='utf-8')
    changed_domain = open(data_folder_name + '/' + time_folder_name + '/changed domain [COMBOTOOLS].txt', 'wb')

    domain_to_change = inputbox(question='Type domain: ')

    for line in tqdm(file.readlines(), desc="[COMBOS LEFT]", unit=' lines',
                     bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):
        count += 1
        count_sorted += 1
        check_ban = 0

        email, password, domain, d_split = splitter(line)

        try:
            combo = d_split[0] + '@' + domain_to_change + split_symbol + password
        except:
            check_ban = 1

        if check_ban == 0:
            complete.append(combo)

        if count >= 100000:
            for combo_line in complete:
                changed_domain.write(combo_line.encode('utf-8', 'ignore'))
            count = 0
            complete = []

    if True:
        for combo_line in complete:
            changed_domain.write(combo_line.encode('utf-8', 'ignore'))

    changed_domain.close()

    input('Done! Press any key...')


def file_split():
    print("file split")

    #

    #    TODO  file_split

    #


def remove_duplicates():
    removed = 0
    stay = 0
    uni_error = 0
    n_digits = 0
    z_digits = 0
    place = 0

    data_folder, time_folder, data_folder_name, time_folder_name = check_dir()
    completed_lines_hash = set()

    file = open(file_select(multiple=False, title=False), encoding='utf-8')
    wo_duplicates = open(data_folder_name + '/' + time_folder_name + '/removed duplicates [COMBOTOOLS].txt', 'wb')

    for line in tqdm(file.readlines(), desc="[COMBOS LEFT]", unit=' lines',
                     bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):
        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        if hashValue not in completed_lines_hash:
            stay += 1

            try:
                wo_duplicates.write(line.encode('utf-8', 'ignore'))
            except:
                uni_error += 1

            completed_lines_hash.add(hashValue)
        else:
            removed += 1

    wo_duplicates.close()

    quotient_rem = removed / stay
    quotient_err = uni_error / stay

    prec_rem = quotient_rem * 100
    prec_err = quotient_err * 100

    for digit in str(prec_rem):

        try:
            digit = int(digit)
        except:
            digit = 9

        if digit == 0:
            z_digits += 1
        else:
            n_digits += 1
            if n_digits > 1:
                place = n_digits + z_digits - 1
                break

    print(Fore.RESET + '')
    print(Fore.GREEN + '[STAY]: ' + str(stay))
    print(Fore.GREEN + '[REMOVED]: ' + str(removed) + ' (' + str(round(prec_rem, place)) + '%)')

    if uni_error > 0:
        print(Fore.RED + '[ENCODE ERROR]: ' + str(uni_error) + ' (' + str(round(prec_err, place)) + '%)')

    print(Fore.RESET + '')

    input('Done! Press any key...')


def wordlist_combo():
    split_symbol = ':'
    fake_password = '0'

    print(Fore.RESET)
    combo_limit = input('[INPUT NUMBER OF LINES (zero for no-limit)]: ')
    while True:
        try:
            combo_limit = int(combo_limit)
            print('')
            break
        except:
            os.system('cls')
            logo()
            print('')
            print(Fore.RED + '[INPUT ERROR]')
            combo_limit = input(Fore.RED + '[TRY AGAIN (type "ok" to exit)]: ' + Fore.RESET)
            if combo_limit == 'ok':
                closing(message="Goodbye!", sleep_time=2)

    fake_domain = inputbox(question='Type domain: ')
    fake_domain = '@' + fake_domain

    data_folder, time_folder, data_folder_name, time_folder_name = check_dir()
    complete = []

    file_dest = file_select(multiple=False, title=False)
    file = open(file_dest, encoding='ISO-8859-1')
    file_complete = open(data_folder_name + '/' + time_folder_name + '/wordlist combo [COMBOTOOLS].txt', 'wb')

    memory_access_a = memory_access(file, file_dest)

    count = 0
    count_sorted = 0

    for line in tqdm(memory_access_a, desc="[COMBOS LEFT]", unit=' lines',
                     bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):
        count += 1
        count_sorted += 1
        check_ban = 0
        combo = 0

        email, password, domain, d_split = splitter(line)
        email = email.strip()

        try:
            combo = email + fake_domain + split_symbol + fake_password
        except:
            check_ban = 1

        if check_ban == 0:
            combo = str(combo) + '\n'
            complete.append(combo)

        if count >= 100000:
            for combo_line in complete:
                file_complete.write(combo_line.encode('utf-8', 'ignore'))
            count = 0
            complete = []

        if combo_limit != 0:
            if count_sorted == combo_limit:
                break

    if True:
        for combo_line in complete:
            file_complete.write(combo_line.encode('utf-8', 'ignore'))

    file_complete.close()

    input('Done! Press any key...')


if __name__ == '__main__':
    __index__ = 'combotools'
    __title__ = __index__ + ' by COLDERVOID'
    __version__ = '0.8.9_0'
    __DEBUG__ = False

    try:
        code = sys.argv[1]
    except:
        __DEBUG__ = False
    else:
        if code == '81b672f9':
            __DEBUG__ = True
        else:
            __DEBUG__ = False

    if __DEBUG__:
        __title__ = __title__ + ' =DEBUG MODE='
        __index__ = __index__ + ' =DEBUG MODE='

    os.system("title " + __title__)

    logo()  # wyswietl logo

    selector = menu()

    if selector == '1':
        sort()

    elif selector == '2':
        email_to_user()

    elif selector == '3':
        email_stats()

    elif selector == '4':
        combo_merge()

    elif selector == '5':
        domain_change()

    elif selector == '6':
        file_split()

    elif selector == '7':
        remove_duplicates()

    elif selector == '8':
        donut()

    elif selector == 'x' and __DEBUG__:
        domains_to_yopmail()
    elif selector == 'y' and __DEBUG__:
        wordlist_combo()

    else:
        closing(message="Goodbye!", sleep_time=2)
