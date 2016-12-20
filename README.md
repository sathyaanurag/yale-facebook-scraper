# yale-facebook-scraper
# Scrape Yale Facebook for all student emails

Due to Yale Facebook detecting robots, the entire process can't be automated. Instead, you have to take the HTML from Yale Facebook and store it in the individual college files. Then, run the script and it should generate the list and store it in a file called "email list".

Usage:

1. Go to Yale Facebook

2. For each of the colleges do the following:

  a. Right-click on an email address, and click 'Inspect Element'
  
  b. In the 'Elements' tab that just opened, scroll up to 'div class="display_data"'
  
  c. Right-click on that class and click 'Copy Element'
  
  d. Paste into appropriate college file in this directory
  
3. Run yale_facebook_scraper.py 
