from classes import Reservation

reservation1 = Reservation('Victor', '31879732807', '3', '2', '4')

reservation1.calculate_room_price()
print(reservation1.daily_rate, reservation1.total_price)

reservation1.update_reservation_num_days('5')
print(reservation1.total_price)

reservation2 = Reservation('Fernanda', '31879732807', '2', '1', '3')

reservation2.calculate_room_price()
print(reservation2.daily_rate, reservation2.total_price)

reserva = Reservation("João Silva", "12345678900", "2", "1", "3")
reserva.calculate_room_price()

print(reserva.__dict__)