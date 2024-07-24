    # @Date: 23-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 23-07-2024
    # @Title : Python program to prints a table of the powers of 2
def print_power_table(input_number:int):
    """
        Description:
            This program takes a command-line argument N and prints a table of the
            powers of 2 that are less than or equal to 2^N.
       
        Parameters:
            input_number: Number till we want powers of 2
        
        Returns:
            none  
    """    
    #step 4 print the powers
    for num in range(input_number+1):
        print(f"2 ^ {num} = {2**num}")

def main():
    #step 1 input the number
    input_number = input("Enter the number : ")
    #step 2 validation of number
    if(input_number.isdigit()==False):
        print(f"Invalid input {input_number}. Please enter a positive integer.")
    else:
        input_number = int(input_number)
        #step 3 int vaidation as it overflow at 31
        if(31 >input_number >=0):
            print_power_table(input_number)
        else:
            print(f"Invalid number must be between 0 and 31")
    

if __name__=="__main__":
    main()