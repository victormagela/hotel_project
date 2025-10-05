'''Utility functions for the hotel reservation system'''
import colors_and_title
import os
import locale
import json

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


def save_reservation_after_update(reservation_dict, reservation, reservation_details_key):
    '''Deletes the old entry and then saves the updated reservation dictionary to the JSON file.'''
    del reservation_dict[reservation_details_key]
    reservation_dict[f'{reservation.client_name}_{reservation.client_cpf}'] = reservation.__dict__
    
    with open(save_path, 'w', encoding='utf-8') as file:
        json.dump(reservation_dict, file, ensure_ascii=False, indent=4)


def delete_reservation(reservation_dict, reservation_details_key):
    del reservation_dict[reservation_details_key]

    with open(save_path, 'w', encoding='utf-8') as file:
        json.dump(reservation_dict, file, ensure_ascii=False, indent=4)


def find_reservation(reservations_dict, reservation_details_key):
    return reservations_dict.get(reservation_details_key)