from website.website import Website


with Website() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.change_country(country='en-us')
