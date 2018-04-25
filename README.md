

```python
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
```


```python
# ------------------------------------------------------------
#  Step 2: Scrape Nasa Mars News website for recent headlines
#  with headlines, dates, and content preview
# ------------------------------------------------------------
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
webpage = aux.getParsedWebpage(browser, url)

# pull the most recent headlines + info from the website
headlines_grouped = soup.find_all(webpage, 'h3', class_=None)
dates_grouped = soup.find_all(webpage, 'div', class_='list_date')
text_grouped = soup.find_all(webpage, 'div', class_='article_teaser_body')

# iterate through and generate lists of all individual items
zipped_headlines = list(zip(aux.getParsedTextList(headlines_grouped),
                            aux.getParsedTextList(dates_grouped),
                            aux.getParsedTextList(text_grouped)))

# generate a readable dataframe
headline_df = pd.DataFrame(zipped_headlines)
headline_df.rename(columns={0:'headline', 
                            1:'date', 
                            2:'text'}, 
                   inplace=True)
headline_df
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>headline</th>
      <th>date</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NASA Engineers Dream Big with Small Spacecraft</td>
      <td>April 19, 2018</td>
      <td>The first CubeSat mission to deep space will l...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bound for Mars: Countdown to First Interplanet...</td>
      <td>April  6, 2018</td>
      <td>On May 5, millions of Californians may witness...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NASA Invests in Visionary Technology</td>
      <td>March 30, 2018</td>
      <td>NASA is investing in technology concepts, incl...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NASA is Ready to Study the Heart of Mars</td>
      <td>March 29, 2018</td>
      <td>NASA is about to go on a journey to study the ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>‘Marsquakes’ Could Shake Up Planetary Science</td>
      <td>March 28, 2018</td>
      <td>InSight, the next mission to the Red Planet, w...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Mars Curiosity Celebrates Sol 2,000</td>
      <td>March 22, 2018</td>
      <td>NASA's Mars Curiosity rover just hit a new mil...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NASA Briefing on First Mission to Study Mars I...</td>
      <td>March 22, 2018</td>
      <td>NASA’s next mission to Mars will be the topic ...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>New 'AR' Mobile App Features 3-D NASA Spacecraft</td>
      <td>March 20, 2018</td>
      <td>NASA spacecraft travel to far-off destinations...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NASA Mars Mission Tours California</td>
      <td>March 14, 2018</td>
      <td>Scientists and engineers with NASA's next miss...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Next NASA Mars Rover Reaches Key Manufacturing...</td>
      <td>March 13, 2018</td>
      <td>NASA's Mars 2020 mission has begun the assembl...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Witness First Mars Launch from West Coast</td>
      <td>March 12, 2018</td>
      <td>NASA invites digital creators to apply for soc...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>360 Video: Tour a Mars Robot Test Lab</td>
      <td>March  8, 2018</td>
      <td>Engineers are practicing operations for NASA's...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>NASA InSight Mission to Mars Arrives at Launch...</td>
      <td>February 28, 2018</td>
      <td>NASA's InSight spacecraft has arrived at Vande...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Curiosity Tests a New Way to Drill on Mars</td>
      <td>February 28, 2018</td>
      <td>NASA's Mars Curiosity rover has conducted the ...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Seven Ways Mars InSight is Different</td>
      <td>February 22, 2018</td>
      <td>NASA has a long and successful track record at...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Nearly a Decade After Mars Phoenix Landed, Ano...</td>
      <td>February 20, 2018</td>
      <td>A recent view from Mars orbit of the site wher...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Spacecraft Exits Safe Mode</td>
      <td>February 16, 2018</td>
      <td>Diagnostic work is the focus for resuming serv...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>5,000 Days on Mars; Solar-Powered Rover Approa...</td>
      <td>February 15, 2018</td>
      <td>The Sun will rise on NASA's solar-powered Mars...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Long-Lived Mars Rover Opportunity Keeps Findin...</td>
      <td>February 15, 2018</td>
      <td>NASA's Mars Exploration Rover Opportunity keep...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>A Piece of Mars is Going Home</td>
      <td>February 13, 2018</td>
      <td>When it launches in 2020, NASA's next Mars rov...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Mars Reconnaissance Orbiter Preparing for Year...</td>
      <td>February  9, 2018</td>
      <td>NASA's Mars Reconnaissance Orbiter (MRO) has b...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Tiny Crystal Shapes Get Close Look From Mars R...</td>
      <td>February  8, 2018</td>
      <td>Star-shaped, tiny, dark bumps in the fine-laye...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>NASA Tests Atomic Clock for Deep Space Navigation</td>
      <td>February  6, 2018</td>
      <td>Project could help spacecraft keep time more e...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Mount Sharp 'Photobombs' Mars Curiosity Rover</td>
      <td>January 31, 2018</td>
      <td>A new self-portrait of NASA's Curiosity Mars r...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Vista From Mars Rover Looks Back Over Journey ...</td>
      <td>January 30, 2018</td>
      <td>A panoramic image that NASA's Curiosity Mars r...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>NASA's Next Mars Lander Spreads its Solar Wings</td>
      <td>January 23, 2018</td>
      <td>NASA's next mission to Mars passed a key test ...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Dust Storms Linked to Gas Escape from Mars Atm...</td>
      <td>January 23, 2018</td>
      <td>If Mars has a global dust storm in 2018, obser...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Steep Slopes on Mars Reveal Structure of Burie...</td>
      <td>January 11, 2018</td>
      <td>Researchers using NASA's Mars Reconnaissance O...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Mars Mission Sheds Light on Habitability of Di...</td>
      <td>December 13, 2017</td>
      <td>How long might a rocky, Mars-like planet be ha...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>NASA Mars Rover Team's Tilted Winter Strategy ...</td>
      <td>December  6, 2017</td>
      <td>NASA's senior Mars rover, Opportunity, has jus...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>NASA Builds Its Next Mars Rover Mission</td>
      <td>November 28, 2017</td>
      <td>In just a few years, NASA's next Mars rover mi...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Recurring Martian Streaks: Flowing Sand, Not W...</td>
      <td>November 20, 2017</td>
      <td>Seasonal dark streaks on Mars that previously ...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>NASA's Mars 2020 Mission Performs First Supers...</td>
      <td>November 14, 2017</td>
      <td>A 58-foot-tall Black Brant IX sounding rocket ...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>More Than 2.4 Million Names Are Going to Mars</td>
      <td>November  3, 2017</td>
      <td>Last month, NASA invited members of the public...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Martian Ridge Brings Out Rover's Color Talents</td>
      <td>November  1, 2017</td>
      <td>On a part of "Vera Rubin Ridge" where rover-te...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Next Mars Rover Will Have 23 'Eyes'</td>
      <td>October 31, 2017</td>
      <td>When NASA's Mars Pathfinder touched down in 19...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Mars Rover Mission Progresses Toward Resumed D...</td>
      <td>October 23, 2017</td>
      <td>NASA's Mars rover Curiosity team is working to...</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Take a Walk on Mars -- in Your Own Living Room</td>
      <td>October 19, 2017</td>
      <td>When NASA scientists want to follow the path o...</td>
    </tr>
    <tr>
      <th>38</th>
      <td>NASA’s MAVEN Mission Finds Mars Has a Twisted ...</td>
      <td>October 19, 2017</td>
      <td>Mars has an invisible magnetic “tail” that is ...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Mars Study Yields Clues to Possible Cradle of ...</td>
      <td>October  6, 2017</td>
      <td>The discovery of evidence for ancient sea-floo...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ------------------------------------------------------------
#  Step 3: Scrape Nasa Mars News website for featured image
# ------------------------------------------------------------
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
webpage = aux.getParsedWebpage(browser, url)

# get title and description
featured_title = soup.find(webpage, 'h1', class_='media_feature_title').get_text()
featured_description = soup.find(webpage, 'a', class_='button fancybox').get('data-description')

# get and construct url for largest size of featured image available
featured_url = soup.find(webpage, 'a', class_='button fancybox').get('data-fancybox-href')
featured_filename = featured_url.split('/')[4].split('_')[0]
featured_url = f'https://www.jpl.nasa.gov/spaceimages/images/largesize/{featured_filename}_hires.jpg'
print(featured_url)
```

    https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA14884_hires.jpg



```python
# ------------------------------------------------------------
#  Step 4: Scrape Mars Twitter for the most recent weather 
#  update
# ------------------------------------------------------------
url = 'https://twitter.com/marswxreport?lang=en'
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
weather_df
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Most Recent Weather on Mars</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>mars_date</th>
      <td>Sol 2029</td>
    </tr>
    <tr>
      <th>earth_date</th>
      <td>April 21, 2018</td>
    </tr>
    <tr>
      <th>cur_weather</th>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>temp_high</th>
      <td>-11C/12F</td>
    </tr>
    <tr>
      <th>temp_low</th>
      <td>-72C/-97F</td>
    </tr>
    <tr>
      <th>pressure</th>
      <td>7.22 hPa</td>
    </tr>
    <tr>
      <th>daylight</th>
      <td>05:25-17:21</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ------------------------------------------------------------
#  Step 5: Scrape Space Facts website for data on Mars
# ------------------------------------------------------------
url = 'https://space-facts.com/mars/'
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

fact_df
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facts about Mars</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Equatorial Diameter:</th>
      <td>6,792 km\n</td>
    </tr>
    <tr>
      <th>Polar Diameter:</th>
      <td>6,752 km\n</td>
    </tr>
    <tr>
      <th>Mass:</th>
      <td>6.42 x 10^23 kg (10.7% Earth)</td>
    </tr>
    <tr>
      <th>Moons:</th>
      <td>2 (Phobos &amp; Deimos)</td>
    </tr>
    <tr>
      <th>Orbit Distance:</th>
      <td>227,943,824 km (1.52 AU)</td>
    </tr>
    <tr>
      <th>Orbit Period:</th>
      <td>687 days (1.9 years)\n</td>
    </tr>
    <tr>
      <th>Surface Temperature:</th>
      <td>-153 to 20 °C</td>
    </tr>
    <tr>
      <th>First Record:</th>
      <td>2nd millennium BC</td>
    </tr>
    <tr>
      <th>Recorded By:</th>
      <td>Egyptian astronomers</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ------------------------------------------------------------
#  Step 6: Scrape images and titles from Astrogeology site
# ------------------------------------------------------------
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
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

# create dataframe
image_df = pd.DataFrame(image_list, columns=['title', 'image_url'])
image_df
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>image_url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Schiaparelli Hemisphere Enhanced</td>
      <td>http://astropedia.astrogeology.usgs.gov/downlo...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Valles Marineris Hemisphere Enhanced</td>
      <td>http://astropedia.astrogeology.usgs.gov/downlo...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Cerberus Hemisphere Enhanced</td>
      <td>http://astropedia.astrogeology.usgs.gov/downlo...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Syrtis Major Hemisphere Enhanced</td>
      <td>http://astropedia.astrogeology.usgs.gov/downlo...</td>
    </tr>
  </tbody>
</table>
</div>


