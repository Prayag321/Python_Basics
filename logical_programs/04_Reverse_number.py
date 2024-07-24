    # @Author: Prayag Bhoir
    # @Date: 24-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 24-07-2024
    # @Title : Python program to reverse a given number
def reverse_number(number):
  """
  Description:
    This function that find reverse of a number

  Parameters:
    number(int):A number that is to be reverse

  Returns:
    rev_number(int): reverse of the number
  """
  rev_number=0
  digit=0
  for i in range(len(str(number))):
    digit=number%10
    rev_number=rev_number*10+digit
    number//=10
  return rev_number

def main():
  number = int(input("Enter a number: "))
  print(reverse_number(number))

if __name__=="__main__":
  main()