    # @Author: Prayag Bhoir
    # @Date: 24-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 24-07-2024
    # @Title : Python program to check number is prime number or not
def prime_number(number):
  """
  Description:
    This function that checks a number is prime number or not

  Parameters:
    number(int):a number to check it is prime number or not

  Returns:
    bool: true if number is prime else false
  """


  for i in range(2,number):
     if number%i==0:
        return False    
  else:
     return True

def main():
    number = int(input("Enter a number: "))
    if prime_number(number):
      print(f"{number} is a prime number")
    else:
       print(f"{number} is not a prime number")
       
if __name__=="__main__":
  main()