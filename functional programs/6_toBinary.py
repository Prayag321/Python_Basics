'''
    @Author: Prayag Bhoir
    @Date: 25-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 25-07-2024 
    @Title : Python program to convert the decimal number to binary form
'''
class D2B():

    @staticmethod
    def tobinary(number):
        """
            Description:
                This function convert the decimal number to binary 
            Parameters:
                number : decimal number given by user
            Return:
                binary_no (string) : string of 0 and 1 with 8 padding
        """

        binary_no =""   
        while number > 0:
            remainder = number % 2
            number = number // 2
            binary_no += str(remainder)
        binary_no = binary_no[::-1]

        return binary_no.zfill(8) #for padding


def main():
    number = int(input("Enter a Decimal number : "))
    print(f"The binary of Decimal number is {D2B.tobinary(number)}")

if __name__ == "__main__":
    main()