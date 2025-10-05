'''Utility functions for the hotel reservation system'''
import colors_and_title
import os
import locale
import json
import calculation_logic

script_directory = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_directory, 'reservation_data.json')

def make_report(reservation_details):
    '''Processes all the data into a concisive report'''

    os.system("cls")
    report = (    
        f'{colors_and_title.VERDE_NEGRITO}{"="*30}\n'
        f'RELATÓRIO DE RESERVA\n'
        f'{"="*30}\n'
        f'{colors_and_title.AMARELO_NEGRITO}Cliente : {reservation_details['client_name']}\n'
        f'CPF: {reservation_details['client_cpf']}\n'
        f'Quarto: {reservation_details['room_name']}\n'
        f'Número de hóspedes: {reservation_details['number_of_guests']}\n'
        f'Preço da diária: {colors_and_title.VERDE_NEGRITO}{locale.currency(reservation_details['daily_rate'], grouping=True)}{colors_and_title.RESET}\n'
        f'{colors_and_title.AMARELO_NEGRITO}Número de dias a hospedar: {reservation_details['number_of_days']}\n'
        f'Preço total: {colors_and_title.VERDE_NEGRITO}{locale.currency(reservation_details['total_price'], grouping=True)}{colors_and_title.RESET}\n'
        )
    return report


def read_file():
    '''Tries to read reservation data from a JSON file. If the file does not exist, returns an empty dictionary.'''

    try:
        with open(save_path, 'r', encoding='utf-8') as file:
            loaded_data = json.load(file)
            reservation_dict = loaded_data
            return reservation_dict
    
    except FileNotFoundError:
        return {}
    
    
def save_reservation(reservation):
    '''Saves the current reservation to a JSON file without overwriting any previous reservation saved on it.'''
    reservation_dict = read_file()  # In order to not overwrite anything, the save function must read the file, and then add to it.
    reservation_dict[f'{reservation.client_name}_{reservation.client_cpf}'] = reservation.__dict__
    
    with open(save_path, 'w', encoding='utf-8') as file:
        json.dump(reservation_dict, file, ensure_ascii=False, indent=4)

def update_reservation_name(reservation_dict, reservation_details, new_name, old_name, cpf_id):
    reservation_details['client_name'] = new_name 
    old_key = f'{old_name}_{cpf_id}'
    new_key = f'{new_name}_{cpf_id}'
    # We check if the new key is indeed different from the old key, just so that the program doesn't need to do a redundant task
    
    if new_key != old_key:
        # The outcome of the expression to the right already returns the dictionary value that we want and is then assigned to new key
        reservation_dict[new_key] = reservation_dict.pop(old_key)


def update_reservation_cpf(reservations_dict, reservation_details, new_cpf, name_id, old_cpf):
    reservation_details['client_cpf'] = new_cpf 
    old_key = f'{name_id}_{old_cpf}'
    new_key = f'{name_id}_{new_cpf}'
    # We check if the new key is indeed different from the old key, just so that the program doesn't need to do a redundant task
    
    if new_key != old_key:
        # The outcome of the expression to the right already returns the dictionary value that we want and is then assigned to new key
        reservations_dict[new_key] = reservations_dict.pop(old_key)


def update_reservation_guest_num(reservation_details, new_guest_num):

    if new_guest_num != reservation_details['number_of_guests']:
        reservation_details['number_of_guests'] = new_guest_num 
        update_prices(reservation_details)

def update_reservation_room_type(reservation_details, new_room_type):

    if new_room_type != reservation_details['room_type']:
        reservation_details['room_type'] = new_room_type 
        update_prices(reservation_details)
        new_room_name = 'Rei Tritão' if new_room_type == '1' else 'Princesa Ariel'
        reservation_details['room_name'] = new_room_name


def update_reservation_num_days(reservation_details, new_num_days):
    new_num_days_int = int(new_num_days) 

    if new_num_days_int != reservation_details['number_of_days']:
        reservation_details['number_of_days'] = new_num_days_int 
        update_prices(reservation_details)

def update_prices(reservation_details):
    '''Function to recalculate prices if needed'''
    new_daily_rate, new_total_price = calculation_logic.calculate_room_price(
            reservation_details['number_of_days'],
            reservation_details['number_of_guests'],
            reservation_details['room_type'])

    reservation_details['daily_rate'] = new_daily_rate
    reservation_details['total_price'] = new_total_price


def save_reservation_after_update(reservation_dict):
    '''Saves the updated reservation dictionary to the JSON file.'''
    with open(save_path, 'w', encoding='utf-8') as file:
        json.dump(reservation_dict, file, ensure_ascii=False, indent=4)


def find_reservation(reservations_dict, name_id, cpf_id):
    return reservations_dict.get(f'{name_id}_{cpf_id}')