# Victor Mateus Magela Amato Ferreira

import user_interface
import os
import colors_and_title
import file_handler
from classes import Reservation

# Defining main program function and execution
def main():
    '''Main program, receives the data from all other .py'''
    while True:
        os.system('cls')
        option = user_interface.display_main_menu()

        if option == '1':
            os.system('cls')
            run_new_reservation()
        
        elif option == '2':
            os.system('cls')
            run_reservation_management()

        else:
            os.system('cls')
            break

    print(f'{colors_and_title.AMARELO_NORMAL}Obrigado por usar o sistema de reservas do Resort das Marés!{colors_and_title.RESET}')


def run_new_reservation():
    while True:
        reservation = user_interface.collect_guest_info()

        report = reservation.generate_reservation_report()

        user_confirmation, reservation_reinput = user_interface.data_exit_and_confirmation(report, reservation)
        if user_confirmation.startswith('s'):
            file_handler.save_reservation(reservation)
            break

            
        elif reservation_reinput.startswith('n'):
            break

        else:
            os.system('cls')


def run_reservation_management():
    reservation_dict = file_handler.read_file()
    
    if user_interface.check_reservation_file(reservation_dict):
        reservation_details, reservation_details_key = user_interface.get_reservation_details(reservation_dict)
        if not reservation_details:
            return
        
        reservation = Reservation(**reservation_details)
        old_reservation_option = user_interface.prompt_old_reservation_options()

        if old_reservation_option == '1':
            report = reservation.generate_reservation_report()
            input(f'{report}\n' 
                f'{colors_and_title.AMARELO_NORMAL}\nDigite qualquer tecla para prosseguir{colors_and_title.RESET}')

        if old_reservation_option == '2':
            user_interface.update_reservation(reservation_dict, reservation, reservation_details_key)

        elif old_reservation_option == '3':
            file_handler.delete_reservation(reservation_dict, reservation_details_key)
            user_interface.display_reservation_deletion_msg()
        
        return

if __name__ == '__main__':
    main()