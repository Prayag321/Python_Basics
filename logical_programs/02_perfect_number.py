    # @Author: Prayag Bhoir
    # @Date: 24-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 24-07-2024
    # @Title : Python program to print fibonacii series
def factors(number):
  """
  Description:
    This function make a list of factors for a given number.

  Parameters:
    number (int): The number for which factors are to be found. Must be a positive integer.

  Returns:
    list: A list of factors of the given number.
  """
  factors = []
  for i in range(1,number):
    if number%i==0:
      factors.append(i)
  return factors
def perfect_number(number):
  """
  Description:
    This function checks if a given number is a perfect number.

  Parameters:
    number (int): The number to be checked. Must be a positive integer.

  Returns:
    bool: Returns True if the number is perfect, otherwise False.
  """
  if number==sum(factors(number)):
    return True
  else:
    return False



    

def main():
  number = int(input("Enter the number:"))
  if perfect_number(number):
    print("Perfect number")
  else:
    print("Not a Perfect number")

if __name__=="__main__":
  main()