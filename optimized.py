import csv
import datetime
import math

"""
Dynamic programming
4.5 0/1 Knapsack - Two Methods - Dynamic Programming
https://www.youtube.com/watch?v=nLmhmB6NzcM

https://stackoverflow.com/questions/30554290/how-to-derive-all-solutions-from-knapsack-dp-matrix



"""
MAX_VALUE = 500

file_path = "csv/20actions.csv"


def load_file(file_path):

    # reading the CSV file
    with open(file_path, mode='r') as file:
        csvBody = csv.DictReader(file)
        clean_data = []
        for line in csvBody:
            action = dict(line)
            name = action["name"]
            price = float(action["price"])
            profit = float(action["profit"])
            gain = (price * profit) / 100
            if profit > 0 and price > 0:
                # price_per_gain = price/gain
                action = {"name": name, "price": price,
                          "profit": profit, "gain": gain}
                clean_data.append(action)
    clean_data.sort(key=lambda x: x["gain"], reverse=False)
    return clean_data


def getKnapsackTable(items, limit):
    matrix = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]
    for j in range(1, len(items) + 1):
        name, price, gain = items[j-1]
        for w in range(1, limit + 1):
            if price < w:
                matrix[j][w] = max(matrix[j-1][w], matrix[j-1][w-price] + gain)
            else:
                matrix[j][w] = matrix[j-1][w]
    return matrix


def getItems(matrix, items):
    result = []
    I, j = len(matrix) - 1, len(matrix[0]) - 1
    for i in range(I, 0, -1):
        if matrix[i][j] != matrix[i-1][j]:
            name, price, gain = items[i - 1]
            result.append(items[i - 1])
            j -= price

    return result


def get_decimal(number):
    return math.floor(number*100) / 100


def display_result(result):
    result.sort(key=lambda x: x[2], reverse=True)
    total_gain = 0
    print(f"{'Actions' : <20} {'Prix' : <10} {'Gain'}")
    for action in result:
        name = action[0]
        price = action[1]
        gain = action[2]
        total_gain += gain
        print(f"{name  : <20} {price : <10} {gain}")  # {gain}
    total_price = sum(i[1] for i in result)
    total_gain = sum(i[2] for i in result)
    total_number = len(result)
    print()
    print(f"{total_number} actions pour un total investi de"
          f"({get_decimal(total_price)} sur {MAX_VALUE})"
          f" et un gain de {get_decimal(total_gain)}.")


def detect_float_price(wt, val):
    W = MAX_VALUE
    for i, action in enumerate(wt):
        # At least one float
        if wt[i] != int(action):
            W = int(MAX_VALUE * 100)
            wt = [int(action*100) for action in wt]
            val = [gain*100 for gain in val]
            result = (W, wt, val)
            return result
    # All prices are int
    else:
        W = MAX_VALUE
        wt = [int(action) for action in wt]
        result = (W, wt, val)
    return result


def restore_float(W, result_price):
    if W != MAX_VALUE:
        new_result_price = []
        for action in result_price:
            action = list(action)
            action[1] = action[1] / 100
            action[2] = action[2] / 100
            action = tuple(action)
            new_result_price.append(action)
        return W, new_result_price
    else:
        W = MAX_VALUE
        return W, result_price


def main():
    start_time = datetime.datetime.now()

    data = load_file(file_path)

    val = [action["gain"] for action in data]  # gains
    wt = [action["price"] for action in data]  # prices
    names = [action["name"] for action in data]

    final_input = detect_float_price(wt, val)

    W = final_input[0]
    wt = final_input[1]
    val = final_input[2]

    items = list(zip(names, wt, val))

    matrix = getKnapsackTable(items, W)

    result_price = getItems(matrix, items)

    W = restore_float(W, result_price)[0]
    result = restore_float(W, result_price)[1]

    display_result(result)

    runtime = datetime.datetime.now() - start_time
    runtime = str(runtime)[5:]
    print(f"Temps d'execution : {runtime} s.")


if __name__ == '__main__':
    main()
