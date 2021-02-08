# Curso Introdução a Linguagem Python - MIT MISTI Brazil–Unicamp
# Ana Luísa Fogarin - 05/02/2021
# a193948@dac.unicamp.br

# SET 2 - Problema 4

def largest_number(input_list):

    if input_list != []:
        best_so_far = float('-inf')
        for num in range(len(input_list)):
            current_num = input_list[num]

            if current_num > best_so_far:
                best_so_far = current_num

        return best_so_far
    
    return None

def second_largest_number(input_list):
    if len(input_list) != 0 and len(input_list) != 1:
        best_so_far = second_best_so_far = float('-inf')

        for num in input_list:
            if num > second_best_so_far:
                if num > best_so_far:
                    second_best_so_far = best_so_far
                    best_so_far = num
                else:
                    second_best_so_far = num
                    
        return second_best_so_far
    return None
