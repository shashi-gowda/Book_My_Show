import re
class ticket_counter:
    def __init__(self):
        print(' Welcome to Book-My-Show '.center(40, '*'))
        self.rows = input("--> Enter No.of Rows: ")  # no of rows in theatre
        self.columns = input("--> Enter No.of Columns: ")  # no of columns in rows
        while self.rows=='0' or self.columns=='0' or self.rows.isdigit() == False or self.columns.isdigit() == False:
            print('\n** Only Non Zero Number inputs are allowed **')
            self.rows = input('--> Enter No. of Rows: ')
            self.columns = input('--> Enter No. of columns: ')
            continue

        self.rows = int(self.rows)
        self.columns = int(self.columns)
        self.row = []
        for i in range(self.rows):
            self.seats = []
            for j in range(self.columns):
                self.seats.append('s')
            self.row.append(self.seats)
        self.details = {}
        self.total_tickets = 0

        for i in self.row:
            for j in i:
                self.total_tickets += 1  # total number of available seats in theatre
            self.current_income = 0

    def show_seats(self):
        print(' Please Check Out The Seats Available/Booked '.center(80, '*'))
        print(end='  ')
        for j in range(self.columns):
            print(j+1, end=" ")
        print()
        for i in range(self.rows):
            print(i+1, end=" ")
            for j in range(self.columns):
                print(self.row[i][j], end=" ")
            print()

    def buy_ticket(self):
        print(f'*** Welcome to the Ticket Counter ***\n*** You can Select the Seats in {self.rows} rows and {self.columns} columns ***')
        self.r = input('\n--> please select the row: ')  # selecting the row by customer
        self.c = input('--> please select the column: ')  # selecting column by customer
        while self.r == '0' or self.c == '0' or self.r.isdigit() == False or self.c.isdigit() == False:
            print('**Please Ensure to select row and column in numbers starting from 1')
            self.r = input('--> Please select the row: ')
            self.c = input('--> Please select the column: ')
            continue
        self.r = int(self.r)
        self.c = int(self.c)

        while int(self.r) > self.rows or int(self.c) > self.columns:
            print(f'*** Please Choose the Seats in Theatre Capacity of Seats in {self.rows} rows and {self.columns} columns ***')
            self.r = input('--> Please select the row: ')
            self.c = input('--> Please select the column in the selected row: ')
            continue

        if (self.r, self.c) in self.details:
            print('You are trying to book the seat which is already booked, Please book other Seat!')
        else:
            print('\n** Please Enter Your Details **\n')
            self.name = input('--> Please Enter your Name: ')
            while self.name.isalpha() == False:
                print('Please Enter Your Name Using alphabets!!')
                self.name = input('--> Please Enter Your Name: ')
                continue

            self.age = input('--> Please Enter Your Age: ')
            while self.age.isdigit() == False:
                print('Please Select Age in Numbers!')
                self.age = input('--> Please Enter Your Age: ')
                continue
            self.age = int(self.age)

            self.gender = input('--> Please Select Your Gender Male/Female/Other: ')
            while self.gender.casefold() not in ['male', 'female', 'other']:
                print('Please Choose Correct Gender!!')
                self.gender = input('--> Enter your Gender: ')
                continue

            self.phone = input('--> Please Enter your phone number: ')
            self.mat = re.fullmatch("[6-9][0-9]{9}", self.phone)
            while self.phone.isdigit() == False or self.mat==None:
                print('Please Enter Your Phone Number in 10 Digits only!')
                self.phone = input('--> Please Enter Your Phone Number: ')
                self.mat = re.fullmatch("[6-9][0-9]{9}", self.phone)
                continue
            self.phone = int(self.phone)

            self.confirm = input('--> Confirm Your Ticket_Booking (Yes/No): ')
            while self.confirm.isalpha() == False:
                print('Please enter word Yes/No !')
                self.confirm = input('--> Confirm Your Booking by Typing Yes/No: ')
                continue
            self.confirm = self.confirm.casefold()

            if self.confirm == 'yes':
                if self.total_tickets <= 60:
                    self.choose = input('--> Your ticket price is 10$, if you want to confirm, Please type Yes/No: ')
                    while self.choose.isalpha() == False:
                        print('Please input your Choice in words only')
                        self.choose = input('--> Your ticket price is 10$, if you want to confirm, Please type Yes/No: ')
                        continue
                    self.choose = self.choose.casefold()
                    if self.choose == 'yes':
                        self.current_income += 10
                        self.row[self.r - 1][self.c - 1] = 'B' #B replaces S
                        self.details[(self.r, self.c)] = [self.name.capitalize(), self.age, self.gender.capitalize(),self.phone]
                    else:
                        print('Thank you for visiting Book-My-Show, Please Visit Again!!')

                elif self.total_tickets >= 61:
                    if self.r <= (self.rows // 2):
                        self.choose = input('--> Your ticket price is 10$, if you want to confirm, Please type Yes/No: ')
                        while self.choose.isalpha() == False:
                            print('Please choose your options in alphabets only!')
                            self.choose = input('--> Your ticket price is 10$, if you want to confirm, Please type Yes/No: ')
                            continue
                        self.choose = self.choose.casefold()
                        if self.choose == 'yes':
                            self.current_income = self.current_income + 10
                            self.row[self.r - 1][self.c - 1] = 'B'
                            self.details[(self.r, self.c)] = [self.name.capitalize(), self.age,self.gender.capitalize(), self.phone]
                        else:
                            print('Thank you for visiting Book-My-Show, Please Visit Again!!')

                    else:
                        self.choose = input('--> Your ticket price is 8$, if you want to confirm, Please type Yes/No: ')
                        while self.choose.isalpha() == False:
                            print('Please choose your options in alphabets only!')
                            self.choose = input('--> Your ticket price is 8$, if you want to confirm, Please type Yes/No: ')
                            continue
                        self.choose = self.choose.casefold()
                        if self.choose == 'yes':
                            self.current_income = self.current_income + 8
                            self.row[self.r - 1][self.c - 1] = 'B'
                            self.details[(self.r, self.c)] = [self.name.capitalize(), self.age,self.gender.capitalize(), self.phone]
                        else:
                            print('Thank you for visiting Book-My-Show, Please Visit Again!!')

                print('\n** You can see the reserved/booked seats marked in B **\n')
                self.show_seats()
            elif self.confirm=='no':
                print('Thanks for visiting Book-My_show, Please Visit Again!!')

    def statistics(self):
        print('\n*** Stats of the Movie_Tickets ***\n')
        self.total = 0
        for i in range(len(self.row)):
            j=self.row[i].count('B')
            self.total+=j
        print(f'Total number of Seats booked are: {self.total}')
        self.percentage = (self.total / self.total_tickets) * 100
        print(f'Booking percentage is : {self.percentage}')
        print(f'current income is : {self.current_income} $')
        self.total_income = 10
        if self.total_tickets <= 60:
            self.total_income = self.total_tickets * 10
        else:
            self.front=(self.rows//2)*self.columns
            self.back = self.total_tickets - self.front
            self.total_income = (self.front * 10 + self.back * 8)
        print(f'Total income is: {self.total_income} $')

    def get_details(self):
        print(" CUSTOMER DETAILS ".center(80, '-'))
        try:
            self.rr = int(input('Please enter row number you want: '))
            self.ss = int(input('Please enter column number you want: '))
            self.u = (self.rr, self.ss)
            self.a = self.details[self.u]
            print('name:', self.a[0])
            print('age:', self.a[1])
            print('Gender:', self.a[2])
            print('Phone Number:', self.a[3])
            if self.total_tickets <= 60:
                print('Ticket Price: 10$')
            else:
                if self.rr <= self.rows // 2:
                    print('Ticket Price: 10$')
                else:
                    print('Ticket Price: 8$')
        except:
            print('Sorry we don\'t have that seat!!')
















