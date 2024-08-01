'''
    @Author: Prayag Bhoir
    @Date: 25-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 25-07-2024 
    @Title : Python program to convert the temperature
'''


class Temperature:
    @staticmethod
    def temp_convert(unit,temperature):
        """
        Description:
            This function convert temperature from celcius to fahrenheit or vice versa.
        Parameters:
            unit: for matching celcius and fahrenheit formula
            temperature: passing temperature value for calculation
        Return:
            None
        """
        match unit:
            case 'C'|'c':
                celcius=temperature
                fahrenheit=(celcius*9/5)+32
                print(f"{celcius}°C is equal to {fahrenheit:.1f}°F")

            case 'F'|'f':
                fahrenheit=temperature
                celcius=(fahrenheit-32)*5/9
                print(f"{fahrenheit}°F is equal to {celcius:.1f}°C")
            case _:
                print("Invalid input, enter 'C' for Celsius or 'F' for Fahrenheit")
       
    

def main():
    temperature=int(input("Enter the Temperature: "))

    unit =input("Enter 'C' for Celsius or 'F' for Fahrenheit: ")

    Temperature.temp_convert(unit,temperature)



if __name__ == "__main__":
    main()