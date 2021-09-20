from datetime import datetime
from tqdm import tqdm
from colorama import Fore
from os import system


def logo():
    print('')
    print(' __   __        __   ___  __        ___ ___       __   __       ')
    print('/  ` /  \ |    |  \ |__  |__) |\ | |__   |  |  | /  \ |__) |__/ ' + '  ' + 'combotools')
    print('\__, \__/ |___ |__/ |___ |  \ | \| |___  |  |/\| \__/ |  \ |  \ ' + '  ' + 'version: ' + __version__)
    print('')
    print('')


def sort():
    banned_emails = ['gmail.', 'hotmail.', 'yahoo.', 'aol.', 'live.', 'outlook.', 'msn.', '###NULL###']
    sorted_table_wo_banned = []
    dumped_email = []
    domain_table = []
    split_symbol = ':'
    null_email = 0
    null_pass = 0
    new_line = bytes([0x0A])

    filename = 'input' + '.txt'

    combolist = open(filename, encoding='utf-8')
    sorted_combolist = open(str(datetime.date(datetime.now())) + ' [SORTED COMBO].txt', 'wb')

    dumped_combo = open('dumped.txt', 'wb')

    domain_list = open('domains.txt', 'wb')

    linijki = combolist.read().splitlines()

    count = 0
    for line in tqdm(linijki, desc="[COMBOS LEFT]", unit=' lines', bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTRED_EX, Fore.RESET)):
        count += 1
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

    for o_combo in sorted_table_wo_banned:
        sorted_combolist.write(o_combo.encode('utf-8', 'ignore') + new_line)

    for o_combo in dumped_email:
        dumped_combo.write(o_combo.encode('utf-8', 'ignore') + new_line)

    for o_domain_list in domain_table:
        domain_list.write(o_domain_list.encode('utf-8', 'ignore') + new_line)

    print('')
    print('[EMAIL SORTED]: ' + str(len(sorted_table_wo_banned)))
    print('[COMBO ERRORS]: ' + str(null_email + null_pass))
    print('')

    input('Done! Press any key...')


if __name__ == '__main__':
    __title__ = 'combotools by COLDERVOID'
    __version__ = '0.2.2'
    system("title " + __title__)
    logo()
    sort()
