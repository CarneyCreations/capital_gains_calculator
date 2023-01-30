import csv
# import tabulate


def calculate_cost_basis(cost, amount, fee):
    """ Calculates the cost basis of coins."""
    cost_basis = (float(cost) * float(amount)) + float(fee)
    print(f"({cost} * {amount}) + {fee} = {cost_basis}")
    return cost_basis


def separate_coins(trade):
    """ Organises each trade in a specific coin and a GBP pair to its own text file. """
    lead_coin = trade[1]
    buy_or_sell = trade[3]
    cost = trade[4]
    amount_executed = trade[5]
    fee = trade[7]

    if buy_or_sell == "BUY":
        pass
        cost_basis = calculate_cost_basis(cost, amount_executed, fee)
        trade[8] = cost_basis

    elif buy_or_sell == "SELL":
        pass
        print("Sell Side")


    lead_coin = open(lead_coin, "a+")           # End game for writing files.
    # lead_coin = open(lead_coin, "w+")         # To clear files.
    lead_coin.write(str(trade) + "\n")
    lead_coin.close()


def alternative_pair(no_cost_basis):
    """ Uploads any trades without a cost basis to a separate file where one will be created. """
    # crypto_crypto = open("alternative_pairs.txt", "w+")
    trades_to_be_processed = open("alternative_pairs.txt", "a+")
    trades_to_be_processed.write(str(no_cost_basis) + "\n")
    no_cost_basis_list.append(no_cost_basis)
    no_cost_basis_list.append("\n")



no_cost_basis_list = []
csv_data = []



while True:
    menu_selection = input("\n\n"
                           "1. Read and process CSV file.\n"
                           "2. Upload information to new files.\n"
                           "0. Exit program.\n"
                           ">>> ")


    # Read and process CSV file.
    if menu_selection == "1":
        # TODO: Display csv files in the directory folder and add an input that dictates which .csv to read.
        # encoding="ISO-8859-1" prevents the csv error:
        # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
        # binance_csv = open("/Users/josh/Git/capital_gains_calculator/binance/2020_2021_binance_split_pairs(complete).csv",
        #                    "r", encoding="ISO-8859-1")
        binance_csv = open("test_csv.csv",
                           "r", encoding="ISO-8859-1")

        # Converts from a TextIOWrapper to a csv.reader object.
        csvreader = csv.reader(binance_csv)

        # Adds the first row (header) to "csv_header" and iterates to the second row.
        csv_header = next(csvreader)


        # Converts from a csv.reader object in to a list.
        for each_trade in csvreader:
            for index, word in enumerate(each_trade[5:8]):        # For the fields with coin prices, fees or quantities.
                without_coin_name = ""                            # Resets value to avoid data redundancy.

                for character in word:
                    with_coin_name = character.strip(",ABCDEFGHIJKLMNOPQRSTUVWXYZ")      # Removes coin name and thousands seperator.
                    without_coin_name += with_coin_name
                    each_trade[index+5] = without_coin_name         # Reassigns the value with commas or letters.

            csv_data.append(each_trade)
        binance_csv.close()


    # Upload information to new files.
    elif menu_selection == "2":
        # for column in csvreader:

        # Needed to pass the crypto into the function.
        for column in csv_data:
            # crypto = column[1]
            # pair = column[2]
            # column = column.remove(",")

            if "GBP" in column[2]:                       # If already calculable.
                separate_coins(column)

            # If the pair isn't GBP/has no cost basis, it is added to a separate text file, ready for me to check
            # and assign the fair market value.
            elif "GBP" not in column[2]:
                alternative_pair(column)

        # Trades which are written to the alternate-pairs file.
        print(f"These are the trades which do not have a cost basis yet: \n{no_cost_basis_list}")


    # Exit program.
    elif menu_selection == "0":
        break

"""
So far the program:

Reads from a .csv file.
Converts the data to a readable list.
Moves each trade to its own <coin>.txt if the trading pair has a cost basis.
Otherwise it is written to a file, waiting to be processed.
"""

# TODO: Can I download/create a database which contains the historical (highest & lowest) or fair market value/average
#  price of each coin to automate calculation of the cost-basis.        Fair Market Value - Cost Basis = Capital Gain