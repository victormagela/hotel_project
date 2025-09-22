# UMC 
# Programador
# https://patorjk.com/software/taag/
import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
verde_negrito = "\033[1;32m"
amarelo_nomal = "\033[0;33m"
amarelo_negrito = "\033[1;33m"
vermelho = "\033[0;31m"
reset = "\033[0m"
Tit='''
  ░██████   ░██████░███     ░███ ░██     ░██ ░██            ░███    ░███████     ░██████   ░█████████     ░███████   ░██████████    ░██     ░██   ░██████     ░██████   ░█████████  ░██████████ ░███████      ░███      ░██████  ░██████████ ░███     ░███ 
 ░██   ░██    ░██  ░████   ░████ ░██     ░██ ░██           ░██░██   ░██   ░██   ░██   ░██  ░██     ░██    ░██   ░██  ░██            ░██     ░██  ░██   ░██   ░██   ░██  ░██     ░██ ░██         ░██   ░██    ░██░██    ░██   ░██ ░██         ░████   ░████ 
░██           ░██  ░██░██ ░██░██ ░██     ░██ ░██          ░██  ░██  ░██    ░██ ░██     ░██ ░██     ░██    ░██    ░██ ░██            ░██     ░██ ░██     ░██ ░██         ░██     ░██ ░██         ░██    ░██  ░██  ░██  ░██        ░██         ░██░██ ░██░██ 
 ░████████    ░██  ░██ ░████ ░██ ░██     ░██ ░██         ░█████████ ░██    ░██ ░██     ░██ ░█████████     ░██    ░██ ░█████████     ░██████████ ░██     ░██  ░████████  ░█████████  ░█████████  ░██    ░██ ░█████████ ░██  █████ ░█████████  ░██ ░████ ░██ 
        ░██   ░██  ░██  ░██  ░██ ░██     ░██ ░██         ░██    ░██ ░██    ░██ ░██     ░██ ░██   ░██      ░██    ░██ ░██            ░██     ░██ ░██     ░██         ░██ ░██         ░██         ░██    ░██ ░██    ░██ ░██     ██ ░██         ░██  ░██  ░██ 
 ░██   ░██    ░██  ░██       ░██  ░██   ░██  ░██         ░██    ░██ ░██   ░██   ░██   ░██  ░██    ░██     ░██   ░██  ░██            ░██     ░██  ░██   ░██   ░██   ░██  ░██         ░██         ░██   ░██  ░██    ░██  ░██  ░███ ░██         ░██       ░██ 
  ░██████   ░██████░██       ░██   ░██████   ░██████████ ░██    ░██ ░███████     ░██████   ░██     ░██    ░███████   ░██████████    ░██     ░██   ░██████     ░██████   ░██         ░██████████ ░███████   ░██    ░██   ░█████░█ ░██████████ ░██       ░██ 
                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                           

Olá, bem vindo ao Resort das Marés.
'''

# Definindo funções 'funcionárias'
'''Funções que tem uma tarefa única e simples'''

def collect_guest_name():
    name = input(f'{amarelo_nomal}Favor informar seu nome para a reserva: ').title().strip()
    return name

def collect_guest_num():
        while True:

            try:
                guest_num = input('Favor informar o número de hóspedes(nossos quartos comportam de 1 a 6 pessoas): ')
                guest_num_int = int(guest_num)

                if guest_num_int > 6 or guest_num_int <= 0:
                    os.system('cls')
                    print(f'{vermelho}Por favor, digite um número inteiro de 1 a 6.{reset}')
                    continue

            except ValueError:
                os.system('cls')
                print(f'{vermelho}Por favor, digite um número inteiro de 1 a 6.{reset}')
                continue

            break
        
        return guest_num, guest_num_int

def collect_room_type():
    # Menu
    os.system("cls")
    while True:
        room_type = input('''
            Favor, escolha do menu abaixo qual quarto vocês desejam:
            [1] Quarto 1, Rei Tritão
            [2] Quarto 2, Princesa Ariel
            >>>>>> ''')
        
        if room_type not in ["1", "2"]:
            os.system("cls")
            print('Opção inválida. Favor inserir 1 ou 2.')
            continue
            
        elif room_type == "1":
            os.system("cls")
            print('Você escolheu o quarto: Rei Tritão!')
            break
            
        elif room_type == "2":
            os.system("cls")
            print('Você escolheu o quarto: Princesa Ariel!')
            break

        os.system("cls")
    
    return room_type

def collect_num_days():
    while True:

        try:
            num_days = input(f'{amarelo_nomal}Favor digitar quantas dias ficarão hospedados: ')
            num_days_int = int(num_days) # Conversão para int

            if num_days_int <= 0:
                os.system('cls')
                print(f'{vermelho}Por favor, digite um número inteiro maior que 0.{reset}')
                continue

        except ValueError:
            print(f'{vermelho}Por favor, digite um número inteiro maior que 0.{reset}')
            continue

        break

    return num_days_int

def calculate_room_price(num_days_int, guest_num, room_type):
    prices_chart = {
    '1' : {'1' : 20, '2' : 25},
    '2' : {'1' : 28, '2' : 34},
    '3' : {'1' : 35, '2' : 42},
    '4' : {'1' : 42, '2' : 50,},
    '5' : {'1' : 48, '2' : 57,},
    '6' : {'1' : 53, '2' : 63,}
}

    price_daily = prices_chart[guest_num][room_type]
    total_price = price_daily * num_days_int # Valor da diária multiplicado pelo número de dias

    return price_daily, total_price

def show_user_total_price(total_price):
    os.system('cls')

    print(f'{amarelo_nomal}O total fica:{reset} {verde_negrito}{locale.currency(total_price, grouping=True)}{reset}\n'
    f'{amarelo_nomal}Obrigado por se hospedar no Resort das Marés!')
    input(f'Digite qualquer tecla para confirmar e prosseguir para o relatório: {reset}')

def make_report(name, guest_num, room_type, price_daily, num_days_int, total_price): # Função que faz um relatório e o entrega ao programa principal

    os.system("cls")

    room_name = 'Rei Tritão' if room_type == '1' else 'Princesa Ariel'

    report = (    
        f'{verde_negrito}{"="*30}\n'
        f'RELATÓRIO DE RESERVA\n'
        f'{"="*30}\n'
        f'{amarelo_negrito}Cliente : {name}\n'
        f'Quarto: {room_name}\n'
        f'Número de hóspedes: {guest_num}\n'
        f'Preço da diária: {verde_negrito}{locale.currency(price_daily, grouping=True)}{reset}\n'
        f'{amarelo_negrito}Número de dias a hospedar: {num_days_int}\n'
        f'Preço total: {verde_negrito}{locale.currency(total_price, grouping=True)}{reset}\n'
        )
    return report


# Definindo funções 'gestoras'
'''Funções maiores que gerenciam outras funções menores'''

def collect_guest_info():   # Função para coletar dados do usuário e os retorna ao programa principal

    print(f'{verde_negrito}{Tit}{reset}')

    name = collect_guest_name()

    guest_num, guest_num_int = collect_guest_num()

    room_type = collect_room_type()

    num_days_int = collect_num_days()
    
    return name, guest_num, room_type, num_days_int, guest_num_int    

#Entrada de dados

name, guest_num, room_type, num_days_int, guest_num_int  = collect_guest_info()

# Processamento

price_daily, total_price = calculate_room_price(num_days_int, guest_num, room_type)

# Saída de dados

show_user_total_price(total_price)

report = make_report(name, guest_num, room_type, price_daily, num_days_int, total_price)

print(report)