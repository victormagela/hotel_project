# Functions that validates data collected from user_interface
def name_validation(name):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 100

    if not name or name.isdigit():
        return False
    
    elif len(name) <= MIN_NAME_LENGTH or len(name) > MAX_NAME_LENGTH:
        return False
    
    else:
        return True

def guest_num_validation(guest_num):
    MIN_NUMBER_GUESTS = 1
    MAX_NUMBER_GUESTS = 6

    try:
        guest_num_int = int(guest_num) # Conversion to int for validation
        return MIN_NUMBER_GUESTS <= guest_num_int <= MAX_NUMBER_GUESTS

    except (ValueError, TypeError):
        return False  


def room_type_validation(room_type):
    return room_type in ["1", "2"]


def num_days_validation(num_days):
    MIN_NUMBER_DAYS = 1
    MAX_NUMBER_DAYS = 15

    try:
        num_days_int = int(num_days) # Conversion to int for validation and calculation        
        return MIN_NUMBER_DAYS < num_days_int <= MAX_NUMBER_DAYS
    
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



def cpf_validation(cpf_input):
    '''Bigger function to summarize CPF validation'''
    if not cpf_input.isdigit() or len(cpf_input) != 11:    #CPF format validation
        return False

    if cpf_input.count(cpf_input[0]) == 11:    #CPF  repeated chars logic validation
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