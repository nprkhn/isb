import filework
import math
from scipy.special import gammainc

def frequency_bitwise_test(sequence: str) -> float:
    """
    First NIST test

    :param sequence: generated sequence
    :return result P
    """
    Sn = 0
    for char in sequence:
        if char == "1":
            Sn += 1
        else:
            Sn += -1
    
    Sn *= 1/math.sqrt(128)
    P = math.erfc(abs(Sn)/math.sqrt(2))

    return P

def  identical_consecutive_bits(sequence: str) -> float:
    """
    Second NIST test

    :param sequence: generated sequence
    :return result P
    """
    percentage_of_units = sequence.count("1") / 128
    P = 0

    if not percentage_of_units - 0.5 < (2 / math.sqrt(128)):
        P = 0
        return P
    
    V_N = sum(1 for i in range(len(sequence) - 1) if sequence[i] != sequence[i + 1])

    P = math.erfc(abs(V_N - 2 * 128 * percentage_of_units * (1 - percentage_of_units)) / (2 * math.sqrt(2 * 128) * percentage_of_units * (1 - percentage_of_units)))

    return P

def longest_sequence_of_units(sequence: str, constants: dict) -> float:
    """
    Third NIST test

    :param sequence: generated sequence
    :param constants: task's constants
    :return result P
    """
    statistic = {
        "V1": 0,
        "V2": 0,
        "V3": 0,
        "V4": 0
    }
    for i in range(len(sequence) // 8):
        max_len = 0
        current_len = 0
        block = sequence[(i * 8):(i * 8 + 8)]
        for num in block:
            if num == '1':
                current_len += 1
                if current_len > max_len:
                    max_len = current_len
            else:
                current_len = 0
        
        if max_len <= 1:
            statistic['V1'] += 1
        elif max_len == 2:
            statistic['V2'] += 1
        elif max_len == 3:
            statistic['V3'] += 1
        else:
            statistic['V4'] += 1
    
    first_comp = ((statistic['V1'] - 16 * constants["pi_0"]) ** 2) / (16 * constants["pi_0"])
    second_comp = ((statistic['V2'] - 16 * constants["pi_1"]) ** 2) / (16 * constants["pi_1"])
    third_comp = ((statistic['V3'] - 16 * constants["pi_2"]) ** 2) / (16 * constants["pi_2"])
    fourth_comp = ((statistic['V4'] - 16 * constants["pi_3"]) ** 2) / (16 * constants["pi_3"])

    square_X = first_comp + second_comp + third_comp + fourth_comp
    P = gammainc(1.5, square_X/2)
    return P

def main():
    cpp_sequence = filework.read_file('cpp_sequence.txt')
    java_sequence = filework.read_file('java_sequence.txt')
    constants = filework.read_json('const.json')
    print(f"\tCPP")
    print(f"Frequency bitwise test: {frequency_bitwise_test(cpp_sequence):.6f}")
    print(f"Identical consecutive bits test: {identical_consecutive_bits(cpp_sequence):.6f}")
    print(f"Longest sequence of units test: {longest_sequence_of_units(cpp_sequence, constants):.6f}\n")
    print(f"\tJava")
    print(f"Frequency bitwise test: {frequency_bitwise_test(java_sequence):.6f}")
    print(f"Identical consecutive bits test: {identical_consecutive_bits(java_sequence):.6f}")
    print(f"Longest sequence of units test: {longest_sequence_of_units(java_sequence, constants):.6f}")

    return 0

if __name__ == '__main__':
    main()
