    # @Date: 23-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 23-07-2024
    # @Title : Python program to find factors of a given number
def prime_factors(number:int):
    """
        Description:
            This function finds the prime factors 

        Parameters:
            number:for which prime factors to be find

        Returns:
           prime_factors
    """
    prime_factors=[]
    diviser = 2
    while number>diviser*diviser:
        while number%diviser==0:
            prime_factors.append(diviser)
            number//=diviser
        diviser+=1
    
    if(number>0):
        prime_factors.append(number)
    return prime_factors


def main():
    #step 1 input the number
    number = input("Enter the numebr: ")
    # step 2 validate is it number or not
    if(number.isdigit()):
        number=int(number)
        #step 3 check the number is greater than 0 or not
        if(number>0):
            number = int(number)
            print(f"Prime factors of {number} is ",prime_factors(number))
        else:
            print("Enter the positive number")
    else:
      print("Enter a valid number")

if __name__=="__main__":
    main()