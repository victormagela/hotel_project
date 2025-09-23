import user_interface
import calculation_logic

# Defining main program function and execution
def main():
    '''Main program, receives the data from all other .py'''
    name, cpf_input, guest_num, room_type, num_days_int = user_interface.collect_guest_info()

    price_daily, total_price = calculation_logic.calculate_room_price(num_days_int, guest_num, room_type)

    user_interface.show_user_total_price(total_price)

    report = user_interface.make_report(room_type, name, cpf_input, guest_num, price_daily, num_days_int, total_price)

    print(report)


if __name__ == '__main__':
    main()