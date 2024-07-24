    # @Date: 23-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 23-07-2024
    # @Title : Program to Compute Quotient and Remainder
def calculate(dividand,diviser):
  """
        Description:
          Program to Compute Quotient and Remainder
          
        Parameters:
            dividand:number wich has to be divided
            diviser:number is to devide

        Returns:
            Quotient and Remainder
  """
  return dividand/diviser,dividand%diviser

def main():
    dividand = input("Enter the dividand: ")
    diviser = input("Enter the diviser: ")
    
    # step 2 validate is it number or not
    if(dividand.isdigit() and diviser.isdigit() ):
        diviser = int(diviser)
        dividand = int(dividand)
        #step 3 check diviser it grater than 0 or not
        if(diviser>0):
            quotient,remainder = calculate(dividand,diviser)
            print(f"The Quotient and Remainder is {quotient:.2f} , {remainder}")
        else:
            print("Enter a positive integer > 0 ")
    else:
        print("Invalid input ")
if __name__=="__main__":
    main()