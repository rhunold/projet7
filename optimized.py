import csv
import datetime

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
            if price*profit > 0:
                price = int(price*100)
                gain = int(price * profit) / 100
                action = {"name": name, "price": price, "profit": profit, "gain": gain}
                clean_data.append(action)
    clean_data.sort(key=lambda x: x["gain"], reverse=True)
    return clean_data


# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum gainsue that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # stores the result of Knapsack
    res = K[n][W]

    # Backtracking pour retrouver les valeurs associées
    selected_price = []

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            # This item is included.

            price = wt[i - 1]
            selected_price.append(price)

            # Since this weight is included, its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]

    return selected_price


def display_result(W, result_price, data):
    final_result = [i for i in data if i["price"] in result_price]
    final_result.sort(key=lambda x: x["gain"], reverse=True)

    total_gain = 0
    print(f"{'Actions' : <20} {'Prix' : <10} {'Gain'}")
    for action in final_result:
        name = action["name"]
        price = action["price"] / 100
        profit = action["profit"]
        gain = float(price)*float(profit) / 100
        total_gain += gain
        print(f"{name  : <20} {price : <10} {round(gain, 2)}")

    total_price = sum(result_price) / 100
    total_number = len(result_price)
    total_gain = round(total_gain, 2)
    print()
    print(f"{total_number} actions pour un total investi de {total_price} "
          f"(sur {W/100}) et un gain de {total_gain}")


def main():
    start_time = datetime.datetime.now()

    data = load_file(file_path)

    W = MAX_VALUE * 100

    val = [action['gain'] for action in data]  # gains
    wt = [action['price'] for action in data]  # prices

    n = len(wt)

    result_price = knapSack(W, wt, val, n)

    display_result(W, result_price, data)

    runtime = datetime.datetime.now() - start_time
    runtime = str(runtime)[5:]
    print(f"Temps d'execution : {runtime} s.")


if __name__ == '__main__':
    main()
