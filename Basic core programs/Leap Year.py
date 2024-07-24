    # @Author:Prayag Bhoir
    # @Date: 23-7-24
    # @Last Modified time: 23-07-2024
    # @Title : Python LeapYear program that takes a year as input and outputs the Year is a Leap Year or not a Leap Year
def check_leap_year():

    """
        Description:
            This function prints the year is leap year or not
        Parameters:
            none
        Returns:
            none  
    """
        #step 1 Input year
    year_input = input("Enter the year: ")

 
    if(year_input.isdigit()):
        #step 2 convert into integer and assign local scope
        year_input = int(year_input)
        #step 3 check it is greater than equal to 1582
        if(year_input<=1582):
            print(f"The year enteres {year_input}. must be 1582 or later")
        else:
            #step 4 check first leap year condition
            if(year_input % 100==0 and year_input % 400==0):
                print(f"The year {year_input} is a leap year")
            #step 5 check second leap tear condition
            elif(year_input % 4==0 and year_input % 100!=0):
                print(f"The year {year_input} is a leap year")
            else:
                print(f"The year {year_input} is not a leap year")
    else:
        print(f"Invalid year {year_input} entered. Please enter a valid year.".format(year_input))

def main():
    check_leap_year()
if __name__=="__main__":
    main()
