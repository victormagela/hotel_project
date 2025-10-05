'''Utility functions for the hotel reservation system'''
import os
import json

script_directory = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_directory, 'reservation_data.json')


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