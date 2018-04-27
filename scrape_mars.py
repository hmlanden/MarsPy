def scrape():
    """
    Returns a dictionary with images and data on Mars. Contains the
    following information in the following formats:
    - Recent headlines (List)
    - Featured image URL (string)
    - Most recent weather (HTML Table)
    - Facts (HTML Table)
    - Image URLs for Hemisphere Pictures (List of Dict)
    """
    
    # ------------------------------------------------------------
    #  Step 1: Import all required modules and initialize all tools
    # ------------------------------------------------------------
    from bs4 import BeautifulSoup as soup
    from splinter import Browser
    import pandas as pd
    import aux_func as aux

    # initialize splinter browser
    browser = Browser('chrome', 
                      **{"executable_path": "/usr/local/bin/chromedriver"}, 
                      headless=False)

    # ------------------------------------------------------------
    #  Step 2: Scrape Nasa Mars News website for recent headlines
    #  with headlines, dates, and content preview
    # ------------------------------------------------------------
    url = aux.hidden_urls[0]
    try:
        webpage = aux.getParsedWebpage(browser, url)

        # pull the most recent headlines + info from the website
        headlines = soup.find_all(webpage, 'h3', class_=None)
        dates = soup.find_all(webpage, 'div', class_='list_date')
        text = soup.find_all(webpage, 'div', class_='article_teaser_body')

        # iterate through and generate lists of all individual items
        zipped_headlines = list(zip(aux.getParsedTextList(headlines),
                                    aux.getParsedTextList(dates),
                                    aux.getParsedTextList(text)))

        # generate a readable dataframe
        headline_df = pd.DataFrame(zipped_headlines)
        headline_df.rename(columns={0:'headline', 
                                    1:'date', 
                                    2:'text'}, 
                           inplace=True)
        headline_html = pd.DataFrame.to_html(headline_df)
    except: 
        print(error)

    # ------------------------------------------------------------
    #  Step 3: Scrape Nasa Mars News website for featured image
    # ------------------------------------------------------------
    try:
        url = aux.hidden_urls[1]
        webpage = aux.getParsedWebpage(browser, url)

        # get title and description
        featured_title = soup.find(webpage, 'h1', 
                                   class_='media_feature_title').get_text()
        featured_description = soup.find(webpage, 'a', 
                                         class_='button fancybox').get('data-description')

        # get and construct url for largest size of featured image available
        featured_url = soup.find(webpage, 'a', 
                                 class_='button fancybox').get('data-fancybox-href')
        featured_filename = featured_url.split('/')[4].split('_')[0]
        featured_url = f'https://www.jpl.nasa.gov/spaceimages/images/largesize/{featured_filename}_hires.jpg'
    
    except:
        print(error)

    # ------------------------------------------------------------
    #  Step 4: Scrape Mars Twitter for the most recent weather 
    #  update
    # ------------------------------------------------------------
    try:
        url = aux.hidden_urls[2]
        webpage = aux.getParsedWebpage(browser, url)

        std_tweet_class = 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'

        # pull text of most recent tweet about the weather
        recent_weather = soup.find_all(webpage, 'p', class_= std_tweet_class)[0].get_text()

        # create split string to pull apart and add to dataframe
        recent_weather_split = recent_weather.split(',')
        recent_weather_split = [i.split(' ') for i in recent_weather_split][2:]

        # create dictionary to turn into a dataframe
        weather_dict = {'mars_date':f'{recent_weather.split("(")[0]}',
                        'earth_date':f'{recent_weather.split("(")[1].split(")")[0]}',
                        'cur_weather':f'{recent_weather_split[0][1]}',
                        'temp_high':f'{recent_weather_split[1][2]}',
                        'temp_low':f'{recent_weather_split[2][2]}',
                        'pressure':f'{recent_weather_split[3][3]} {recent_weather_split[3][4]}',
                        'daylight':f'{recent_weather_split[4][2]}'}
        weather_df = pd.DataFrame.from_dict(weather_dict, orient='index')
        weather_df = weather_df.rename(columns={0:'Most Recent Weather on Mars'})
        weather_html = pd.DataFrame.to_html(weather_df)
        
    except:
        print(error)

    # ------------------------------------------------------------
    #  Step 5: Scrape Space Facts website for data on Mars
    # ------------------------------------------------------------
    try:
        url = aux.hidden_urls[3]
        webpage = aux.getParsedWebpage(browser, url)

        # create dict to hold facts
        fact_dict = {}

        # get all rows in the facts table and parse into dict
        facts_all = soup.find(webpage, 
                              'table', 
                              class_='tablepress tablepress-id-mars').find_all('tr')
        for fact in facts_all:
            fact_dict[soup.find(fact, 'strong').get_text()] = (soup.find(fact, class_='column-2').get_text())

        # convert to Dataframe and to HTML table
        fact_df = pd.DataFrame.from_dict(fact_dict, orient='index')
        fact_df.rename(columns={0:'Facts about Mars'}, inplace=True)
        fact_html = pd.DataFrame.to_html(fact_df)
    except:
        print(error)

    # ------------------------------------------------------------
    #  Step 6: Scrape images and titles from Astrogeology site
    # ------------------------------------------------------------
    try:
        url = aux.hidden_urls[4]
        webpage = aux.getParsedWebpage(browser, url)

        # store the base link for the page
        base_url = 'https://astrogeology.usgs.gov/'

        # get all unique links to the photo pages first
        page_links_list = []
        page_links = soup.find_all(webpage, 'a', class_='itemLink product-item')
        [page_links_list.append(page.get('href')) for page in page_links]
        page_links_list = list(set(page_links_list))

        image_list = []

        # iterate through links and pull URL for full size images
        for link in page_links_list:
            url = f'https://astrogeology.usgs.gov{link}'
            webpage = aux.getParsedWebpage(browser, url)

            # get image title
            title = soup.find(webpage, 'h2', class_='title').get_text()

            # get full size image link
            downloads_section = soup.find(webpage, 'div', class_='downloads')
            image_link = soup.find(downloads_section, 'a').get('href')

            # add title and full-size image url to dict
            image_list.append({'title':title,
                               'image_url':image_link})
        
    except:
        print(error)
    
    # ------------------------------------------------------------
    #  Step 7: Stick everything into a dictionary and return it
    # ------------------------------------------------------------
    scrape_results_dict = {'headlines':zipped_headlines,
                           'featured_img_url':featured_url,
                           'weather':weather_html, 
                           'facts':fact_html, 
                           'image_urls':image_list}
    
    return scrape_results_dict;