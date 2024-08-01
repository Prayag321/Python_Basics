'''
    @Author: Prayag Bhoir
    @Date: 25-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 25-07-2024 
    @Title : Python program to calculate the monthly loan payment
'''

class Loan():

    @staticmethod
    def monthly_pay(P,Y,R):

        """
        Description:
            This function calculate the Monthly loan payment.
        Parameters:
            P: Principle amount
            Y: duration (in year)
            R: Rate of interest
        Return:
            Float : monthly payment with 2 digit after point
        """

        r = R/(100*12)
        n = Y*12
        monthly_payment = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1)
        return round(monthly_payment,2)
    

def main():
    principal_amount= float(input("Enter the principal amount in rupees : "))
    years_to_pay_off= float(input("Enter the duration to pay off in year : "))
    annual_interest_rate= float(input("Enter the annual interest rate in percentage : "))

    monthly_payment = Loan.monthly_pay(principal_amount,years_to_pay_off,annual_interest_rate)
    print(f"Monthly loan payment : {monthly_payment}")

if __name__ == "__main__":
    main()