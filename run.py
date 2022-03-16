from website.website import Website


try:
    with Website() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.change_country(language='en-us')
        bot.select_destination(destination='New York')
        bot.select_dates(check_in_date='2022-03-18',
                         check_out_date='2022-03-21')
        bot.select_adults(count=1)
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
