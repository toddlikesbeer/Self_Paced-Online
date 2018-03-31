#!/usr/bin/env python

def send_thank_you():
    """Print a thank you email"""
    while True:
        full_name = input("Please enter donor's full name: ")
        if full_name.lower() == 'list'
            print(donor_names)
        elif full_name.lower() == 'quit'
            return
        elif not full_name in donor_names:
            add_donor(full_name)
            break
        else:
            break
      
    donation = float(input('Enter the donation amount: '))
    add_donation(full_name,donation)

    write_email(full_name,donation)
  
  
def create_report():
    """Print a donation report"""
    #Print header

  
def add_donor(donor_name):
    """Add a donor to donor list"""
    donors.append([donor_name])
    donor_names.append(donor_name)
  
  
def add_donation(donor_name, amount):
    """Add donation amount to list under donors name"""
    for donor in donors:
    if donor[0] == donor_name
        donor.append(amount)
        return

    
def write_email(donor_name, amount):
    """Print a thank you email"""
    print('FROM: Your friendly local charity mailroom.')
    print('TO: {}'.format(donor_name))
    print('RE: Your recent donation')
    print('\nThank you so much for your recent donation of ${:,.2f}. This will'
          ' go a long way towards helping to save the pythons. Your generosity'
          ' is most appreciated!'.format(amount))
    print('\nBest Regards,\nSave The Pythons\n\n')
  
  
if __name__ == '__main__':
    donors = [['Bill Gates',789.25,87562.22,125000.00],
              ['Jeff Bezos',3456.89,130],['Jimmy Buffett',85000],
              ['Abe Lincoln',5,2,1],['Yankee Doodle',67]]
    donor_names = [donor[0] for donor in donors]

    while True:
        main_menu = input('Select an option: "Send a Thank You", '
                          '"Create Report", "quit" > ')
        if main_menu.lower() == 'send a thank you':
            send_thank_you()
        elif main_menu.lower() == 'create report':
            create_report()
        elif main_menu.lower() == 'quit'
            break
        else:
            print('Please select an option from the list.\n')
