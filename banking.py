# Write your code here
import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

"""
cur.execute_stmt('''
create table card( 
id integer, 
number text, 
pin text, 
balance integer default 0 
)''')
"""

number_id = 0
card_number = [4, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
card_num_attempt = 0
card_pin = ""
card_pin_attempt = 0
choice = 4
correct_pin = False
balance2 = 0
random_num = 0
total_num = 8
str_card_number = ""
luhn_card_number = [4, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
luhn_total = 0
transfer_number = ""
get_transfer_balance = ""
transfer_balance = ""
transfer_amount = 0


def check_luhn_algorithm(input_number):
    total = 0
    list_input_number = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i2 in range(16):
        list_input_number[i2] = input_number[i2]
        list_input_number[i2] = int(list_input_number[i2])
        if i2 % 2 == 0:
            list_input_number[i2] *= 2
            if list_input_number[i2] > 9:
                list_input_number[i2] -= 9
        total += list_input_number[i2]
    if total % 10 == 0:
        return True
    else:
        return False
    # print(list_input_number)
    # print(type(list_input_number))
    # print(total)


while not correct_pin:
    print("1. Create an account")
    print("2. Log into an account")
    print("0. Exit")
    choice = input()

    if choice == "1":
        # reset card array - this is required for checking multiple card numbers
        card_number = [4, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        luhn_card_number = [4, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

        # first get random numbers for digits 5 to 15 (i.e., [4] to [14]
        for i in range(5, 14):
            rand_int = random.randint(1, 9)
            card_number[i] = card_number[i] * rand_int
            luhn_card_number[i] = luhn_card_number[i] * rand_int

        for i in range(14):
            if i % 2 == 0:  # multiply odd digits by 2
                # last digit is in even digit. It will not impacted by the if conditions
                luhn_card_number[i] = luhn_card_number[i] * 2
                if luhn_card_number[i] > 9:  # subtract 9 from numbers over 9
                    luhn_card_number[i] = luhn_card_number[i] - 9
            # luhn total for the first 15 digits are added up
            luhn_total = luhn_total + luhn_card_number[i]

        # adding digit 16 and checking if the sum is divisible by 10
        if luhn_total % 10 != 0:
            for i in range(1, 10):
                luhn_card_number[15] = i
                luhn_total += 1
                if luhn_total % 10 == 0:
                    break

        card_number[15] = luhn_card_number[15]

        if card_number[15] >= 2:
            card_number[15] -= 2
        else:
            card_number[15] += 8
        card_pin = random.randint(1000, 9999)
        for i in range(16):
            card_number[i] = str(card_number[i])
        str_card_number = (' '.join(card_number))
        str_card_number = str(str_card_number)
        str_card_number = str_card_number.replace(" ", "")
        str_card_number = int(str_card_number)
        number_id += 1
        execute_stmt = '''INSERT INTO card (id, number, pin, balance) 
        VALUES (''' + str(number_id) + ''',''' + str(str_card_number) + ''',''' + '''
        ''' + str(card_pin) + ''',''' + str(balance2) + ''')'''
        str_card_number = str(str_card_number)

        print("Your card number has been created")
        print("Your card number:")

        print(str_card_number)
        number_id += 1
        print("Your card PIN:")
        # print(execute_stmt)

        cur.execute(execute_stmt)
        # (number_id, card_number, card_pin, balance))
        conn.commit()
        card_pin = str(card_pin)
        print(card_pin)

    if choice == "2":
        print("Enter your card number:")
        card_num_attempt = input()
        print("Enter your PIN:")
        card_pin_attempt = input()
        # correct_card_pin = check_number_and_pin(card_num_attempt, card_pin_attempt)

        get_number_stmt2 = '''
        select
            number,
            pin 
        from card
        where 
        number = ''' + str(card_num_attempt) + '''
        and pin = ''' + str(card_pin_attempt) + ''''''

        cur.execute(get_number_stmt2)
        credit_acc_record = cur.fetchall()
        # print(credit_acc_record)
        card_number2 = ""
        pin2 = ""
        for row in credit_acc_record:
            card_number2 = row[0]
            pin2 = row[1]
            # print("number is ", card_number2)
            # print("pin is ", pin2)

        conn.commit()
        if card_num_attempt == card_number2 and card_pin_attempt == pin2:
            correct_pin = True

        if correct_pin:
            # correct_pin = True
            print("You have successfully logged in!")
            print("1. Balance")
            print("2. Add income")
            print("3. Do transfer")
            print("4. Close account")
            print("5. Log out")
            print("0. Exit")
        else:
            print("Wrong card number or PIN!")
    if choice == "0":
        print("Bye!")
        exit()

while correct_pin:
    choice = input()
    balance_get_stmt = '''
    select
        balance
    from card
    where
    number = ''' + str(card_num_attempt) + '''
    and pin = ''' + str(card_pin_attempt) + ''''''
    cur.execute(balance_get_stmt)
    balance_record = cur.fetchall()
    balance = ""
    for row in balance_record:
        balance = row[0]
        conn.commit()
    if choice == "1":
        print(balance)
    if choice == "2":
        print("Enter income:")
        balance_update = int(input())
        balance += balance_update
        balance_update_stmt = '''
        update card
        set balance = ''' + str(balance) + '''
        where 
        number = ''' + str(card_num_attempt) + '''
        and pin = ''' + str(card_pin_attempt) + ''''''
        cur.execute(balance_update_stmt)
        conn.commit()
        print("Income was added!")

    if choice == "3":
        print("Transfer")
        print("Enter card number:")

        card_num_transfer = input()
        card_works = True
        if len(card_num_transfer) != 16:
            print("Probably you made mistake in the card number.")
            print("Please try again!")
            card_works = False
        if not check_luhn_algorithm(card_num_transfer):
            print("Probably you made mistake in the card number.")
            print("Please try again!")
            card_works = False
        if card_works:
            get_transfer_num_stmt = '''
            select 
                number
            from card
            where
            number = ''' + card_num_transfer + ''''''
            cur.execute(get_transfer_num_stmt)
            get_transfer_number = cur.fetchall()
            if len(get_transfer_number) > 0:
                for row in get_transfer_number:
                    transfer_number = row[0]
                # print(get_transfer_number)
                # print(type(get_transfer_number))
                # print(len(get_transfer_number))
            else:
                card_works = False
                print('Such a card does not exist.')
        if card_works:
            update_from_balance_stmt = '''
            update card
            set balance = ''' + str(transfer_balance) + '''
            where
            number = ''' + str(transfer_number) + ''''''

            update_to_balance_stmt = '''
            update card
            set balance = ''' + str(balance) + '''
            where
            number = ''' + str(card_num_attempt) + ''''''

            get_transfer_to_balance_stmt = '''
            select
                balance
            from card
            where 
            number = ''' + str(transfer_number) + ''''''
            cur.execute(get_transfer_to_balance_stmt)
            get_transfer_balance = cur.fetchall()

            for row in get_transfer_balance:
                transfer_balance = row[0]
            print("Enter how much money you want to transfer:")
            transfer_amount = int(input())

            if balance >= transfer_amount:
                transfer_balance += transfer_amount
                balance -= transfer_amount
                update_from_balance_stmt = '''
                update card
                set balance = ''' + str(transfer_balance) + '''
                where
                number = ''' + str(transfer_number) + ''''''

                update_to_balance_stmt = '''
                update card
                set balance = ''' + str(balance) + '''
                where
                number = ''' + str(card_num_attempt) + ''''''
                cur.execute(update_from_balance_stmt)
                conn.commit()
                cur.execute(update_to_balance_stmt)
                conn.commit()

                print("Success!")
            else:
                print("Not enough money!")

    if choice == "4":
        card_delete_stmt = '''
        delete 
        from card
        where
        number = ''' + str(card_num_attempt) + '''
        and pin = ''' + str(card_pin_attempt) + ''''''
        cur.execute(card_delete_stmt)
        conn.commit()
        print("The account has been closed!")

    if choice == "0":
        print("Bye!")
        exit()
    print()
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")
