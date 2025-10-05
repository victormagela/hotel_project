from classes import Reservation

# reservation1 = Reservation('Victor', '31879732807', '3', '2', '4')

# reservation1.calculate_room_price()
# print(reservation1.daily_rate, reservation1.total_price)

# reservation1.update_reservation_num_days('5')
# print(reservation1.total_price)

# reservation2 = Reservation('Fernanda', '31879732807', '2', '1', '3')

# reservation2.calculate_room_price()
# print(reservation2.daily_rate, reservation2.total_price)

# reserva = Reservation("João Silva", "12345678900", "2", "1", "3")
# reserva.calculate_room_price()

# print(reserva.__dict__)

# reserva_dict = {
#     'client_name': 'João',
#     'client_cpf': '12345678900',
#     'number_of_guests': '2',
#     'room_type': '1',
#     'number_of_days': 3,
#     'daily_rate': 28,  # Esses campos extras
#     'total_price': 84,  # que vêm do JSON
#     'room_name': 'Rei Tritão'  # Esse também
# }

# reserva = Reservation(**reserva_dict)

# Teste 1: Criar do zero
reserva1 = Reservation('João', '123', '2', '1', 3)
print(f"Nova: {reserva1.daily_rate}, {reserva1.total_price}")

# Teste 2: Recriar do JSON
reserva2 = Reservation('Maria', '456', '3', '2', 5, 'Princesa Ariel', 42, 210)
print(f"Do JSON: {reserva2.daily_rate}, {reserva2.total_price}")