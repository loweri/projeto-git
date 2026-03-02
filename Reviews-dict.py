raw_prices = [
    {"timestamp": "10:00", "price": 61000},
    {"timestamp": "10:05", "price": "61500"}, # String!
    {"timestamp": "10:10", "price": None},    # Nulo!
    {"timestamp": "10:15", "price": 62000}
]
newprices = []
for item in raw_prices:
    prices = item["price"]
    if prices == None:
        continue
    else:
        final_price = int(item["price"])
        newprices.append(final_price)
print(newprices)
