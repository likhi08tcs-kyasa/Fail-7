def calculate_total(prices, tax_rate):
    total = sum(prices)
    return total + total * tax_rate


def average(values):
    return sum(values) / len(values) if values else 0
