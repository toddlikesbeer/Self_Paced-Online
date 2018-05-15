#!/usr/bin/env python3
import os
import datetime
from collections import defaultdict

"""
Lesson4 - Mailroom, Part 3
"""

now = datetime.datetime.now()

_donors = {
    'Jim Halpert': [1.00],
    'Pam Beesley': [1000.00, 2000.00, 3000.00],
    'Dwight Shrute': [2.00, 3.00],
    'Michael Scott': [10.00, 20.00, 30.00],
    'Andy Bernard': [500.00]
}


def quit_menu():
    return 'break'


def thank_donor(donor_name=None, donations=None):
    if donor_name is None:
        while True:
            donor_name = input('Type donor name: ')
            try:
                donations = _donors[donor_name]
            except KeyError:
                print('Type the exact donor name (see list): ', end='\n\n')
                list_donors()
            else:
                donor_email(donor_name, sum(donations), True)
                break
    else:
        donor_email(donor_name, donations, False)


def add_donor():
    while True:
        try:
            donor_name = input('Type donor name: ')
            if not donor_name:
                raise ValueError('String required.')
        except ValueError as e:
            print(e)
            continue
        else:
            if donor_name in _donors:
                print('Donor already exists, use append.')
                return
            _donors[donor_name] = defaultdict(list)
            break

    while True:
        try:
            donation = input('Donation amount: ')
            donation = float(donation)
            break
        except ValueError:
            print('Input must be a int/float, try again.')

    _donors[donor_name] = [float(donation)]
    thank_donor(donor_name, donation)


def list_donors():
    print('\n'.join([k for k in _donors.keys()]))


def append_donation():
    while True:
        try:
            donor_name = input('Type donor name: ')
            donations = _donors[donor_name]
            break
        except KeyError:
            print('Type the exact donor name (see list): ', end='\n\n')
            list_donors()

    while True:
        try:
            donation = input('Donation amount: ')
            donation = float(donation)
            break
        except ValueError:
            print('Input must be a int/float, try again.')

    donations.append(float(donation))
    thank_donor(donor_name, donation)


def format_currency_str(donation):
    donation = float(donation)
    donation = "${0:.2f}".format(donation)
    return donation


def donor_email(donor_name, amount, total=False):
    donation = format_currency_str(amount)
    str1 = ('Dear {},\n\n'
            '        Thank you for your very kind donation of {}.\n\n'
            '        It will be put to very good use.\n\n'
            '               Sincerely,\n'
            '                  -The Team')
    str2 = ('Dear {},\n\n'
            '        Thank you for your very kind donations totalling {}.\n\n'
            '        It will be put to very good use.\n\n'
            '               Sincerely,\n'
            '                  -The Team')
    body = str2 if total else str1
    print(body.format(donor_name, donation))


def generate_letters():
    cwd = os.getcwd()
    date = now.strftime('%Y-%m-%d')
    path = cwd + '/letters/'
    ext = '.txt'
    for key, val in _donors.items():
        total_donations = sum(val)
        name = key.split(' ')
        file_path = "{}{}_{}_{}{}".format(path, date, name[0], name[1], ext)
        donations = format_currency_str(total_donations)
        with open(file_path, 'w') as letter:
            text = ('Dear {} {},\n\n'
                    '        Thank you for your very kind donation of {}.\n\n'
                    '        It will be put to very good use.\n\n'
                    '               Sincerely,\n'
                    '                  -The Team')
            body = text.format(name[0], name[1], donations)
            letter.write(body)
    print('Letters created.')


def create_report():
    sorted_donors = sort_donors()
    rows = get_donor_summary(sorted_donors)
    print_report(rows)


def sort_donors():
    sorted_donors = sorted(_donors.items(), key=lambda x: x[1], reverse=True)
    return sorted_donors


def get_donor_summary(donors):
    """ pass summary list of strings that is ready for parsing"""
    summary = []
    for name, donations in _donors.items():
        total = float(sum(donations))
        number = len(donations)
        str_total = format_currency_str(total)
        str_number = str(len(donations))
        str_average = format_currency_str(total / max(number, 1))
        summary.append([name, str_total, str_number, str_average])
    return summary


def print_report(rows):
    # table heading
    h = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    hs = ' | '
    hf = '{0:<25}{1}{2}{3}{4}{5}{6}'
    print(hf.format(h[0], hs, h[1], hs, h[2], hs, h[3]))
    # table rows
    for r in rows:
        name = "{}".format(r[0])
        f0 = '{0:<' + str(max(len(name), 25)) + '}'
        f2 = '{2:>' + str(max(len(r[1]), len(h[1]))) + '}'
        f4 = '{4:>' + str(max(len(r[2]), len(h[2]))) + '}'
        f6 = '{6:>' + str(max(len(r[3]), len(h[3]))) + '}'
        rf = f0 + '{1}' + f2 + '{3}' + f4 + '{5}' + f6
        args = [name, '  $', r[1], ' | ', r[2], '  $', r[3]]
        print(rf.format(*args))


def menu_selection(prompt, dispatch):
    while True:
        r = input(prompt)
        if r not in dispatch:
            print('Please choose a valid menu option.')
            continue
        if dispatch[r]() == "break":
            break


def main_menu():
    main_prompt = ("\n--- MAIN MENU ---\n"
                   "What do you want to do?\n"
                   "Type '1' - Donors Menu\n"
                   "Type '2' - Reports Menu\n"
                   "Type '3' - Gratitude Menu\n"
                   "Type 'q' - Quit >> "
                   )
    main_dispatch = {'1': donors_sub_menu,
                     '2': reports_sub_menu,
                     '3': gratitude_sub_menu,
                     'q': quit_menu,
                     }
    menu_selection(main_prompt, main_dispatch)


def donors_sub_menu():
    donors_prompt = ("\n--- DONOR SUB MENU ---\n"
                     "Type '1' - Add Donor\n"
                     "Type '2' - Append Donation\n"
                     "Type '3' - List Donors\n"
                     "Type 'q' - Quit >> "
                     )
    donors_dispatch = {'1': add_donor,
                       '2': append_donation,
                       '3': list_donors,
                       'q': quit_menu,
                       }
    menu_selection(donors_prompt, donors_dispatch)


def reports_sub_menu():
    reports_prompt = ("\n--- REPORTS SUB MENU ---\n"
                      "Type '1' - Print Report\n"
                      "Type 'q' - Quit >> "
                      )
    reports_dispatch = {'1': create_report,
                        'q': quit_menu,
                        }
    menu_selection(reports_prompt, reports_dispatch)


def gratitude_sub_menu():
    gratitude_prompt = ("\n--- GRATITUDE SUB MENU ---\n"
                        "Type '1' - Print Individual Letter\n"
                        "Type '2' - Generate Letters for All Donors\n"
                        "Type 'q' - Quit >> "
                        )
    gratitude_dispatch = {'1': thank_donor,
                          '2': generate_letters,
                          'q': quit_menu,
                          }
    menu_selection(gratitude_prompt, gratitude_dispatch)


if __name__ == "__main__":
    main_menu()
