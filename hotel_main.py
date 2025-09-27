import user_interface
import calculation_logic
import os
import colors_and_title

# Defining main program function and execution
def main():
    '''Main program, receives the data from all other .py'''
    while True:
        name, cpf_input, guest_num, room_type, num_days_int = user_interface.collect_guest_info()

        daily_room_rate, total_price = calculation_logic.calculate_room_price(num_days_int, guest_num, room_type)

        report = user_interface.make_report(room_type, name, cpf_input, guest_num, daily_room_rate, num_days_int, total_price)

        user_confirmation, reservation_reinput = user_interface.data_exit_and_confirmation(report, total_price)
        if reservation_reinput.startswith('n') or user_confirmation.startswith('s'):
            break
    
        else:
            os.system('cls')
            continue

    print(f'{colors_and_title.amarelo_nomal}Obrigado por usar o sistema de reservas do Resort das Marés!{colors_and_title.reset}')


if __name__ == '__main__':
    main()