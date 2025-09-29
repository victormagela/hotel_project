'''Utility functions for the hotel reservation system'''
import colors_and_title
import os
import locale
import json

script_directory = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_directory, 'reservation_data.json')


def valid_data_into_dict(name, cpf_input, guest_num, room_type_name, daily_room_rate, num_days_int, total_price):
    data_dict = {
        'Nome do cliente': name,
        'Cpf do cliente': cpf_input,
        'Número de hóspedes': guest_num, 
        'Tipo do quarto': room_type_name,
        'Preço da diária': daily_room_rate,
        'Número de dias a hospedar': num_days_int,
        'Total a pagar': total_price
    }
    return data_dict


def make_report(dict):
    '''Processes all the data into a concisive report'''

    os.system("cls")
    report = (    
        f'{colors_and_title.VERDE_NEGRITO}{"="*30}\n'
        f'RELATÓRIO DE RESERVA\n'
        f'{"="*30}\n'
        f'{colors_and_title.AMARELO_NEGRITO}Cliente : {dict['client_name']}\n'
        f'CPF: {dict['client_cpf']}\n'
        f'Quarto: {dict['room_name']}\n'
        f'Número de hóspedes: {dict['number_of_guests']}\n'
        f'Preço da diária: {colors_and_title.VERDE_NEGRITO}{locale.currency(dict['daily_rate'], grouping=True)}{colors_and_title.RESET}\n'
        f'{colors_and_title.AMARELO_NEGRITO}Número de dias a hospedar: {dict['number_of_days']}\n'
        f'Preço total: {colors_and_title.VERDE_NEGRITO}{locale.currency(dict['total_price'], grouping=True)}{colors_and_title.RESET}\n'
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
    
    
def save_reservation(dict):
    '''Saves the current reservation to a JSON file without overwriting any previous reservation saved on it.'''
    reservation_dict = read_file()  # In order to not overwrite anything, the save function must read the file, and then add to it.
    reservation_dict[f'{dict['client_name']}_{dict['client_cpf']}'] = dict
    with open(save_path, 'w', encoding='utf-8') as file:
        json.dump(reservation_dict, file, ensure_ascii=False, indent=4)