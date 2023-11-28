from time import sleep
from booking.booking import Booking


# inst = Booking()
# inst.land_first_page()

with Booking() as bot:
    bot.land_first_page()
    print("Existing...")
    # bot.change_currency(currency="USD")
    bot.select_place_to_go(place_to_go="New York")

sleep(30)
