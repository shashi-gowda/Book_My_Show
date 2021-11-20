import ticketbook_stats
Okay = ticketbook_stats.ticket_counter()
while True:
    print('==================================================')
    print('1. Show the seats')
    print('2. Buy a tickets')
    print('3. Statistics')
    print('4. Show booked ticket user info')
    print('0. Exit')
    choice = input('Please select your choice from above Options: ')
    while choice.isdigit()==False:
        print('Please choose the choice in numbers')
        choice = input('Please select your choice from above Options: ')
        continue
    choice = int(choice)
    if choice==0:
        print(" THANK YOU & VISIT AGAIN ".center(80,'-'))
        break
    if choice ==1:
        Okay.show_seats()
    elif choice == 2:
        Okay.buy_ticket()
    elif choice==3:
        Okay.statistics()
    elif choice == 4:
        Okay.get_details()