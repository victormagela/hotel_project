import colors_and_title
import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
import data_validation

'''Collects user data one by one'''
def collect_guest_name():
    name = input(f'{colors_and_title.amarelo_nomal}Favor informar seu nome para a reserva: ').title().strip()
    return name

def collect_cpf():
    while True:
         
        cpf_input = input(f'{colors_and_title.amarelo_nomal}Favor digitar seu CPF: ')
        if data_validation.cpf_validation(cpf_input):
            break
        else:
            os.system('cls')
            print(f'{colors_and_title.vermelho}CPF inválido!{colors_and_title.reset}')
            continue
        
    return cpf_input

def collect_guest_num():
    while True:

        guest_num = input('Favor informar o número de hóspedes(nossos quartos comportam de 1 a 6 pessoas): ')
        if data_validation.guest_num_validation(guest_num):
            break
        else:
            os.system('cls')
            print(f'{colors_and_title.vermelho}Por favor, digite um número inteiro de 1 a 6.{colors_and_title.reset}')
                 
    return guest_num

def collect_room_type():
    # Menu
    while True:
        room_type = input('''
Favor, escolha do menu abaixo qual quarto vocês desejam:
    [1] Quarto 1, Rei Tritão
    [2] Quarto 2, Princesa Ariel
>>>>>> ''')
        
        if data_validation.room_type_validation(room_type):
             break
        else:
             os.system('cls')
             print(f'{colors_and_title.vermelho}Favor escolher apenas entre quarto [1] ou [2]{colors_and_title.reset}')
             continue
    
    os.system("cls")
    if room_type == "1":
            print('Você escolheu o quarto: Rei Tritão!')
            
    elif room_type == "2":
            print('Você escolheu o quarto: Princesa Ariel!')

    return room_type

def collect_num_days():
    while True:
        num_days = input(f'{colors_and_title.amarelo_nomal}Favor digitar quantas dias ficarão hospedados: ')
        
        os.system('cls')
        if data_validation.num_days_validation(num_days):
            num_days_int = int(num_days)
            break

        else:
            print(f'{colors_and_title.vermelho}Por favor, digite um número inteiro maior que 0.{colors_and_title.reset}')
            continue

    return num_days_int

'''Displays processed data to the user'''
def show_user_total_price(total_price):
    os.system('cls')

    print(f'{colors_and_title.amarelo_nomal}O total fica:{colors_and_title.reset} {colors_and_title.verde_negrito}{locale.currency(total_price, grouping=True)}{colors_and_title.reset}\n'
    f'{colors_and_title.amarelo_nomal}Obrigado por se hospedar no Resort das Marés!')
    input(f'Digite qualquer tecla para confirmar e prosseguir para o relatório: {colors_and_title.reset}')

'''Processes all the data into a concisive report'''
def make_report(room_type, name, cpf_input, guest_num, price_daily, num_days_int, total_price):

    os.system("cls")

    room_name = 'Rei Tritão' if room_type == '1' else 'Princesa Ariel'

    report = (    
        f'{colors_and_title.verde_negrito}{"="*30}\n'
        f'RELATÓRIO DE RESERVA\n'
        f'{"="*30}\n'
        f'{colors_and_title.amarelo_negrito}Cliente : {name}\n'
        f'CPF: {cpf_input}\n'
        f'Quarto: {room_name}\n'
        f'Número de hóspedes: {guest_num}\n'
        f'Preço da diária: {colors_and_title.verde_negrito}{locale.currency(price_daily, grouping=True)}{colors_and_title.reset}\n'
        f'{colors_and_title.amarelo_negrito}Número de dias a hospedar: {num_days_int}\n'
        f'Preço total: {colors_and_title.verde_negrito}{locale.currency(total_price, grouping=True)}{colors_and_title.reset}\n'
        )
    return report

'''Larger functions that groups all the smaller ones'''
def collect_guest_info():

    print(f'{colors_and_title.verde_negrito}{colors_and_title.title}{colors_and_title.reset}')

    name = collect_guest_name()

    cpf_input = collect_cpf()

    guest_num = collect_guest_num()

    room_type = collect_room_type()

    num_days_int = collect_num_days()

    return name, cpf_input, guest_num, room_type, num_days_int
