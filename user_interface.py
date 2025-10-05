import colors_and_title
import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
import data_validation
import file_handler
import sys
from classes import Reservation

# Smaller function that collects user info one by one
def collect_guest_name():
    while True:
        name = input(f'{colors_and_title.AMARELO_NORMAL}'
        f'Favor informar seu nome completo para a reserva: {colors_and_title.RESET}').title().strip()

        os.system('cls')
        if data_validation.name_validation(name):
            return name

        else:
            print(f'{colors_and_title.VERMELHO_NORMAL}Nome inválido!{colors_and_title.RESET}')


def collect_guest_cpf():
    while True: 
        cpf_input = input(f'{colors_and_title.AMARELO_NORMAL}Favor digitar seu CPF: {colors_and_title.RESET}')\
        .replace(' ', '')\
        .replace('-', '')\
        .replace('.', '')

        os.system('cls')
        if data_validation.cpf_validation(cpf_input):
            return cpf_input
        
        else:
            print(f'{colors_and_title.VERMELHO_NORMAL}CPF inválido!{colors_and_title.RESET}')


def collect_guest_num():
    while True:
        guest_num = input(f'{colors_and_title.AMARELO_NORMAL}Favor informar o número de hóspedes(nossos quartos comportam de 1 a 6 pessoas): '
                          f'{colors_and_title.RESET}')
        
        os.system('cls')
        if data_validation.guest_num_validation(guest_num):
            return guest_num
        
        else:
            print(f'{colors_and_title.VERMELHO_NORMAL}Por favor, digite um número inteiro de 1 a 6.{colors_and_title.RESET}')


def collect_room_type():
    # Menu
    while True:
        room_type = input(f'''{colors_and_title.AMARELO_NORMAL}Favor, escolha do menu abaixo qual quarto vocês desejam:
    [1] Quarto 1, Rei Tritão
    [2] Quarto 2, Princesa Ariel
>>>>>> {colors_and_title.RESET}''')
        
        os.system('cls')
        if data_validation.room_type_validation(room_type) and room_type == '1':
            input(f'{colors_and_title.AMARELO_NEGRITO}Você escolheu o quarto: Rei Tritão!{colors_and_title.RESET}'
                  f'\n{colors_and_title.AMARELO_NORMAL}Digite qualquer tecla para continuar.{colors_and_title.RESET}')

        elif data_validation.room_type_validation(room_type) and room_type == '2':
            input(f'{colors_and_title.AMARELO_NEGRITO}Você escolheu o quarto: Princesa Ariel!{colors_and_title.RESET}'
                  f'\n{colors_and_title.AMARELO_NORMAL}Digite qualquer tecla para continuar.{colors_and_title.RESET}')
        
        else:
             print(f'{colors_and_title.VERMELHO_NORMAL}Favor escolher apenas entre quarto [1] ou [2].{colors_and_title.RESET}')
             continue
        
        os.system('cls')
        return room_type


def collect_num_days():
    while True:
        num_days = input(f'{colors_and_title.AMARELO_NORMAL}Favor digitar quantas dias ficarão hospedados: {colors_and_title.RESET}')
        
        os.system('cls')
        if data_validation.num_days_validation(num_days):
            num_days_int = int(num_days)
            return num_days_int

        else:
            print(f'{colors_and_title.VERMELHO_NORMAL}Desculpe, nossas reservas requerem um mímino de 1 dia e um máximo de 15 dias.'
                  f'{colors_and_title.RESET}')


def show_user_total_price(reservation):
    '''Displays processed data to the user'''
    os.system('cls')
    print(f'{colors_and_title.AMARELO_NORMAL}O total fica:{colors_and_title.RESET} {colors_and_title.VERDE_NEGRITO}'
          f'{locale.currency(reservation.total_price, grouping=True)}{colors_and_title.RESET}\n')
    input(f'{colors_and_title.AMARELO_NORMAL}Digite qualquer tecla para confirmar e prosseguir para o relatório: {colors_and_title.RESET}')


def show_report_and_ask_confirmation(report):    
    user_confirmation = input(f'{report}\n'
        f'{colors_and_title.AMARELO_NORMAL}\nDeseja confirmar sua reserva? Por favor, verifique se seus dados estão corretos. [s/n]'
        f'{colors_and_title.RESET}').strip().lower()
    return user_confirmation
    

def collect_guest_info():
    '''Larger function that groups all the smaller data collect related ones'''
    os.system('cls')
    print(f'{colors_and_title.VERDE_NEGRITO}\n---DADOS DO CLIENTE---{colors_and_title.RESET}')
    name = collect_guest_name()

    print(f'{colors_and_title.VERDE_NEGRITO}\n---DADOS DO CLIENTE---{colors_and_title.RESET}')
    cpf_input = collect_guest_cpf()

    print(f'{colors_and_title.VERDE_NEGRITO}\n---DADOS DA RESERVA---{colors_and_title.RESET}')
    guest_num = collect_guest_num()

    print(f'{colors_and_title.VERDE_NEGRITO}\n---DADOS DA RESERVA---{colors_and_title.RESET}')
    room_type = collect_room_type()

    print(f'{colors_and_title.VERDE_NEGRITO}\n---DADOS DA RESERVA---{colors_and_title.RESET}')
    num_days_int = collect_num_days()

    reservation = Reservation(name, cpf_input, guest_num, room_type, num_days_int)
    return reservation

def data_exit_and_confirmation(report, reservation):
    '''Function that groups smaller data exit and user confirmation related functions'''
    show_user_total_price(reservation)
    while True:
        os.system('cls')
        user_confirmation = show_report_and_ask_confirmation(report)

        os.system('cls')
        if user_confirmation.startswith('s'):
            input(f'{colors_and_title.AMARELO_NORMAL}Reserva confirmada! Obrigado por se hospedar no Resort das Marés!'
                f'\nDigite qualquer tecla para voltar ao começo.{colors_and_title.RESET}')
            return user_confirmation, ''

        elif user_confirmation.startswith('n'):
            print(f'{colors_and_title.VERMELHO_NORMAL}Reserva cancelada!{colors_and_title.RESET}')
            reservation_reinput = input(f'{colors_and_title.AMARELO_NORMAL}'
            f'Deseja refazer a reserva? Digite qualquer tecla para refazer ou "n" para sair: {colors_and_title.RESET}').strip().lower()
            return user_confirmation, reservation_reinput

        else:
            print(f'{colors_and_title.VERMELHO_NORMAL}Por favor, digite apenas "s" para sim ou "n" para não.{colors_and_title.RESET}')
            input(f'{colors_and_title.AMARELO_NORMAL}Digite qualquer tecla para voltar ao menu anterior.{colors_and_title.RESET}')


def display_main_menu():
    input(f'{colors_and_title.VERDE_NEGRITO}{colors_and_title.title}{colors_and_title.RESET}\n'
          f'{colors_and_title.AMARELO_NORMAL}Digite qualquer tecla para prosseguir para o menu principal: {colors_and_title.RESET}')
   
    while True:
        os.system('cls')
        option = input(f'''{colors_and_title.AMARELO_NORMAL}Por favor, escolha do menu abaixo qual das opções gostaria de seguir:
    [1] - Fazer nova reserva
    [2] - Consultar reserva antiga
    [3] - Encerrar o programa
>>>>>> {colors_and_title.RESET}''')

        if option not in ['1', '2', '3']:
            print(f'{colors_and_title.VERMELHO_NORMAL}Por favor, escolha apenas entre opções 1, 2 e 3.{colors_and_title.RESET}')
            continue

        else:
            return option
        
def get_reservation_details(reservation_dict):
    while True:
        os.system('cls')
        name_id = input(f'{colors_and_title.AMARELO_NORMAL}Por favor, digite seu nome para consultarmos nossa lista de reservas:  '
                        f'{colors_and_title.RESET}').title().strip()
        cpf_id = input(f'{colors_and_title.AMARELO_NORMAL}Por favor, digite seu CPF agora para finalizarmos nossa consulta:  '
                       f'{colors_and_title.RESET}').replace(' ', '').replace('-', '').replace('.', '')
        reservation_details_key = f'{name_id}_{cpf_id}'

        reservation_details = file_handler.find_reservation(reservation_dict, reservation_details_key)
        if not reservation_details:
            option_for_id_not_found = input(f'''{colors_and_title.AMARELO_NORMAL}Não conseguimos localizar sua reserva. Gostaria de:
            [1] Tentar novamente
            [2] Voltar ao menu anterior
        >>>>>>  {colors_and_title.RESET}''').strip()

            if option_for_id_not_found not in ['1', '2']:
                    input(f'{colors_and_title.VERMELHO_NORMAL}Por favor, escolha apenas entre opções 1 e 2. Digite qualquer tecla para voltar.'
                        f'{colors_and_title.RESET}')

            elif option_for_id_not_found == '1':
                continue

            elif option_for_id_not_found == '2':
                return None, None
            
        return reservation_details, reservation_details_key

def update_reservation(reservation_dict, reservation_object, reservation_details_key):
    while True:
        os.system('cls')
        data_change_input = input(
f'''{colors_and_title.AMARELO_NORMAL}Qual dos dados a seguir você gostaria de alterar:

    [1] Nome
    [2] CPF
    [3] Número de hóspedes
    [4] Tipo do quarto 
    [5] Número de dias hospedados 
    [6] Concluir alterações e encerrar o programa
>>>>>>  {colors_and_title.RESET}''').strip()

        if data_change_input not in ['1', '2', '3', '4', '5', '6']:
            input(f'{colors_and_title.VERMELHO_NORMAL}Por favor, escolha uma opcão entre 1 e 6. Digite qualquer tecla para voltar.'
                   f'{colors_and_title.RESET}')

        elif data_change_input == '1':
            new_name = input(f'{colors_and_title.AMARELO_NORMAL}Digite o novo nome:  {colors_and_title.RESET}').strip().title()
                            
            if data_validation.name_validation(new_name):
                reservation_object.update_reservation_name(new_name)
                input(f'\n{colors_and_title.VERDE_NEGRITO}Nome atualizado com sucesso! Digite qualquer tecla para voltar.'
                      f'{colors_and_title.RESET}')

            else:
                input(f'\n{colors_and_title.VERMELHO_NORMAL}Nome inválido! Digite qualquer tecla para tentar novamente.'
                      f'{colors_and_title.RESET}')

        elif data_change_input == '2':
            new_cpf = input(f'{colors_and_title.AMARELO_NORMAL}Digite o novo CPF:  {colors_and_title.RESET}')\
            .replace(' ', '')\
            .replace('-', '')\
            .replace('.', '')
                            
            if data_validation.cpf_validation(new_cpf):
                reservation_object.update_reservation_cpf(new_cpf)               
                input(f'\n{colors_and_title.VERDE_NEGRITO}CPF atualizado com sucesso! Digite qualquer tecla para voltar.'
                      f'{colors_and_title.RESET}')

            else:
                input(f'\n{colors_and_title.VERMELHO_NORMAL}CPF inválido! Digite qualquer tecla para tentar novamente.'
                      f'{colors_and_title.RESET}')

        elif data_change_input == '3':
            new_guest_num = input(f'{colors_and_title.AMARELO_NORMAL}Digite o novo número de hóspedes:  {colors_and_title.RESET}')
                            
            if data_validation.guest_num_validation(new_guest_num):
                reservation_object.update_reservation_guest_num(new_guest_num)
                input(f'\n{colors_and_title.VERDE_NEGRITO}Número de hóspedes atualizado com sucesso! Digite qualquer tecla para voltar.'
                      f'{colors_and_title.RESET}')

            else:
                input(f'\n{colors_and_title.VERMELHO_NORMAL}Número de hóspedes inválido! Digite qualquer tecla para tentar novamente.'
                      f'{colors_and_title.RESET}')

        elif data_change_input == '4':
            new_room_type = input(
f'''{colors_and_title.AMARELO_NORMAL}Favor, escolha do menu abaixo qual quarto vocês desejam:
    [1] Quarto 1, Rei Tritão
    [2] Quarto 2, Princesa Ariel
>>>>>> {colors_and_title.RESET}''')
                            
            if data_validation.room_type_validation(new_room_type):
                reservation_object.update_reservation_room_type(new_room_type)
                input(f'\n{colors_and_title.VERDE_NEGRITO}Tipo de quarto atualizado com sucesso! Digite qualquer tecla para voltar.'
                      f'{colors_and_title.RESET}')

            else:
                input(f'\n{colors_and_title.VERMELHO_NORMAL}Tipo de quarto inválido! Digite qualquer tecla para tentar novamente.'
                      f'{colors_and_title.RESET}')

        elif data_change_input == '5':
            new_num_days = input(f'{colors_and_title.AMARELO_NORMAL}Digite o novo número de dias a hospedar:  {colors_and_title.RESET}')
                            
            if data_validation.num_days_validation(new_num_days):
                reservation_object.update_reservation_num_days(new_num_days)
                input(f'\n{colors_and_title.VERDE_NEGRITO}Número de dias atualizado com sucesso! Digite qualquer tecla para voltar.'
                      f'{colors_and_title.RESET}')

            else:
                input(f'\n{colors_and_title.VERMELHO_NORMAL}Número de dias inválido! Digite qualquer tecla para tentar novamente.'
                      f'{colors_and_title.RESET}')

        else:
            os.system('cls')
            file_handler.save_reservation_after_update(reservation_dict, reservation_object, reservation_details_key)
            print(f'{colors_and_title.VERDE_NEGRITO}Alterações concluídas! Obrigado por se hospedar no Resort das Marés!'
                  f'{colors_and_title.RESET}')
            sys.exit()
                

def check_reservation_file(reservation_dict):
    if not reservation_dict:
        input(f'{colors_and_title.VERMELHO_NORMAL}Não há reservas salvas! Digite qualquer tecla para voltar ao menu anterior.'
              f'{colors_and_title.RESET}')
        return False
    
    return True


def prompt_old_reservation_options():
    while True:

        os.system('cls')
        update_or_cancel = input(
    f'''{colors_and_title.AMARELO_NORMAL}Por favor, escolha do menu abaixo qual das opções gostaria de seguir:
        [1] - Visualizar reserva antiga
        [2] - Alterar sua reserva antiga
        [3] - Cancelar sua reserva antiga
        [4] - Voltar ao menu anterior
    >>>>>> {colors_and_title.RESET}''')
                    
        if update_or_cancel not in ['1', '2', '3', '4']:
            input(f'{colors_and_title.VERMELHO_NORMAL}Por favor, escolha uma opcão entre 1 e 4. Digite qualquer tecla para voltar'
                f'{colors_and_title.RESET}')

        elif update_or_cancel == '1':
            return '1'

        elif update_or_cancel == '2':
            return '2'

        elif update_or_cancel == '3':
            return '3'
        
        return '4'
    

def display_reservation_deletion_msg():
    input(f'{colors_and_title.VERDE_NEGRITO}Reserva cancelada com sucesso! Digite qualquer tecla para voltar ao menu anterior.'
                f'{colors_and_title.RESET}')
            