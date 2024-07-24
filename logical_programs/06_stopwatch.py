    # @Author: Prayag Bhoir
    # @Date: 24-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 24-07-2024
    # @Title : Python program to simulate the stopwatch
import time as t
def stopwatch():
  """
  Description:
    This function simulate the stopwatch

  Parameters:
    none

  Returns:
    none
  """
  input("Press enter to start stopwatch: ")
  start_time = t.time()
  input("press enter to stop: ")
  print(t.time()-start_time
  )

def main():
  stopwatch()

if __name__=="__main__":
  main()