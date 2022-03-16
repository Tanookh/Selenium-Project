from website.website import Website


try:
    with Website() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.change_country(language='en-us')
        bot.select_destination(destination=input("Where do you want to travel to? "))
        bot.select_dates(check_in_date=input("When do you want to leave? "),
                         check_out_date=input("When do you want to get back? "))
        bot.select_adults(count=int(input("How many are you? ")))
        bot.click_search()
        bot.apply_filtration(4, 5)
        bot.refresh() # A refresh to let the bot grab the data properly
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
