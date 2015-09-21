# Get Grailed
Trying to create a webscraper to pull Grailed data.

#Progress so far
I've pulled most of the element from a single webpage. This includes info like shipping, size, listing price. 
I still need to figure out how to grab price drop information. After this the goal is to store it in a .csv/

#Long Term
After grabbing all of the information from a single web page, I will use Scrapy to crawl Grailed and grab the corresponding info
for each new item listed. 

Based on my reaserch, I'll crawl Grailed once a day, and store the info in a Posregres database. From there I'll query it and do
statistical analysis. 
