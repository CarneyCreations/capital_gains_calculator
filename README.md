# Cryptocurrency Tax Calculator (work-in-progress)
Calculates tax owed for cryptocurrency trading, as per the 2022 laws for Capital Gains tax in the UK.

## The Prompt
As a cryptocurrency trader, each year I have to submit my Capital Gains tax summary to the HMRC. Each year I have paid Koinly to generate my trading summary of the financial year including the tax I owe the government. This service was exceptional but having learnt programming, I decided to create my own tax calculator which my friends and I can use free of charge.

## Description
This program reads my trade history from a .csv and organises each trade into categories. First it determines which currency the user receives and whether more data is needed to calculate the cost-basis. From there each trade is divided into various trading rules: same-day, bed and breakfasting or section 104. Once both of these stages are complete, the program will run the final calculations and summarise: trading volume, allowable costs, capital gains, capital losses and tax owed. This information can then be included in a Self Assessment tax return for the HMRC.

## Improvements
* I still need to link access to historical day-trade prices which I will use a database/API for. This will determine a Fair Market Value price and allow for a cost-basis to be calculated for coin/coin trades. 
* Once I have a fully-functioning program I will add an feature that uses APIs to read from the Cryptocurrency platforms directly to increase automation. 
* Also I intend to build a front-end to enhance the user experience.

### Credits
Joshua Carney (CarneyCreations)
