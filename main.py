def calculate_total_sales(sales_totals):
    if sales_totals == {}:
        return 0.0
    
    total = 0.0
    for key, value in sales_totals.items():
        total += value["quantity"] * value["price"]
    return total
        

def calculate_average_sales(sales_totals):
    if not sales_totals:
        return 0.0
    total_price = 0.0

    for key, value in sales_totals.items():
        total_price += value["quantity"] * value["price"]

    return total_price/len(sales_totals)

def filter_to_better_than_average_sales(sales_totals):
    if not sales_totals:
        return sales_totals
    
    filtered ={}
    total_price = 0
   
    for key, value in sales_totals.items():
        total_price += value["quantity"] * value["price"]
        average = total_price/len(sales_totals)
        if value["quantity"] * value["price"] > average:
            filtered[key]= value
    return filtered


    
def ninety_nine_bottles(count, beverage):
    pass
