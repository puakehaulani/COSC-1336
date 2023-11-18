# lexi scales, complete.
# this program reads a string from the user containing a date in the form mm/dd/yyyy, and converts it to be printed in format Month day, year.

import datetime

month_dict = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

def main():
    # enter_date function, with return saved to var
    user_date = enter_date()
    # split string to pieces to reformat
    date_tokens = user_date.split('/')    
    # print new format
    print(f'month_dict[date_tokens[0]] {date_tokens[1]}, {date_tokens[2]}')
    
# enter_date prompts a user to enter a date then verifies it is a valid date in the format specified. it handles exceptions by rerunning the function. it returns the valid date object.
def enter_date():
    try:
    # user enters date in format mm/dd/yyy
        date_input = str(input('Enter a date in the format mm/dd/yyy: '))
    # verify entry meets format and is a valid date
        datetime.datetime.strptime(date_input, '%m/%d/%Y')
        return date_input
    # rerun function if encounters exception
    except Exception as err:
        print(f'Error: {err}')
        return enter_date()
    
if __name__ == '__main__':
    main()