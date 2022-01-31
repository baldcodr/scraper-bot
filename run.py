from locale import currency
from booking.booking import Booking

with Booking() as bot:
    bot.open_home_page()
    bot.accept_cookies()
    bot.select_currency(currency='GBP')
    bot.select_destination('New York')
    bot.select_date(check_in_date='2022-02-03',check_out_date='2022-02-28')
    bot.select_adults()