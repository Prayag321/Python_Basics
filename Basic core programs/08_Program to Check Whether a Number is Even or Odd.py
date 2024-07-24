    # @Date: 23-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 23-07-2024
    # @Title : Program to Check Whether a Number is Even or Odd
def even_odd(number):
  """
    Description:
        Function to check whether a number is even or odd.

    Parameters:
        number (int): a number.

    Returns:
        str: "Number is even" if the number is even, otherwise "Number is odd".
  """
  if(number%2==0):
     return f"Number is even"
  else:
    return f"Number is odd"

def main():
    #step 1 input the number
    number = int(input("Enter the numebr: "))
    print(even_odd(number))


if __name__=="__main__":
    main()