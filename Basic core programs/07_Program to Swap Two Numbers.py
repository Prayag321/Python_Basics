    # @Date: 23-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 23-07-2024
    # @Title : Program to Swap Two Numbers
def swap(num1,num2):
  """
    Description:
        This function swaps the values of two numbers.

    Parameters:
        num1: The first number.
        num2: The second number.

    Returns:
        A tuple containing the swapped values of num2 and num1.
  """
  return num2,num1

def main():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the first number: "))
    first_number,second_number=swap(first_number,second_number)
    print(f"swaped number is {first_number},{second_number}")

if __name__=="__main__":
    main()