import csv
import tabulate


def separate_coins(lead_coin):
    """ Organises each trade in a specific coin and a GBP pair to its own text file. """
    for check_column in csv_data:
        if lead_coin == check_column[1] and "GBP" in check_column[2]:
            lead_coin = open(lead_coin, "a+")           # End game for writing files.
            # lead_coin = open(lead_coin, "w+")         # To clear files.
            lead_coin.write(str(column) + "\n")

    lead_coin.close()


double_crypto_pair = []
csv_data = []

# encoding="ISO-8859-1" prevents the csv error:
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
# binance_csv = open("/Users/josh/Git/capital_gains_calculator/Binance/2020-2021 Tax Year (complete) (SPLIT PAIRS).csv",
#                    "r", encoding="ISO-8859-1")
binance_csv = open("test_csv.csv",
                   "r", encoding="ISO-8859-1")

# Converts from a TextIOWrapper to a csv.reader object.
csvreader = csv.reader(binance_csv)

# Adds the first row (header) to "csv_header" and iterates to the second row.
csv_header = next(csvreader)

# Converts from a csv.reader object in to a list.
for row in csvreader:
    csv_data.append(row)
binance_csv.close()

# for column in csvreader:
for column in csv_data:
    crypto = column[1]
    pair = column[2]

    if "GBP" in pair:                       # If already calculable.
        separate_coins(crypto)

    # If the pair isn't GBP it is added to a separate text file, ready for me to check th fair market value.
    elif "GBP" not in pair:
        crypto_crypto = open("crypto_crypto_pair.txt", "a+")
        crypto_crypto.write(str(column) + "\n")
        double_crypto_pair.append(column)
        double_crypto_pair.append("\n")


print(double_crypto_pair)       # Trades which are written to the alternate-pairs file.

"""
So far the program:

Reads from a .csv file.
Converts the data to a readable list.
Moves each trade to its own <coin>.txt if the trading pair has a cost basis.
Otherwise it is written to a file, waiting to be processed.
"""

# TODO: Can I download/create a database which contains the historical (highest & lowest) or fair market value/average
#  price of each coin to automate calculation of the cost-basis.        Fair Market Value - Cost Basis = Capital Gain