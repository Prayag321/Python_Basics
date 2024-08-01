    # @Author: Prayag Bhoir
    # @Date: 24-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 24-07-2024
    # @Title : Python program to print fibonacii series
def fibonacci_series(number):
  """
  Description:
    This function generates a Fibonacci sequence up to the specified number of elements.

  Parameters:
    number (int): The number of elements in the Fibonacci sequence to generate. Must be a positive integer.

  Returns:
    list: A list containing the Fibonacci sequence up to the specified number of elements.
    If the input is invalid (less than 1), an empty list is returned.
  """
  if number < 1:
    return []
  
  fibo_seq = [0,1]
  for i in range(2,number):
    fibo_seq.append(fibo_seq[-1]+fibo_seq[-2])
  
  return fibo_seq

def main():
  number = int(input("Enter the number:"))
  print(fibonacci_series(number))
if __name__=="__main__":
  main()