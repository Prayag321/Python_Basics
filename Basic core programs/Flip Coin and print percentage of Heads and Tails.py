    # @Date: 23-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 23-07-2024
    # @Title : Python program to Flip Coin and print percentage of Heads and Tails
import random as rd
def coin_toss(coin_flips:int):
        """
        Description:
            This function simulates flipping a coin multiple/one times and returns the
            percentages of heads and tails.

        Parameters:
            coin_flip: The number of times the coin is flipped. Must be a positive integer.

        Returns:
            A tuple containing the percentages of tails and heads, respectively.
        """
        
        head_count = 0 
        tails_count = 0

        for i in range(coin_flips):
            rand_choice = rd.random()
            if(rand_choice>0.5):
                 tails_count+=1
            else:
                 head_count+=1
        return (tails_count*100)/coin_flips,(head_count*100)/coin_flips
                 
                    

def main():
    try:
        coin_flips = int(input("Enter the number of times to Flip Coin: "))
        if(coin_flips<= 0):
            print(f"invalid input {coin_flips},Enter positive number")
        else:
            head_perc,tail_perc=coin_toss(coin_flips)
            print(f"Percentage of Head:{head_perc:.2f}%\nPercentage of Tails:{tail_perc:.2f}%")
    except:
        print("Invalid input, String")

if __name__=="__main__":
    main()