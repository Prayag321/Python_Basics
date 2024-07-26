'''
    @Author: Prayag Bhoir
    @Date: 25-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 25-07-2024 
    @Title : Python program to swap the nibbles and check it is power of 2 or not
'''

def to_binary(num):
    """
            Description:
                This function convert the decimal number to binary form
            Parameters:
                num : decimal number 
            Return:
                string : string of 0 and 1 with 8 padding
    """
    binary_no =""   #this is an empty string
    while num > 0:
        remainder = num % 2
        num = num // 2
        binary_no += str(remainder)
    binary_no = binary_no[::-1]
    return binary_no.zfill(8)#or we can use bin(value) thats return binary number
    


def swap_nibbles(num):
    """
            Description:
                This function swap the higher and lower nibble of number and gives new number using 
                bitwise and(&) operation
            Parameters:
                num : decimal number 
            Return:
                int : An decimal number after swapping the nibbles 
    """
    low_nibble = num & 0x0F
    high_nibble = (num & 0xF0) >> 4
    swapped = (low_nibble << 4) | high_nibble
    return swapped



def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0      #(n>0 and n has only one '1' bit in its binary representation)

def is_power_of_two(num):
    """
            Description:
                This function check the number is power of 2
            Parameters:
                num : decimal number 
            Return:
                boolean : true or false
    """
    if num <= 0:
        return False
    while num > 1:
        if num % 2 != 0:
            return False
        num = num // 2
    return True


def main():
    num = int(input("Enter an integer: "))
    
    binary_string = to_binary(num)
    print(f"Binary representation: {binary_string}")
    
    swapped_number = swap_nibbles(num)
    print(f"After nibble swapping: {swapped_number}")
    
    power_of_two = is_power_of_two(swapped_number)
    print(f"Is the number a power of 2? {power_of_two}")

if __name__ == "__main__":
    main()