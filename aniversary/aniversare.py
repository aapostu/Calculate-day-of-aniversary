from datetime import date

""" Program that calculates on which day of the week the
    anniversary will be after n years """

def get_weekday(n: str, birthday: str)-> date.weekday:
    """
    birthday: yyyy-mm-dd
    :param n:
    :param birthday:
    :return: date object - weekday anniversary

    """
    WEEKDAY = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday",
                5:"Saturday", 6:"Sunday"}
    try:
        years = int(n)
    except ValueError as e:
        print(f'The error occurred: -> {e}.'
              f'The year must be integer')
    else:
        current_year = date.today().year
        birthday = f'{current_year + years}{birthday[birthday.find("-")::]}'
        return WEEKDAY[date.fromisoformat(birthday).weekday()]
        #fromisoformat.weekday return number of day in week

if __name__ == "__main__":
    n = input('number years')
    birthday = input('your birthday: ')
    day = get_weekday(n, birthday)
    print(day)

