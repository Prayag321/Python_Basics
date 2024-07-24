    # @Date: 23-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 23-07-2024
    # @Title : Program to Check Whether an Alphabet is Vowel or Consonant 
def largest(first_number,second_number,third_number):
  """
    Description:
        This function check largest number .

    Parameters:
        first_number
        second_number
        third_number

    Returns:
        int:largest number
  """
  if(first_number>second_number and first_number>third_number):
    return first_number
  elif(second_number>first_number and second_number>third_number):
    return second_number
  else:
    return third_number
def main():
    #step 1 input a char
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
    print(f"largest number amoung {first_number},{second_number},{third_number} is {largest(first_number,second_number,third_number)}")


if __name__=="__main__":
    main()