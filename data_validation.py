from colors_and_title import vermelho, reset
import os

'''Functions that validates data collected from user_interface'''
def guest_num_validation(guest_num):

    try:
        guest_num_int = int(guest_num)
        return 1 <= guest_num_int <= 6

    except (ValueError, TypeError):
        return False  

def room_type_validation(room_type):
    return room_type in ["1", "2"]

def num_days_validation(num_days):
    try:
        num_days_int = int(num_days) # Conversão para int
        
        if num_days_int > 0:
            return True
        
        else:
            return False
    
    except (ValueError, TypeError):
        return False


def cpf_digit_calculation(cpf_list):        

    countdown = list(range(len(cpf_list) + 1, 1, -1))

    cpf_sum = 0

    for i in range(len(cpf_list)):
        cpf_sum += (cpf_list[i] * countdown[i])

    calculated_digit = (cpf_sum * 10) % 11

    if calculated_digit > 9:
        calculated_digit = 0

    return calculated_digit

'''Bigger function to summarize CPF validation'''
def cpf_validation(cpf_input):
    if not cpf_input.isdigit() or len(cpf_input) != 11:
        return False

    if cpf_input.count(cpf_input[0]) == 11:
        return False
    
    else:
        cpf_list = [int(i) for i in cpf_input[:9]]

        first_digit = cpf_digit_calculation(cpf_list)

        cpf_list.append(first_digit)

        second_digit = cpf_digit_calculation(cpf_list)

        cpf_list.append(second_digit)

        cpf_list_comparison = [str(i) for i in cpf_list]
        cpf_comparison = ''.join(cpf_list_comparison)

        return cpf_comparison == cpf_input