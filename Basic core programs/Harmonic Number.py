    # @Date: 23-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 23-07-2024
    # @Title : Python program to calculate sum of harmonic series
def calculate_harmoniic(number:int):
    """
    Description:
        Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
    
    Parameters:
        number:number till we want series
    
    Returns:
       result:sumation of the series
    """     
    #step 4 calculate the series value
    result = 0
    for elem in range(1,number+1):
        result +=1/elem
    return result

def main():
    #step 1 input the number
    number = input("Enter the numebr: ")
    # step 2 validate is it number or not
    if(number.isdigit()):
        number = int(number)
        #step 3 check is it grater than 0 or not
        if(number>0):
            #just for fun to print the series
            temp = 1
            print("1 +",end=" ")
            while(temp<number+1):
                print(f"1/{temp} {'+' if(temp!=number) else '='}",end=" ")
                temp+=1

            print(f"{calculate_harmoniic(number):.2f}")
        else:
            print("Enter a positive integer")
    else:
        print(f"Invalid input {number}")
    
if __name__=="__main__":
    main()
