    # @Author: Prayag Bhoir
    # @Date: 24-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 24-07-2024
    # @Title : Python program to generate coupons and check user vin or not (Lottery)
import random as rd
def coupon_generator(coupons):
  """
  Description:
    This function generates a specified number of unique coupon codes.

  Parameters:
    coupons (int): The number of unique coupon codes to generate. Must be a positive integer.

  Returns:
    list: A list containing the generated unique coupon codes.
          If the input is invalid (less than 1), an empty list is returned.
  """
  coupon_list=[]
  coupon_number = 0
  for i in range(coupons):
    coupon_number=rd.randint(1000,9999)
    if coupon_number not in coupon_list :
      coupon_list.append(coupon_number)
  return coupon_list
def main():
  coupons = int(input("Enter number of coupons to generate: "))
  user_coupon_number =int(input("Enter your coupon number :"))
  if user_coupon_number in coupon_generator(coupons):
    print("You win")
  else:
    print("You loose")
if __name__=="__main__":
  main()