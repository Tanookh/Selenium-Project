from website.website import Website


with Website() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.change_country(language='en-us')
    bot.select_destination(destination='New York')
    bot.select_dates(check_in_date='2022-03-18',
                     check_out_date='2022-03-21')
    bot.select_adults(count=3)
    bot.click_search()
    bot.apply_filtration(4, 5)

