'''Logic to calculate prices'''
def calculate_room_price(num_days_int, guest_num, room_type):
    daily_rate_table = {
    '1' : {'1' : 20, '2' : 25},
    '2' : {'1' : 28, '2' : 34},
    '3' : {'1' : 35, '2' : 42},
    '4' : {'1' : 42, '2' : 50,},
    '5' : {'1' : 48, '2' : 57,},
    '6' : {'1' : 53, '2' : 63,}
}

    daily_room_rate = daily_rate_table[guest_num][room_type]
    total_price = daily_room_rate * num_days_int # Daily price times number of days

    return daily_room_rate, total_price
