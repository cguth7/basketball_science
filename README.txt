This was a quick project I did to prepare for the fantasy basketball season. I wanted to run a machine learning algorithm on an nba dataframe with both physical characteristics and stats. I generally use basketball reference for my NBA stats, but I realized there isn't a bbref page with both player stats and physical measurements. One option would be to pull the basic stats data frame from bbref using beautiful soup, and also take their heights from the site, which were not in a data frame but listed next to each players title, along with their name. I could have done this but figured there was a lot of potential for issues. Instead I decided to pull combine information from nba.com. In order to do this I needed to leverage selenium and chrome driver to local host the site and pull from it, since nba.com uses javascript that stopped me from parsing the source code straight from the web.

tldr;

- scraped basketball reference w/beautiful soup for basic stats table, converted the csv into dataframe with pandas
- used chrome driver and selenium to localhost nba.com, so that I could write a script to scroll through the page, and then also parsed with beautifulsoup
- combined the two data frames with a pandas merger, and did some very basic visualization with seaborn and matplotlib

