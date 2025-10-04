import locale
import colors_and_title


class Reservation:
    daily_rate_table = {            # Class atribute to be used by all instances that want to calculate price
    '1' : {'1' : 20, '2' : 25},
    '2' : {'1' : 28, '2' : 34},
    '3' : {'1' : 35, '2' : 42},
    '4' : {'1' : 42, '2' : 50,},
    '5' : {'1' : 48, '2' : 57,},
    '6' : {'1' : 53, '2' : 63,}
    }


    def __init__(self, client_name, client_cpf, number_of_guests, room_type, number_of_days):
        self.client_name = client_name
        self.client_cpf = client_cpf
        self.number_of_guests = number_of_guests
        self.room_type = room_type
        self.number_of_days = int(number_of_days)
        self.room_name = 'Rei Tritão' if self.room_type == '1' else 'Princesa Ariel'
        self.daily_rate = 0
        self.total_price = 0

    def calculate_room_price(self):

        self.daily_rate = self.daily_rate_table[self.number_of_guests][self.room_type]
        self.total_price = self.daily_rate * self.number_of_days

    def generate_reservation_report(self):
        '''Processes all the data into a concisive report'''

        report = (    
            f'{colors_and_title.VERDE_NEGRITO}{"="*30}\n'
            f'RELATÓRIO DE RESERVA\n'
            f'{"="*30}\n'
            f'{colors_and_title.AMARELO_NEGRITO}Cliente : {self.client_name}\n'
            f'CPF: {self.client_cpf}\n'
            f'Quarto: {self.room_name}\n'
            f'Número de hóspedes: {self.number_of_guests}\n'
            f'Preço da diária: {colors_and_title.VERDE_NEGRITO}{locale.currency(self.daily_rate, grouping=True)}{colors_and_title.RESET}\n'
            f'{colors_and_title.AMARELO_NEGRITO}Número de dias a hospedar: {self.number_of_days}\n'
            f'Preço total: {colors_and_title.VERDE_NEGRITO}{locale.currency(self.total_price, grouping=True)}{colors_and_title.RESET}\n'
            )
        return report

    def update_reservation_name(self, new_name):
        self.client_name = new_name 

    def update_reservation_cpf(self, new_cpf):
        self.client_cpf = new_cpf 

    def update_reservation_guest_num(self, new_guest_num):

        if new_guest_num != self.number_of_guests:
            self.number_of_guests = new_guest_num 
            self.calculate_room_price()

    def update_reservation_room_type(self, new_room_type):

        if new_room_type != self.room_type:
            self.room_type = new_room_type 
            self.calculate_room_price()
            new_room_name = 'Rei Tritão' if new_room_type == '1' else 'Princesa Ariel'
            self.room_name = new_room_name

    def update_reservation_num_days(self, new_num_days):
        new_num_days_int = int(new_num_days) 

        if new_num_days_int != self.number_of_days:
            self.number_of_days = new_num_days_int 
            self.calculate_room_price()