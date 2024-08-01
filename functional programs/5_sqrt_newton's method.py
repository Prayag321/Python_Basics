'''
    @Author: Prayag Bhoir
    @Date: 25-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 25-07-2024 
    @Title : Python program to find the square root of a number using newton formula
'''

class Squareroot():

    @staticmethod
    def sqrt(c):
        """
            Description:
                This function find the square root of a number using newton formula
            Parameters:
                c : number given by user to find the square root
            Return:
                float : square root in float with 3 digit after point
        """
        t = c
        epsilon = 1e-15
        while abs(t-c/t) > epsilon*t:
            t = (c/t + t) / 2
            
        return round(t,3)

def main():
    c = int(input("Enter the value for 'c' : "))

    if c > 0:
        print(f"Square root is {Squareroot.sqrt(c)}")
    else:
        print("Please enter a non-negative number")


if __name__ == "__main__":
    main()