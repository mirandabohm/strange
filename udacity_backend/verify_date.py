import cgi

def valid_month(month):
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    months = [m.lower() for m in months]
    month = month.lower()

    if month in months:
        month = month[0].upper() + month[1::]
    else:
        print('Sorry, that is a not a valid month.')
        month = None
    return month

def valid_day(day):
    if day.isdigit() and int(day) < 32 and int(day) > 0:
        day = int(day)
    else:
        day = None
    return day

def valid_year(year):
    if year.isdigit() and int(year) < 2021 and int(year) > 1899:
        year = int(year)
    else:
        year = None
    return year

def escape_html(s):
    return cgi.escape(s, quote = True)