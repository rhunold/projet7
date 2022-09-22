import csv
import datetime
from itertools import combinations


CAPACITY = 50
file_path = "csv/5actions.csv"


def load_file(file_path):
    data = []
    # read csv file
    with open(file_path, mode='r') as file:
        csvBody = csv.DictReader(file)
        # displaying the contents of the CSV file
        for line in csvBody:
            action = dict(line)
            action["price"] = float(action["price"])
            action["gain"] = (action["price"] * float(action["profit"])/100)
            data.append(action)
    return data


def get_best_combination(data):
    """ Using the combination itertool to find the best combination"""
    data = sorted(data, key=lambda x: x["price"])
    selected_stocks = []
    total_invested = 0
    total_gain = 0
    best_combination = [selected_stocks, total_invested, total_gain]
    for i in range(len(data)):
        for combination in combinations(data, i):
            total_invested = 0
            total_gain = 0
            for element in combination:
                total_invested += element["price"]
                total_gain += element["gain"]
            if total_invested <= CAPACITY and total_gain > best_combination[2]:
                best_combination = [combination, total_invested, total_gain]
    return best_combination


def display_result(result, start_time):
    list_actions = list(result[0])
    total = result[1]
    total_gain = result[2]
    list_actions.sort(key=lambda x: x["gain"], reverse=True)

    print(f"{'Actions' : <20} {'Prix' : <10} {'Gain'}")
    for action in list_actions:
        name = action["name"]
        price = action["price"]
        gain = action["gain"]
        print(f"{name  : <20} {int(price) : <10} {gain}")
    print()
    nomber_actions = str(len(list_actions))
    print(f"{nomber_actions + ' actions' : <20} {total : <10} {total_gain}")
    runtime = datetime.datetime.now() - start_time
    runtime = str(runtime)[5:]
    print(f"Temps d'execution : {runtime} s.")


def main():
    start_time = datetime.datetime.now()

    data = load_file(file_path)
    result = get_best_combination(data)
    display_result(result, start_time)


if __name__ == '__main__':
    main()
