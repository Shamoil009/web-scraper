from time import sleep
from booking.booking import Booking


# inst = Booking()
# inst.land_first_page()

with Booking() as bot:
    bot.land_first_page()
    print("Existing...")
    # bot.change_currency(currency="USD")
    bot.select_place_to_go(place_to_go="New York")
    bot.select_dates(check_in_date="2023-12-05", check_out_date="2023-12-24")
    bot.select_adults(count=30)
    bot.click_search()


sleep(30)
