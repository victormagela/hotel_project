# Victor Mateus Magela Amato Ferreira

import user_interface
import calculation_logic
import os
import colors_and_title
import utils

# Defining main program function and execution
def main():
    '''Main program, receives the data from all other .py'''
    while True:
        option = user_interface.display_main_menu()

        if option == '1':
            os.system('cls')
            run_new_reservation()
        
        elif option == '2':
            os.system('cls')
            user_interface.reservation_management()

        else:
            os.system('cls')
            break

    print(f'{colors_and_title.AMARELO_NORMAL}Obrigado por usar o sistema de reservas do Resort das Marés!{colors_and_title.RESET}')


def run_new_reservation():
    while True:
        valid_data_dict = user_interface.collect_guest_info()

        daily_room_rate, total_price = calculation_logic.calculate_room_price(
                valid_data_dict['number_of_days'],
                valid_data_dict['number_of_guests'],
                valid_data_dict['room_type']
                )
            
        valid_data_dict['daily_rate'] = daily_room_rate
        valid_data_dict['total_price'] = total_price

        report = utils.make_report(valid_data_dict)

        user_confirmation, reservation_reinput = user_interface.data_exit_and_confirmation(report, total_price)
        if user_confirmation.startswith('s'):
            utils.save_reservation(valid_data_dict)
            break

            
        elif reservation_reinput.startswith('n'):
            break

        else:
            os.system('cls')


if __name__ == '__main__':
    main()