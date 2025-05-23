# Stockbuddy

This repository contains code and artifacts I use for security selection as part of the magic formula investment strategy described in Joel Greenblatt's book The Little Book That Beats The Market.

Magic stocks generated using the free screener provided at 
https://www.magicformulainvesting.com/Screening/StockScreening

Criteria used:
Market cap > $100 million
Number of stocks: 30

Stockbuddy converts the html table into a csv with an added column for number of dividend payouts in the last 10 years

### To use Stockbuddy
1. Select stocks from the latest csv file in `output` into a Google sheet.
2. Buy these stocks and setup reminders 1 year from now
    - Taxable accounts: Setup a week long event from 2 days before the purchase date to 2 days after so that you can optimize for taxes
    - Tax-sheltered account: the distinction between short-term and long-term gains does not matter, a single reminder day is sufficient

### Update Schedule
output is updated approx every 3 months
