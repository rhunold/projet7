import csv
import datetime
import math


"""
Dynamic programming
4.5 0/1 Knapsack - Two Methods - Dynamic Programming
https://www.youtube.com/watch?v=nLmhmB6NzcM

https://stackoverflow.com/questions/30554290/how-to-derive-all-solutions-from-knapsack-dp-matrix

d1actions.csv 1 results :
Share-GRUT,498.76,39.42
Total cost: 498.76â‚¬
Total return: 196.61â‚¬

d2actions.csv 18 results :
Share-ECAQ 3166
Share-IXCI 2632
Share-FWBE 1830
Share-ZOFA 2532
Share-PLLK 1994
Share-YFVZ 2255
Share-ANFX 3854
Share-PATS 2770
Share-NDKR 3306
Share-ALIY 2908
Share-JWGF 4869
Share-JGTW 3529
Share-FAPS 3257
Share-VCAX 2742
Share-LFXB 1483
Share-DWSK 2949
Share-XQII 1342
Share-ROOM 1506
Total cost: 489.24â‚¬
Profit: 193.78â‚¬

"""
MAX_VALUE = 500
file_path = "csv/20actions.csv"
# file_path = "csv/20actions_floats.csv"
file_path = "csv/d1actions.csv"


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
            # gain = gain_2decimal(gain)
            
            if profit > 0 and price > 0:
                price_per_gain = price/gain              
                action = {"name": name, "price": price, "profit": profit, "gain": gain, "price_per_gain" : price_per_gain}

                clean_data.append(action)
    clean_data.sort(key=lambda x: x["gain"], reverse=False)

    return clean_data




def getKnapsackTable(items, limit):
    matrix = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]
    for j in range(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in range(1, limit + 1):
            if wt > w:
                matrix[j][w] = matrix[j-1][w]
            else:
                matrix[j][w] = max(matrix[j-1][w], matrix[j-1][w-wt] + val)

    return matrix

def getItems(matrix, items):
    result = []
    I, j = len(matrix) - 1, len(matrix[0]) - 1
    for i in range(I, 0, -1):
        if matrix[i][j] != matrix[i-1][j]:
            item, weight, value = items[i - 1]
            result.append(items[i - 1])
            j -= weight

    return result


def display_result(W, result):
    result.sort(key=lambda x: x[2], reverse=True)

    total_gain = 0
    print(f"{'Actions' : <20} {'Prix' : <10} {'Gain'}")
    for action in result:
        name = action[0]

        price = action[1]
        gain = action[2]         
        total_gain += gain
        print(f"{name  : <20} {price : <10} {gain}")

    total_price = sum(i[1] for i in result)
    # total_gain = sum(i[2] for i in result)
    total_number = len(result)
        
    print()
    print(f"{total_number} actions pour un total investi de {total_price} "
          f"(sur {MAX_VALUE}) et un gain de {total_gain}")


def detect_float_price(wt, val):    
    W = MAX_VALUE
    for i, action in enumerate(wt):
        # At least one float
        if wt[i] != int(action):
            W = int(MAX_VALUE * 100)
            wt = [int(action*100) for action in wt]
            val = [gain*100 for gain in val]  
            # print(val)
            result = (W, wt, val)
            return result
    # All prices are int
    else:
        W = MAX_VALUE 
        wt = [int(action) for action in wt]
        result = (W, wt, val)
        
    return result

def restore_float(W, result_price):
    # if W == MAX_VALUE:
    #     result = (W, result_price, "toto")
    #     print("test")
    #     return result 
       
    if W != MAX_VALUE:
        # print("hello")
       
        new_result_price = []

        
        for action in result_price:

            action = list(action)
          
            action[1] = action[1] / 100
            action[2] = action[2] /100
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

    # total_price = sum(i[1] for i in result_price)
    # total_gain = sum(i[2] for i in result_price)
    # print(total_price)
    # print(total_gain)
    
    W = restore_float(W, result_price)[0]
    result = restore_float(W, result_price)[1]
    test = restore_float(W, result_price)
    
    # print(restore_float(W, result_price))
    
    # print(result)
    # print(W)   
    # print(test) 
    

    display_result(W, result)


    runtime = datetime.datetime.now() - start_time
    runtime = str(runtime)[5:]
    print(f"Temps d'execution : {runtime} s.")


if __name__ == '__main__':
    main()
