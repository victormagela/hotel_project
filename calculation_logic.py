'''Logic to calculate prices'''
def calculate_room_price(num_days_int, guest_num, room_type):
    prices_chart = {
    '1' : {'1' : 20, '2' : 25},
    '2' : {'1' : 28, '2' : 34},
    '3' : {'1' : 35, '2' : 42},
    '4' : {'1' : 42, '2' : 50,},
    '5' : {'1' : 48, '2' : 57,},
    '6' : {'1' : 53, '2' : 63,}
}

    price_daily = prices_chart[guest_num][room_type]
    total_price = price_daily * num_days_int # Valor da diária multiplicado pelo número de dias

    return price_daily, total_price
