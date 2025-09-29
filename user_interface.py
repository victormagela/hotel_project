import colors_and_title
import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
import data_validation

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


def collect_cpf():
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
            print(f'{colors_and_title.AMARELO_NEGRITO}Você escolheu o quarto: Rei Tritão!{colors_and_title.RESET}')
            return room_type

        elif data_validation.room_type_validation(room_type) and room_type == '2':
            print(f'{colors_and_title.AMARELO_NEGRITO}Você escolheu o quarto: Princesa Ariel!{colors_and_title.RESET}')
            return room_type
        
        else:
             print(f'{colors_and_title.VERMELHO_NORMAL}Favor escolher apenas entre quarto [1] ou [2]{colors_and_title.RESET}')


def collect_num_days():
    while True:
        num_days = input(f'{colors_and_title.AMARELO_NORMAL}Favor digitar quantas dias ficarão hospedados: {colors_and_title.RESET}')
        
        os.system('cls')
        if data_validation.num_days_validation(num_days):
            num_days_int = int(num_days)
            return num_days_int

        else:
            print(f'{colors_and_title.VERMELHO_NORMAL}Desculpe, nossas reservas requerem um mímino de 1 dia e um máximo de 15 dias.{colors_and_title.RESET}')


def show_user_total_price(total_price):
    '''Displays processed data to the user'''
    os.system('cls')
    print(f'{colors_and_title.AMARELO_NORMAL}O total fica:{colors_and_title.RESET} {colors_and_title.VERDE_NEGRITO}'
          f'{locale.currency(total_price, grouping=True)}{colors_and_title.RESET}\n')
    input(f'{colors_and_title.AMARELO_NORMAL}Digite qualquer tecla para confirmar e prosseguir para o relatório: {colors_and_title.RESET}')


def show_report_and_ask_confirmation(report):    
    user_confirmation = input(f'{report}\n'
        f'{colors_and_title.AMARELO_NORMAL}\nDeseja confirmar sua reserva? Por favor, verifique se seus dados estão corretos. [s/n]'
        f'{colors_and_title.RESET}').strip().lower()
    return user_confirmation
    

def collect_guest_info(dict):
    '''Larger function that groups all the smaller data collect related ones'''
    input(f'{colors_and_title.VERDE_NEGRITO}{colors_and_title.title}{colors_and_title.RESET}\n'
          f'{colors_and_title.AMARELO_NORMAL}Digite qualquer tecla para prosseguir para a reserva: {colors_and_title.RESET}')

    os.system('cls')
    print(f'{colors_and_title.VERDE_NEGRITO}\n---DADOS DO CLIENTE---{colors_and_title.RESET}')
    name = collect_guest_name()
    dict['client_name'] = name

    print(f'{colors_and_title.VERDE_NEGRITO}\n---DADOS DO CLIENTE---{colors_and_title.RESET}')
    cpf_input = collect_cpf()
    dict['client_cpf'] = cpf_input

    print(f'{colors_and_title.VERDE_NEGRITO}\n---DADOS DA RESERVA---{colors_and_title.RESET}')
    guest_num = collect_guest_num()
    dict['number_of_guests'] = guest_num

    print(f'{colors_and_title.VERDE_NEGRITO}\n---DADOS DA RESERVA---{colors_and_title.RESET}')
    room_type = collect_room_type()
    room_name = 'Rei Tritão' if room_type == '1' else 'Princesa Ariel'
    dict['room_type'] = room_type
    dict['room_name'] = room_name

    print(f'{colors_and_title.VERDE_NEGRITO}\n---DADOS DA RESERVA---{colors_and_title.RESET}')
    num_days_int = collect_num_days()
    dict['number_of_days'] = num_days_int

    return dict


def data_exit_and_confirmation(report, total_price):
    '''Function that groups smaller data exit and user confirmation related functions'''
    show_user_total_price(total_price)
    while True:
        user_confirmation = show_report_and_ask_confirmation(report)

        os.system('cls')
        if user_confirmation.startswith('s'):
            print(f'{colors_and_title.AMARELO_NORMAL}Reserva confirmada! Obrigado por se hospedar no Resort das Marés!'
                f'{colors_and_title.RESET}')
            return user_confirmation, ''

        elif user_confirmation.startswith('n'):
            print(f'{colors_and_title.VERMELHO_NORMAL}Reserva cancelada!{colors_and_title.RESET}')
            reservation_reinput = input(f'{colors_and_title.AMARELO_NORMAL}'
            f'Deseja refazer a reserva? Digite qualquer tecla para refazer ou "n" para sair: {colors_and_title.RESET}').strip().lower()
            return user_confirmation, reservation_reinput

        else:
            print(f'{colors_and_title.VERMELHO_NORMAL}Por favor, digite apenas "s" para sim ou "n" para não.{colors_and_title.RESET}')
            input(f'{colors_and_title.AMARELO_NORMAL}Digite qualquer tecla para voltar ao menu anterior.{colors_and_title.RESET}')